from django.urls import path
from . import views

urlpatterns = [
    path('',views.homekitchen, name="home&kitchen"),
    path('bedroom/<int:bedroomid>/',views.bedroomaddtocart,name="bedroomaddtocart")
]
