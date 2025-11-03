from django.urls import path
from Fashion import views

urlpatterns = [
    path('', views.vocalforlocal13, name="vocalforlocal"),

    #--------------------vocalforlocal1-----------------------------------------------------------------------
  
    path('vocalforlocal/<int:vocalforlocalid>/',views.vocalforlocal1_addtocart,name="vocalforlocal1_addtocart"),
    path('product_vocalforlocal1/<int:vocalforlocal1_id>/', views.product_details_vocalforlocal1, name="Product_detailsvocalforlocal1"),
    path("buy-now-vocalforlocal1/<int:vocalforlocal1_id>/", views.buy_now_vocalforlocal1, name="buy_now_vocalforlocal1"),

   #------------------------vocalforlocal2----------------------------------------------------------------------
    
    path('vocalforlocal2/<int:vocalforlocalid>/',views.vocalforlocal2_addtocart,name="vocalforlocal2_addtocart"),
    path('product_vocalforlocal2/<int:vocalforlocal2_id>/', views.product_details_vocalforlocal2, name="Product_detailsvocalforlocal2"),
    path("buy-now-vocalforlocal2/<int:vocalforlocal2_id>/", views.buy_now_vocalforlocal2, name="buy_now_vocalforlocal2"),

    #------------------------------shopclothing----------------------------------------------------------
    path('shopclothings/<int:shopclothingsid>/',views.shopclothing_addtocart,name="shopclothing_addtocart"),
    path('product_shopclothing/<int:shopclothing_id>/', views.product_details_shopclothing, name="Product_detailsshopclothing"),
    path("buy-now-shopclothing/<int:shopclothing_id>/", views.buy_now_shopclothing, name="buy_now_shopclothing"),

    #-------------------------------shopfootwear----------------------------------------------------------
    path('shopfootwear/<int:shopfootwearid>/',views.shopfootwear_addtocart,name="shopfootwear_addtocart"),
    path('product_shopfootwear/<int:shopfootwear_id>/', views.product_details_shopfootwear, name="Product_detailsshopfootwear"),
    path("buy-now-shopfootwear/<int:shopfootwear_id>/", views.buy_now_shopfootwear, name="buy_now_shopfootwear"),

   #------------------------------------------ShopBudget ads ons-----------------------------------------
    path('shopBudget/<int:shopBudgetid>/',views.shopBudget_addtocart,name="shopBudget_addtocart"),
    path('product_shopBudget/<int:shopBudget_id>/', views.product_details_shopBudget, name="Product_detailsshopBudget"),
    path("buy-now-shopBudget/<int:shopBudget_id>/", views.buy_now_shopBudget, name="buy_now_shopBudget"),

    #----------------------------------------------shopbeauty------------------------------------------
    path('shopBeauty/<int:shopbeautyid>/',views.shopbeauty_addtocart,name="shopbeauty_addtocart"),
    path('product_shopbeauty/<int:shopbeauty_id>/', views.product_details_shopbeauty, name="Product_detailsshopbeauty"),
    path("buy-now-shopbeautyt/<int:shopbeauty_id>/", views.buy_now_shopbeauty, name="buy_now_shopbeauty"),



  path('product_<str:type>/<int:id>/', views.product_details, name="Product_details"),    



]
