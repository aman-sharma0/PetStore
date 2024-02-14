from django.db import models
from django.contrib.auth.models import User
from pets.models import Pet

class Payment(models.Model):
    payment_id=models.CharField(max_length=30,default='123')
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    amount=models.FloatField(blank=True,null=True,default=1000.1)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    status=models.CharField(max_length=15,blank=True)
    class Meta:
        db_table='payment'
    def __str__(self) :
        return self.payment_id
class Orders(models.Model):
    states=[
       ('AP','Andhra Pradesh'), ('AR','Arunchal Pradesh'),('AS','Assam'),
       ('BR','Bihar'),('CG','Chhattisgarh'), ('GA','Goa'),('GJ','Gujrat'),('HR','Haryana'),
       ('HP','Himanchal Prdesh'),('MP','Madhya Pradesh'), ('MH','Maharashtra'),
       ('MZ','Mizoram'),('NL','Nagaland'),('OD','Odisha'), ('PB','Punjab'),
       ]
    status=[('new','new'),('pending','pending'),('delivered','deliverd'),('cancelled','cancelled')]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,blank=True,null=True)
    order_number=models.CharField(max_length=70)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    number=models.CharField(max_length=20)
    country=models.CharField(max_length=20,default="India")
    state=models.CharField(max_length=30,choices=states)
    status=models.CharField(max_length=20,choices=status,default='new')
    address=models.CharField(max_length=70,blank=True)
    ip=models.CharField(max_length=50)
    total=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='orders'
    def __str__(self):
        return self.first_name


class OrderPet(models.Model):
    order=models.ForeignKey(Orders,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_per_price=models.FloatField()
    is_ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='OrderPet'
    def __str__(self) :
        return self.pet.name
    
    




