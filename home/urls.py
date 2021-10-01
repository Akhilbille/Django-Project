from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("home/farmer/", views.farmer, name="farmer"),
    path("home/employement/", views.employement, name="employement"),
    path("home/blood-donors/", views.blood_donors, name="blood"),
    path("home/covid-plasma/", views.covid_plasma, name="farmer"),
    path("home/school/", views.school_admission, name="school"),
    path("home/apcs-rules/", views.apcs_rules, name="apcs-rules"),
    path(
        "home/apcs-conduct-rules/", views.apcs_conduct_rules, name="apcs-conduct-rules"
    ),
    path("home/apcs-leave-rules/", views.apcs_leave_rules, name="apcs-leave-rules"),
    path("home/ap-govt-employees/", views.ap_govt_employees, name="apcs-leave-rules"),
    path("home/logout", views.logout, name="logout"),
]
