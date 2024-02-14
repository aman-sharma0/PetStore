from django.db import models
from pets.models import Pet
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price=models.FloatField(default=10000)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='cart'