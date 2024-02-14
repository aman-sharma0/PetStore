from django.contrib import admin
from .models import Pet,Tag

# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display=['id','name','age','breed','spcies','age','gender','height','image']

admin.site.register(Pet,PetAdmin)


admin.site.register(Tag)