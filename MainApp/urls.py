from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('countryList', views.country),
    path('country/<str:EveryCountry>/', views.EveryCountry),
    path('lang', views.lang),
    path('lang/<str:EveryLang>/', views.EveryLang),
    path('countryList/<str:Bukva>/', views.EveryBukva),

]
