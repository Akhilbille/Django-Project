from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from signup.models import Proffesional_detail
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method =='POST':
        username =request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username,password=password)
        print(user)
        # user1 =auth.authnticate(username=username,password=password)
        # user = auth.authenticate(phone_number=username, password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')


    return render(request, "login.html")

def forgotpassword(request):
    if request.method=='POST':
        username = request.POST['username']
        dob = request.POST['dateofbirth']
        new_pass=request.POST['new_password']
        dummy_pass=request.POST['dummy_pass']

        if User.objects.filter(username=username).exists():
            user_obj = User.objects.get(username=username)
            query_set = User.objects.get(id=user_obj.id)
            if new_pass == dummy_pass:
                pro_obj = Proffesional_detail.objects.get(phone_Number=username)

                if pro_obj.date_Of_Birth == dob:
                    print(query_set)
                    query_set.set_password(new_pass)
                    query_set.save()
                    messages.success(request, 'Successfully Updated')


                else:
                    messages.error(request, 'Please enter valid Date of Birth')




            else:
                messages.error(request, 'Password not matching')

        else:
                messages.error(request, 'Invalid Mobile Number')


    return render(request, "forgotpassword.html")



