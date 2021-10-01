from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('style-register', views.style_register, name="style_register")
]