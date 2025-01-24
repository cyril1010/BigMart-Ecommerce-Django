from django.urls import path
from . import views

urlpatterns = [
    path('admin_home_page/',views.admin_home_page,name="admin_home_page"),
    path('CategoryDisplay/', views.CategoryDisplay, name="CategoryDisplay"),
    path('CategoryAdd/', views.CategoryAdd, name="CategoryAdd"),
    path('CategoryEdit/', views.CategoryEdit, name="CategoryEdit"),
    path('CategorySave/', views.CategorySave, name="CategorySave"),
    path('CategoryEdit/<int:cat_id>/', views.CategoryEdit, name="CategoryEdit"),
    path('CategoryUpdate/<int:cat_id>/', views.CategoryUpdate, name="CategoryUpdate"),
    path('CategoryDelete/<int:cat_id>/', views.CategoryDelete, name="CategoryDelete"),

    path('ProductDisplay/', views.ProductDisplay, name="ProductDisplay"),
    path('ProductAdd/', views.ProductAdd, name="ProductAdd"),
    path('ProductSave/', views.ProductSave, name="ProductSave"),
    path('ProductEdit/<int:prod_id>/', views.ProductEdit, name="ProductEdit"),
    path('ProductUpdate/<int:prod_id>/', views.ProductUpdate, name="ProductUpdate"),
    path('ProductDelete/<int:prod_id>/', views.ProductDelete, name="ProductDelete"),

    path('ContactDisplay/', views.ContactDisplay, name="ContactDisplay"),
    path('ContactDelete/<int:contact_id>/', views.ContactDelete, name="ContactDelete"),
    path('NewsLetterDisplay/', views.NewsLetterDisplay, name="NewsLetterDisplay"),




    path('admin/', views.admin_login_page, name="admin_login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

]