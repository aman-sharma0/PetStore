from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from pets.models import Pet
from .models import Cart
from django.db.models import Sum
from django.contrib.auth.decorators import permission_required
# Create your views here.
def add_to_cart(request,pk):
    pet_object=Pet.pets.get(pk=pk)
    Cart(pet=pet_object,user=request.user,total_price=pet_object.price).save()
    #print(pet_object,request.user,pet_object.price)
    msg="pet added in cart"
    request.session['msg']=msg
    return redirect('homepage')

@permission_required("cart.view_cart")
def show_cart(request):
    cart_items=Cart.objects.filter(user=request.user)
    print(cart_items)
    flag=cart_items.exists()# it returns bool value , True when qs. contains object otherwise return Fals
    total_amount=Cart.objects.filter(user=request.user).aggregate(Sum('total_price'))
    totalamount=total_amount['total_price__sum']
    return render(request,'cart/mycart.html',{'flag':flag,'cart_item':cart_items,'totalamount':totalamount})

def update_cart(request):
    price=request.POST['price']
    qnt=request.POST['qnt']
    cart_id=request.POST['cart_id']
    total_price=float(price)*float(qnt)
    print(price,qnt,cart_id)
    Cart.objects.filter(id=cart_id).update(total_price=total_price,quantity=qnt)
    total_amount=Cart.objects.filter(user=request.user).aggregate(Sum('total_price'))
    totalamount=total_amount['total_price__sum']
    return JsonResponse({'totalprice':total_price,'totalamount':totalamount})

def delete_cart(request,pk):
    pet=Cart.objects.get(pk=pk)
    pet.delete()
    return redirect('cart:mycart')