from django.shortcuts import render
from .models import Contact_US
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        contacted_message = Contact_US.objects.create(
            User_Name=name, Email=email, Subject=subject, Message=message
        )
        contacted_message.save()
        messages.success(request, "Thanks for Contacting US")

    return render(request, "contactus.html")
