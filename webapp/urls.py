from django.urls import path
from webapp import views

urlpatterns = [
    path('homepage/', views.homepage, name="home_page"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('save_contact/', views.save_contact, name="save_contact"),

    path('shop/', views.all_products, name="all_products"),
    path('filtered_page/<cat_name>/', views.filtered_page, name="filtered_page"),
    path('product_page/<prod_name>/', views.product_page, name="product_page"),
    path('', views.user_login_page, name="user_login_page"),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name='user_logout'),

    path('cart/', views.cart, name="cart"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('delete_cart/<pro_name>/', views.delete_cart_item, name="delete_cart"),

    path('save_newsletter/', views.newsletter, name="newsletter"),

    path('checkout/', views.checkout, name="checkout"),
    path('save_order/', views.save_order, name="save_order"),

    path('payment/', views.payment, name="payment"),

]