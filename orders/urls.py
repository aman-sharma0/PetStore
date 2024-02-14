from django.urls import path
from .views import placeorder,payments,orderplaced


app_name='orders'

urlpatterns = [
    path('placeorder/',placeorder,name='placeorder'),
     path('payments/',payments, name='payments'),
     path('orderplaced/',orderplaced, name='orderplaced'),
    
 
]