from django.urls import path
from . import views

urlpatterns = [
    path('',views.homekitchen, name="home&kitchen"),
    path('bedroom/<int:bedroomid>/',views.bedroomaddtocart,name="bedroomaddtocart"),
    path('product_bedroom/<int:bedroom_id>/', views.product_details_bedroom, name="Product_detailsbedroom"),
    path("buy-now-bedroom/<int:bedroom_id>/", views.buy_now_bedroom, name="buy_now_bedroom"),

]
