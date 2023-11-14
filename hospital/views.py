from django.shortcuts import render
from .models import user
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method=='POST':
        name1=request.POST['username1']
        password=request.POST['password']
        print(name1,password)
        user1=user.objects.filter(username=name1,password=password)
        if user1:
            print("user found")
            return render(request,'user_info.html',{'user':name1})
        else:
            print("user not found")
            messages.error(request, 'User not found.')
            return render(request,'index.html')
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        address=request.POST['address1']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        email=request.POST['email']
        password=request.POST['password']
        user1=user(fname=fname,lname=lname,username=username,address=address,city=city,state=state,pincode=pincode,email=email,password=password)
        user1.save()
        print("user created")
        return render(request,'user_info.html')
    else:
        return render(request,'signup.html')