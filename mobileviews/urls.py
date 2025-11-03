# mobileviews/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart-mobile/<int:mainob_id>/', views.add_to_cart_mainob, name='add_to_cart_mobile'),
    path('footermobile/', views.footermobile_view, name='footermobile'),
    path('product_buy/<int:mainob_id>/',views.buy_now_mainob,name="buy_now_mainob"),
    path('product/<int:mainob_id>/',views.product_details_mainob,name="product_details_mainob")
]
