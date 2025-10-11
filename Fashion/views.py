from django.shortcuts import render, get_object_or_404, redirect
from Fashion.models import vocalforlocal, vocalforlocal1, vocalforlocal2, shopclothing, shopfootwear, Budget_Add_Ons,shopBeauty
from maincontainer.models import CartItem
from django.http import JsonResponse

def vocalforlocal13(request):
    allvocalforloacal = vocalforlocal.objects.all()
    allvocalforloacal2 = vocalforlocal2.objects.all()
    allvocalforloacal1 = vocalforlocal1.objects.all()
    allshopclothing = shopclothing.objects.all()
    allshopfootwear = shopfootwear.objects.all()
    allBudgetaddons = Budget_Add_Ons.objects.all()
    allshopbeauty = shopBeauty.objects.all()
   
    return render(request,'fashion.html',{
    'vocalforlocal':allvocalforloacal,
    'vocalforlocal1':allvocalforloacal1,
    'vocalforlocal2':allvocalforloacal2,
    'shopclothing':allshopclothing,
    'shopfootwear':allshopfootwear,
    'Budgetaddons':allBudgetaddons,
    'shopbeauty':allshopbeauty,
    })

def vocalforlocal1_addtocart(request,vocalforlocalid):
    vocal = get_object_or_404(vocalforlocal,id=vocalforlocalid)
    
    pricevocal = vocal.price
    offervocal = vocal.offer
    intrestingvocal = vocal.interestincontent 

    if intrestingvocal is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingvocal,
        price = pricevocal,
        off174 = offervocal,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('vocalforlocal')    

def vocalforlocal2_addtocart(request,vocalforlocalid2):
    vocal1 = get_object_or_404(vocalforlocal1,id=vocalforlocalid2)
    
    pricevocal1 = vocal1.price1
    offervocal1 = vocal1.offer1
    intrestingvocal1 = vocal1.interestincontent1 

    if intrestingvocal1 is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingvocal1,
        price = pricevocal1,
        off174 = offervocal1,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('vocalforlocal')    

def shopclothing_addtocart(request,shopclothingsid):
    shopclo = get_object_or_404(shopclothing,id=shopclothingsid)
    
    priceshopclo = shopclo.priceshopclothing 
    intrestingshopclo = shopclo.contentshopclothing 

    if intrestingshopclo is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingshopclo,
        price = priceshopclo,
        off174 = 0,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('vocalforlocal')    

def shopfootwear_addtocart(request,shopfootwearid):
    shopfoot = get_object_or_404(shopfootwear,id=shopfootwearid)
    
    priceshopfoot = shopfoot.priceshopfootwear 
    intrestingshopfoot = shopfoot.contentshopfootwear 

    if intrestingshopfoot is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingshopfoot,
        price = priceshopfoot,
        off174 = 0,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('vocalforlocal')    

def shopBudget_addtocart(request,shopBudgetid):
    shopBudget = get_object_or_404(Budget_Add_Ons,id=shopBudgetid)
    
    priceshopBudget = shopBudget.priceshopBudget
    intrestingshopBudget = shopBudget.contentshopBudget 

    if intrestingshopBudget is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingshopBudget,
        price = priceshopBudget,
        off174 = 0,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('vocalforlocal')    

def shopbeauty_addtocart(request,shopbeautyid):
    shopbeauty = get_object_or_404(shopBeauty,id=shopbeautyid)
    
    priceshopbeauty = shopbeauty.priceshopBeauty
    intrestingshopbeauty = shopbeauty.contentshopBeauty 

    if intrestingshopbeauty is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingshopbeauty,
        price = priceshopbeauty,
        off174 = 0,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('vocalforlocal')    

# Create your views here.
