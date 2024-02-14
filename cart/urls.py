from django.urls import path
from .views import add_to_cart,show_cart,update_cart,delete_cart

app_name='cart'

urlpatterns = [
    path('addcart/<int:pk>',add_to_cart,name='addcart'),
    path('mycart/',show_cart,name='mycart'),
    path('updatecart/',update_cart,name='updatecart'),
    path('deletecart/<pk>',delete_cart,name='deletecart')
    
    
]