from django.urls import path
from . import views  

urlpatterns = [
    path('', views.gamecase_list, name='gamecase_list'),  
    path('<slug:slug>/', views.gamecase_page, name='gamecase_page'),
    
    
]

