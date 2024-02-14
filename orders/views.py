from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .forms import Orders_form
from datetime import date
from .models import Orders,Payment,OrderPet
from django.db.models import Q
from cart.models import Cart
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import json


def placeorder(request):
    form=Orders_form()
    print(request.GET)
    totalamount=request.GET['totalamount']
    if request.method=='POST':
        form=Orders_form(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.total=float(totalamount)
            data.ip=request.META['REMOTE_ADDR']      
            data.save()
            today=str(date.today()).replace('-','')
            ordernumber=today+str(data.id)
            data.order_number=ordernumber
            data.save() 
            qs_object=Orders.objects.filter(Q(user=request.user)& Q(order_number=ordernumber))
            
            orders_object=qs_object.first()#it will return first object from QS
            context={'order_number':ordernumber,'totalamount':totalamount,"order_obj":orders_object}   
            return render(request,'orders/payment_page.html',context)
   
    return render(request,'orders/billing_page.html',{'form':form})

def payments(request):
    
    body=json.loads(request.body)
    print(body,type(body))
    paymentId=body['transactionId']
    status=body['status']
    totalam=body['total']
    ordernumber=body['orderId']
    user=request.user
    payment=Payment(payment_id=paymentId,user=user,amount=totalam,status=status)
    payment.save()
    #assign payment object in payment attribute 
    orderObject=Orders.objects.filter(Q(user=request.user) & Q(order_number=ordernumber)).first()
    orderObject.payment=payment
    orderObject.save()
    
    # store values in OrderPetModel
    cart_item=Cart.objects.filter(user=request.user)
    print(cart_item)
    for item in cart_item: 
        q=item.quantity
        totalPerPrice=item.total_price
        pet=item.pet
        ord=OrderPet(order=orderObject,payment=payment,user=request.user,pet=pet,quantity=q,total_per_price=totalPerPrice,is_ordered=True)
        ord.save()
        item.delete()  
        #setting data into session object
        print(ordernumber)
        request.session["ordernumber"]=ordernumber
        request.session['paymentId']=paymentId
        mail_subject="Order Received"
        
        message=render_to_string('orders/Order_email.html',context={'ordersobject':orderObject,"ordernumber":ordernumber})
     
        to_email=orderObject.email
        email=EmailMessage(mail_subject,message,to=[to_email])
        print(email)
        email.send() 
    return JsonResponse({})

def orderplaced(request):
    ordernumber=request.session.get('ordernumber')
    paymentId=request.session.get('paymentId')
    print(ordernumber,paymentId)
    ordersObject=Orders.objects.get(order_number=ordernumber)
    paymentObject=Payment.objects.get(payment_id=paymentId)
    orderspetObject=OrderPet.objects.filter(order=ordersObject,payment=paymentObject)
    print(ordersObject,paymentObject,orderspetObject)
    context={'orderNumber':ordernumber,
             'paymentId':paymentId,
             'ordersObject':ordersObject,
             'paymentObject':paymentObject,
             'orderspetObject':orderspetObject}
    return render(request,'orders/order_completed_page.html',context=context)
