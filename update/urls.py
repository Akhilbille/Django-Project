from django.urls import path
from . import views

urlpatterns = [
    path('home/profile-update', views.update, name="update"),

]