from django.urls import path
from . import views
from maincontainer import views as main_views 


urlpatterns = [
    path('', views.allcontent, name="New_Releases"),
    path('add-to-product/<int:bestseller_id>/', views.filtered_products1, name="New_Releases-filtered_products1"),
    path('electronics_laptop/<int:laptop_id>/', main_views.laptopaddtocart, name="New_Releases-laptopaddtocart"),
        
]
