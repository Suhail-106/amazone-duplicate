from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
 
    path('add-to-cart/<int:product_id>/<str:which_content>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),

    #-----------------------------------bestseller of watch---------------------------------------
    path('products/', views.filtered_products, name='filtered_products'),
    path('add-to-product/<int:bestseller_id>/', views.filtered_products1, name="filtered_products1"),
    path('product_details_bestseller/<int:bestseller_id>/', views.product_details_bestseller, name="Product_detailsbestseller"),
    path("buy-now-bestseller/<int:bestseller_id>/", views.buy_now_bestseller, name="buy_now_bestseller"),




   #------------------------------------remove from cart.html urls-------------------------------
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

   #---------------------------------------mobilepage-----------------------------

    path('mobile/', views.mobilepage, name="mobile"),
    path('mobile<int:mainmobile_id>/', views.mainmobileaddtocart, name="mainmobileaddtocart"),
    path("buy-now-mobilepage/<int:mobilepage_id>/", views.buy_now_mobilepage, name="buy_now_mobilepage"),
    path('product_mainmobile/<int:mobilepage_id>/', views.product_details_mobilepage, name="Product_detailsmobilepage"),

    #------------------------------------electronics page----------------------------

    path('electronics/', views.electronics, name="electronics"),
    path('electronics_stored/<int:stored_id>/', views.storedaddtocart, name="storedaddtocart"),
    path('product_stored/<int:stored_id>/', views.product_details_viewelectronicsstored, name="Product_detailsstored"),
    path("buy-now-stored/<int:stored_id>/", views.buy_now_stored, name="buy_now_stored"),

    path('autoupdate/',views.autoupdatedataandimage,name="autoupdatedataandimage"),

    #-------------------------------------form urls------------------------------------------
    path('form/',views.form,name="form"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),

    #-------------------------------------product details in index.html-------------------------------------
    path('product/<int:product_id>/<str:which_content>/', views.product_detail, name='product_detail'),

   

    #--------------------------freshpage ------------------------------
    path('Fresh/', views.fresh, name="fresh"),
    path('product_fresh/<int:fresh_id>/', views.product_details_viewelectronicsfresh, name="Product_detailsfresh"),
    path('add-to-cart-fresh/<int:fresh_id>/', views.fresh_addtocart, name='add_to_cartfresh'),
    path("buy-now-fresh/<int:fresh_id>/", views.buy_now_fresh, name="buy_now_fresh"),
    

    #--------------------------------------homepage mobile ------------------------------------------------
    
    path('product_mobile/<int:mobile_id>/', views.product_details_viewelectronicsmobile, name="Product_detailsmobile"),
    path('add-to-cart-mobile/<int:mobile_id>/', views.add_to_cartmobile, name='add_to_cartmobile'),
    path("buy-now-mobile/<int:mobile_id>/", views.buy_now_mobile, name="buy_now_mobile"),
    

    #-----------------------------------------------electronics of headphones-------------------------------------

    path('product_headphones/<int:headphones_id>/', views.product_details_viewelectronicsheadphones, name="Product_detailsheadphones"),
    path('electronics_headphones/<int:headphones_id>/', views.headphonesaddtocart, name="headphonesaddtocart"),
    path("buy-now-headphones/<int:headphones_id>/", views.buy_now_headphones, name="buy_now_headphones"),

    #---------------------------------------electronics of laptop---------------------------------
    
    path('product_laptop/<int:laptop_id>/', views.product_details_viewelectronicslaptop, name="Product_detailslaptop"),
    path('electronics_laptop/<int:laptop_id>/', views.laptopaddtocart, name="laptopaddtocart"),
    path("buy-now-laptop/<int:laptop_id>/", views.buy_now_laptop, name="buy_now_laptop"),
   
   
   #----------------------------------funcion for product buy to paymentsuccess----------------------
    path("add-address/", views.add_address, name="add_address"),


    path('buy-now/<int:product_id>/<str:which_content>/', views.buy_now, name='buy_now'),

    path('payment-success/', views.payment_success, name="payment_success"),



   
]
