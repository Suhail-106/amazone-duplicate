# mobileviews/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart-mobile/<int:mobile_id>/', views.add_to_cart_mobile, name='add_to_cart_mobile'),
    path('mobile-cart/', views.cart_view_mobile, name='mobile_cart_view'),
    path('footermobile/', views.footermobile_view, name='footermobile'),
]
