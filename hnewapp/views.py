from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect


# Create your views here.
def about(request):
    return render(request,'about.html')


def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')


def login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username =u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error ="No"

            else:
                error ="Yes"

        except:
            error = "yes"
    d = {'error': error}
    return render(request,'login.html',d)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('login')