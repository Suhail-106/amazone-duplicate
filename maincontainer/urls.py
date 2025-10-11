from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
 
    path('add-to-cart/<int:product_id>/<str:which_content>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart-mobile/<int:mobile_id>/', views.add_to_cartmobile, name='add_to_cartmobile'),
    path('products/', views.filtered_products, name='filtered_products'),
    path('add-to-product/<int:bestseller_id>/', views.filtered_products1, name="filtered_products1"),
   
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('Fresh/', views.fresh, name="fresh"),
    path('fresh/<int:fresh_id>/', views.fresh_addtocart, name="fresh_addtocart"),
    path('mobile/', views.mobilepage, name="mobile"),
    path('mobile<int:mainmobile_id>/', views.mainmobileaddtocart, name="mainmobileaddtocart"),
    path('electronics/', views.electronics, name="electronics"),
    path('electronics_laptop/<int:laptop_id>/', views.laptopaddtocart, name="laptopaddtocart"),
    path('electronics_headphones/<int:headphones_id>/', views.headphonesaddtocart, name="headphonesaddtocart"),
    path('electronics_stored/<int:stored_id>/', views.storedaddtocart, name="storedaddtocart"),
    path('autoupdate/',views.autoupdatedataandimage,name="autoupdatedataandimage"),
    path('form/',views.form,name="form"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),

   
]
