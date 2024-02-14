from django.urls import path
from . import views
app_name='pets'
urlpatterns = [
     path('petlist/',views.PetList.as_view()),
   # path('<pk>/',views.petDetailView),#it must be last url
     path('homepage/',views.homepage),
     path('pricerange/',views.PetRangeView.as_view()),
     path('doglist/',views.Dog_List.as_view(),name="doglist"),
     path('addpet/',views.add_pets,name='addpet'),
      path('searchpet/',views.search_pet,name='searchpet'),
     
     path('<slug:slug>/',views.PetDetailView.as_view(),name="petdetail"),
  
]