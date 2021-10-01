from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import auth

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        side_bar_set = side_bar.objects.all()

        return render(request, "home.html", {"side_bars": list(side_bar_set)})
    else:
        return redirect("login")


def farmer(request):
    if request.user.is_authenticated:
        farmer_info = Farmer.objects.all()
        side_bar_set = side_bar.objects.all()
        return render(
            request,
            "farmer.html",
            {"farmer_info": list(farmer_info), "side_bars": list(side_bar_set)},
        )
    else:
        return redirect("login")


def covid_plasma(request):
    if request.user.is_authenticated:
        covid_plasma = Convid_Plasma.objects.all()
        side_bar_set = side_bar.objects.all()

        return render(
            request,
            "covid-plasma.html",
            {"covid_plasma": list(covid_plasma), "side_bars": list(side_bar_set)},
        )
    else:
        return redirect("login")


def employement(request):
    if request.user.is_authenticated:
        employement = Employement.objects.all()
        side_bar_set = side_bar.objects.all()
        return render(
            request,
            "employement.html",
            {"employement": list(employement), "side_bars": list(side_bar_set)},
        )

    else:
        return redirect("login")


def blood_donors(request):
    if request.user.is_authenticated:
        blood_donors = Blood_Donor.objects.all()
        side_bar_set = side_bar.objects.all()
        return render(
            request,
            "blood-donors.html",
            {"blood_donors": list(blood_donors), "side_bars": list(side_bar_set)},
        )

    else:
        return redirect("login")


def school_admission(request):
    if request.user.is_authenticated:
        school_admission = School.objects.all()
        side_bar_set = side_bar.objects.all()
        return render(
            request,
            "school-Admission.html",
            {
                "school_admission": list(school_admission),
                "side_bars": list(side_bar_set),
            },
        )

    else:
        return redirect("login")


def apcs_rules(request):
    if request.user.is_authenticated:
        apcs_rules = APCS_Rules.objects.all()
        side_bar_set = side_bar.objects.all()
        return render(
            request,
            "apcs-rules.html",
            {"apcs_rules": list(apcs_rules), "side_bars": list(side_bar_set)},
        )

    else:
        return redirect("login")


def apcs_conduct_rules(request):
    if request.user.is_authenticated:
        apcs_conduct_rules = APCS_Conduct_Rules.objects.all()
        side_bar_set = side_bar.objects.all()
        return render(
            request,
            "apcs-conduct-rules.html",
            {
                "apcs_conduct_rules": list(apcs_conduct_rules),
                "side_bars": list(side_bar_set),
            },
        )

    else:
        return redirect("login")


def ap_govt_employees(request):
    if request.user.is_authenticated:
        folder_set = Folder.objects.all()
        side_bar_set = side_bar.objects.all()
        return render(
            request,
            "apgovtemployee.html",
            {"folders": list(folder_set), "side_bars": list(side_bar_set)},
        )

    else:
        return redirect("login")


def apcs_leave_rules(request):
    if request.user.is_authenticated:
        apcs_leave_rules = APCS_Leave_Rules.objects.all()
        side_bar_set = side_bar.objects.all()
        return render(
            request,
            "apcs-leave-rules.html",
            {
                "apcs_leave_rules": list(apcs_leave_rules),
                "side_bars": list(side_bar_set),
            },
        )

    else:
        return redirect("login")


def logout(request):
    if request.user.is_authenticated:

        auth.logout(request)
        return redirect("/")
    else:
        return redirect("login")
