from django.shortcuts import render, get_object_or_404,redirect
from HomeandKitchen.models import bedroom
from maincontainer.models import CartItem

def homekitchen(request):
    allbedroom = bedroom.objects.all()
    return render(request,'home&kitchen.html',{'bedroom':allbedroom})

def bedroomaddtocart(request,bedroomid):
    bedroom1 = get_object_or_404(bedroom, id=bedroomid)

    bedroomcontent = bedroom1.content
    bedroomprice = bedroom1.price

    if bedroomcontent is None:
        return redirect('home&kitchen')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        off174 = 0,
        price = bedroomprice,
        content = bedroomcontent,
        defaults={'quantity':1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('home&kitchen')    

# Create your views here.
