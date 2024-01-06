from django.urls import path
from . import views
urlpatterns = [

    path('home/', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('update/', views.update, name= 'update'),
    path('details/', views.doctordetails, name='doctordetails'),
    path('patientdetails/', views.patientdetails, name='patientdetails'),
    path('allpatients/', views.allpatients, name='allpatients'),
    path('deletePatient/', views.deletePatient, name='deletePatient'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]