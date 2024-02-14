from django.contrib import admin
from .models import Orders,Payment,OrderPet
# Register your models here.
admin.site.register(Orders)
admin.site.register(Payment)
admin.site.register(OrderPet)


