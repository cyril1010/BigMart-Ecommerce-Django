from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,ProductDB,Newsletter
from webapp.models import ContactDB,UserDB,CartDB,OrderDB
from django.contrib import messages
import razorpay


def homepage(request):
    category = CategoryDB.objects.all()
    products = ProductDB.objects.all()
    cart = CartDB.objects.filter(username=request.session['Username'])
    x = cart.count()
    context = {
        'category': category,
        'products': products,
        'x': x
        }
    return render(request, "homepage.html", context)

def about(request):
    category = CategoryDB.objects.all()
    products = ProductDB.objects.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, "about_page.html", context)

def contact(request):
    category = CategoryDB.objects.all()
    products = ProductDB.objects.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, "contact_page.html", context)

def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        nu = request.POST.get('number')
        em = request.POST.get('email')
        me = request.POST.get('message')
        contact = ContactDB(name=na,number=nu,email=em,message=me)
        contact.save()
        return redirect('contact')

def newsletter(request):
    if request.method == "POST":
        em = request.POST.get('email')
        news = Newsletter(email=em)
        news.save()
        return redirect(homepage)



def all_products(request):
    products = ProductDB.objects.all()
    category = CategoryDB.objects.all()
    return render(request, "AllProducts.html", {'products': products,'category': category})



def filtered_page(request,cat_name):
    products = ProductDB.objects.filter(category=cat_name)
    category = CategoryDB.objects.all()
    return render(request, "Filtered_Page.html", {'products': products, 'category': category})

def product_page(request,prod_name):
    product = ProductDB.objects.get(name=prod_name)
    category = CategoryDB.objects.all()
    return render(request, "product_page.html", {'product': product, 'category': category})


def user_login_page(request):
    return render(request, "user_login_page.html")


def user_signup(request):
    if request.method == "POST":
        na = request.POST.get('name')
        un = request.POST.get('username')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        pa = request.POST.get('password')
        # hashed_password = make_password(pa)
        userOBJ = UserDB(name=na,username=un,email=em,phone=ph,password=pa)
        userOBJ.save()
        return redirect('user_login_page')


def user_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pa = request.POST.get('password')
        if UserDB.objects.filter(username=un, password=pa).exists():
            request.session['Username']=un
            request.session['Password']=pa
            messages.success(request, "Logged In Succesfully")
            return redirect('home_page')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('user_login_page')
    else:
        messages.warning(request, "Invalid Credentials")
        return redirect('user_login_page')

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.warning(request, "Succesfully Logged Out")
    return redirect('user_login_page')

def cart(request):
    sub_total = 0
    shipping_amount = 0
    cart = CartDB.objects.filter(username=request.session['Username'])
    for i in cart:
        sub_total += i.TotalPrice

    if sub_total>1000:
        shipping_amount=100
    else:
        shipping_amount=200
    total_amount = sub_total+shipping_amount

    context = {'cartproducts': cart, 'subtotal': sub_total, 'shippingamount': shipping_amount, 'totalamount': total_amount}
    return render(request,"cart.html", context)

def save_cart(request):
    if request.method == "POST":
        pro_name = request.POST.get('prod_name')
        un = request.POST.get('username')
        price = int(float(request.POST.get('mrp')))
        total_price = int(float(request.POST.get('total_mrp')))
        quantity = int(request.POST.get('qty'))  # Ensure quantity is an integer

        try:
            # Get the product image
            x = ProductDB.objects.get(name=pro_name)
            img = x.image
        except ProductDB.DoesNotExist:
            img = None

        try:
            # Check if the product is already in the cart for the user
            cartOBJ = CartDB.objects.get(ProductName=pro_name, username=un)
            cartOBJ.Quantity += quantity  # Update quantity
            cartOBJ.TotalPrice = cartOBJ.Quantity * price  # Update total price
            cartOBJ.save()
            messages.success(request, "Cart updated successfully!")
        except CartDB.DoesNotExist:
            # Create a new cart entry if it doesn't exist
            cartOBJ = CartDB(
                ProductName=pro_name,
                username=un,
                Price=price,
                TotalPrice=total_price,
                Quantity=quantity,
                Prod_Image=img,
            )
            cartOBJ.save()
            messages.success(request, "Added to cart")

        return redirect('home_page')


def delete_cart_item(request,pro_name):
    cart_item = CartDB.objects.filter(username=request.session['Username']).filter(ProductName=pro_name)
    cart_item.delete()
    message = f"{pro_name} has been removed from your cart."
    messages.success(request, message)
    return redirect('cart')


def checkout(request):
    cart = CartDB.objects.filter(username=request.session['Username'])
    sub_total = 0
    shipping_amount = 0
    for i in cart:
        sub_total += i.TotalPrice

    if sub_total>1000:
        shipping_amount=100
    else:
        shipping_amount=200
    total_amount = sub_total+shipping_amount

    context = {'cartproducts': cart, 'subtotal': sub_total, 'shippingamount': shipping_amount, 'totalamount': total_amount}
    return render(request, "checkout.html",context)

def save_order(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        message = request.POST.get('message')
        total_price = request.POST.get('total_price')

        order = OrderDB(name=name,email=email,place=place,address=address,mobile=mobile,
                        state=state,pin=pin,message=message,total_price=total_price)
        order.save()
        return redirect('payment')
    else:
        return redirect('checkout')


def payment(request):
    cart = CartDB.objects.filter(username=request.session['Username'])
    sub_total = 0
    shipping_amount = 0
    for i in cart:
        sub_total += i.TotalPrice
    if sub_total > 1000:
        shipping_amount = 100
    else:
        shipping_amount = 200
    total_amount = sub_total + shipping_amount


    #Retreive the data from OrderDB with specified ID
    customer = OrderDB.objects.order_by('-id').first()
    payy = customer.total_price

    amount  = int(payy*100)

    payy_str = str(amount)


    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_gI8v8djb3KFaLP', 't1fVvLOrj5kyW0C3MfFod1dZ'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})
        print("Hello")


    context = {'cartproducts': cart, 'subtotal': sub_total, 'shippingamount': shipping_amount,
               'totalamount': total_amount, 'customer': customer, 'payy_str': payy_str}

    return render(request, "payment.html", context)


