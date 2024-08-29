from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('cart',views.cart_page,name='cart'),
    path('removecart/<str:cid>',views.remove_cart,name='removecart'),
    path('categories',views.categories,name='categories'),
    path('categories/<str:name>',views.categoriesview,name='categories'),
    path('categories/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('addtocart',views.add_to_cart,name='addtocart'),


]