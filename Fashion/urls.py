from django.urls import path
from Fashion import views

urlpatterns = [
    path('', views.vocalforlocal13, name="vocalforlocal"),
    path('vocalforlocal/<int:vocalforlocalid>/',views.vocalforlocal1_addtocart,name="vocalforlocal1_addtocart"),
    path('vocalforlocal2/<int:vocalforlocalid>/',views.vocalforlocal2_addtocart,name="vocalforlocal2_addtocart"),
    path('shopclothings/<int:shopclothingsid>/',views.shopclothing_addtocart,name="shopclothing_addtocart"),
    path('shopfootwear/<int:shopfootwearid>/',views.shopfootwear_addtocart,name="shopfootwear_addtocart"),
    path('shopBudget/<int:shopBudgetid>/',views.shopBudget_addtocart,name="shopBudget_addtocart"),
    path('shopBeauty/<int:shopbeautyid>/',views.shopbeauty_addtocart,name="shopbeauty_addtocart"),





]
