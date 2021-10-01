from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.


def landingpage(request):
    def get_ip(request):
        adress = request.META.get("HTTP_X_FORWARDED_FOR")
        if adress:
            ip = adress.split(",")[-1].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    ip = get_ip(request)
    u = User(user=ip)
    print(ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exist")
    elif len(result) > 1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")
    count = User.objects.all().count()
    print("total users is count", count)
    return render(request, "index.html", {"count": count})


def about(request):
    return render(request, "aboutus.html")


def error_404(request, exception):
    return render(request, "404.html")
