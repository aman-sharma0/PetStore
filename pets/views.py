from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView,DetailView
from .models import Pet
from .forms import PetRegisterForm
from cart.models import Cart
from django.db.models import Q 
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,"base/base.html")

class PetList(ListView):
   # model = Pet
   queryset=Pet.pets.all()
  
  
   #print(queryset)
   context_object_name="object"
   template_name="pets/list.html"
   
"""def petDetailView(request,pk):# replace pk with slug
    qs=Pet.objects.get(id=pk)
    print(qs)
    status=Cart.objects.filter(Q(pet=context['object']) & Q(user=self.request.user)).exists()
    return render(request,'pets/detail.html',{'qs':qs,'cartr_exist':status})
"""
class PetDetailView(DetailView):
    model=Pet
    context_object_name="qs"
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context=super().get_context_data(**kwargs)
        status=Cart.objects.filter(Q(pet=context['object']) & Q(user=self.request.user)).exists()
        context['pet_exists_incart']=status# adding data in contect object
        return context
   
        
    
class PetRangeView(ListView): 
   # queryset=Pet.pets.pet_range(1000,1500)
    queryset=Pet.petqs.age_filter(2)
    template_name="pets/list.html"

class Dog_List(ListView):#list will providename to object ie modelname_list or object_list name
     queryset=Pet.petqs.dog_list()
     template_name="account/index.html"

     #{'instance':querset}
     #context_object_name="instance"
     
def search_pet(request):
       
    query=request.POST.get("query")
    print("------",query)
    querySet=Pet.petqs.search(query)
    template_name="account/index.html"
    return render(request,template_name,{"object_list":querySet})
@login_required(login_url='/login/')
def add_pets(request):
    
    form=PetRegisterForm()
    #print("------------",request)
    #print(request.method)
    if request.method =="POST":
       form=PetRegisterForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('/pets/petlist/')
    return render(request,'pets/addpet.html',{'form':form}) 
    
    
    
    