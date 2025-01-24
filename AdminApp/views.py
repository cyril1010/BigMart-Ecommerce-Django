from django.shortcuts import render,redirect

import datetime
from webapp.models import ContactDB
from .models import CategoryDB,ProductDB,Newsletter
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages



def admin_home_page(request):
    category = CategoryDB.objects.count()
    product = ProductDB.objects.count()
    date = datetime.datetime.now()
    return render(request,"index.html", {'category': category, 'product': product, 'date': date})



def CategoryDisplay(request):
    data = CategoryDB.objects.all()
    return render(request,"CategoryDisplay.html",{'data':data})

def CategoryAdd(request):
    return render(request,"CategoryAdd.html")

def CategoryEdit(request,cat_id):
    data = CategoryDB.objects.get(id=cat_id)
    return render(request, "CategoryEdit.html", {'data': data})


def CategorySave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES['image']
        category = CategoryDB(name=name, description=description, image=image)
        category.save()
        messages.success(request, "Category Saved Succesfully")
        return redirect('CategoryDisplay')

def CategoryDelete(request,cat_id):
    x = CategoryDB.objects.filter(id=cat_id)
    x.delete()
    messages.error(request, "Category Deleted")
    return redirect('CategoryDisplay')

def CategoryUpdate(request,cat_id):
    if request.method == 'POST':
        na = request.POST.get('name')
        de = request.POST.get('description')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            image_name = "category_images/" + image.name
            file = fs.save(image_name, image)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=cat_id).image
            image_path = file
        CategoryDB.objects.filter(id=cat_id).update(name=na, description=de, image=file)
        messages.success(request, "Data Updated Succesfully")
        return redirect('CategoryDisplay')


def ProductDisplay(request):
    data = ProductDB.objects.all()
    return render(request,"ProductDisplay.html",{'products': data})

def ProductAdd(request):
    category = CategoryDB.objects.all()
    return render(request,"ProductAdd.html",{'categories': category})


def ProductEdit(request, prod_id):
    category = CategoryDB.objects.all()
    data = ProductDB.objects.get(id=prod_id)
    return render(request, "ProductEdit.html", {'data': data, 'categories': category})


def ProductSave(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        ca = request.POST.get('category')
        pr = request.POST.get('price')
        de = request.POST.get('description')
        im = request.FILES.get('image')
        product = ProductDB(name=na,category=ca,price=pr,description=de,image=im)
        product.save()
        messages.success(request, "Product Added Succesfully")
        return redirect('ProductDisplay')

def ProductUpdate(request, prod_id):
    if request.method == 'POST':
        na = request.POST.get('name')
        de = request.POST.get('description')
        pr = request.POST.get('price')
        ca = request.POST.get('category')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage(location='media/product_images')
            image_name = "product_images/" + image.name
            file = fs.save(image_name, image)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=prod_id).image
            image_path = file
        ProductDB.objects.filter(id=prod_id).update(name=na,description=de,price=pr,category=ca,image=file)
        messages.success(request, "Product Updated Succesfully")
        return redirect('ProductDisplay')

def ProductDelete(request,prod_id):
    x = ProductDB.objects.filter(id=prod_id)
    x.delete()
    messages.error(request, "Product Deleted Succesfully")
    return redirect('ProductDisplay')


def admin_login_page(request):
    return render(request,"admin_login.html")

def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request, "Welcome to BigMart Admin Dashboard")
                return redirect('admin_home_page')
            else:
                messages.warning(request, "Invalid Password")
                return redirect('admin_login_page')
        else:
            messages.warning(request, "Invalid Username")
            return redirect('admin_login_page')

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect('admin_login_page')

def ContactDisplay(request):
    data = ContactDB.objects.all()
    return render(request,"ContactDisplay.html",{'data': data})

def ContactDelete(request,contact_id):
    x = ContactDB.objects.filter(id=contact_id)
    x.delete()
    return redirect('ContactDisplay')


def NewsLetterDisplay(request):
    data = Newsletter.objects.all()
    return render(request,"NewsletterDisplay.html", {'data': data})

