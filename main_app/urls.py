from django.urls import path
from atelier.forms import *
from  .views import *

urlpatterns=[
    path('',index ,name='index'),
    path('home/',home_page , name='home'),
    path('my_form/',send_forms_for_email , name='my_form')
]