
from django.urls import path
from .views import *

urlpatterns = [
    path('payment', payment, name='payment'),
     path('payment/success' , success , name='success'),
     path('authentication' , authentication , name='authenticator')

]
