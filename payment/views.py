from django.shortcuts import render,redirect
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from signup.models import Proffesional_detail
from django.contrib.auth.models import User

from .models import Payment





def payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        amount = 10000

        client = razorpay.Client(
            auth=("rzp_test_1eBcZWRELKoYV9", "BWmDJdSZMZq6K5EM7OV01R5H")
        )

        payment = client.order.create(
            {'name':name,"amount": amount, "currency": "INR", "payment_capture": "1","email":email}
        )
    return render(request, "payment.html")


@csrf_exempt
def success(request):
    if request.method == 'POST':
        QueryDict = request.POST
        name = QueryDict.__getitem__('name')
        phone = QueryDict.__getitem__('phone')
        payment_id = QueryDict.__getitem__('razorpay_payment_id')

        context={
            'phone':phone,


        }

        print(QueryDict)
        if payment_id != "":
            print('hii')

            user_payment = Payment.objects.create(name=name,phone=phone,payment_ID=payment_id)
            user_payment.save()
            print('I am IN')
            return render(request, "authdetails.html",context)

        else:
            return redirect('payment')

def authentication(request):
    if request.method == 'POST':

        phone = request.POST['phone']

        if (Payment.objects.filter(phone=phone).exists()):

            if(Proffesional_detail.objects.filter(phone_Number=phone).exists()):
                messages.info(request, "Account already exists, You can Login ")




            else:
                return redirect('signup')
        else:
            messages.info(request, "Payment not Finished. Please complete the Payment.")
    return render(request, 'authenticator.html')


