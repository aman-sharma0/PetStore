from typing import Iterable, Optional
from django.db import models
from django.db.models.signals import pre_save 
from django.utils.text import slugify
from django.db.models import Q
#from django.db.models.query import QuerySet

class PetQueryset(models.QuerySet):
    def age_filter(self,age):
        return self.filter(age__gt=age)
    def dog_list(self):
        return self.filter(animal_type="D")
    def search(self,query):
        return self.filter((Q(name__icontains=query) | Q(breed__icontains=query) | Q(age__icontains=query)
                           | Q(tag__tagname__icontains=query)))
                           
                           
                           
                           
                           
       

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-name')# ut is use tom arrnge data 
    def pet_range(self,r1,r2):
        print(self,r1,r2,"--------------")
        return super().get_queryset().filter(price__range=(r1,r2))  # field__range=(r1,r2)
    
   
    
class Pet(models.Model):
    gen=(("male","male"),("female","female"))
    name=models.CharField(max_length=25)
    slug=models.SlugField(max_length=40,blank=True,null=True)
    breed=models.CharField(max_length=25)
    spcies=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=gen)
    price=models.FloatField(default=1000)
    height=models.FloatField()
    image=models.ImageField(upload_to='media',default=" ")
    animal_type=models.CharField(max_length=3,choices=(('D',"Dog"),("C","Cat")),default="D")
    description=models.CharField(max_length=70)
    
    #pet=models.Manager()
    pets=CustomManager()
    petqs=PetQueryset.as_manager()
    
    
    
     
    class Meta:
        db_table='pets'
        
    def __str__(self):
        return self.name
"""def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        #before saving data
        #self.slug=self.breed
        return super().save()
        # after saving data"""
def pet_pre_save(sender,instance,*arg,**kwargs):
    #print(sender,instance,kwargs,arg)
    s="pet-breed-"+str(instance.breed)+"-"+str(instance.id)
    instance.slug=slugify(s)
    print('before saving data ')

pre_save.connect(pet_pre_save,sender=Pet)


#model for Search 

class Tag(models.Model):
    tagname=models.CharField(max_length=25)
    pet=models.ManyToManyField(Pet)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table="tag"
    
    def __str__(self) :
        return self.tagname





















