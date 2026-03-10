from django.shortcuts import render

def index(request):
    return render(request, "Home/index.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student/student_dashboard')
        else:
            return render(request, 'Home/login.html', {'error': 'Invalid credentials'})

    return render(request, 'Home/login.html')


def student_dashboard(request):
    return render(request, 'student/student_dashboard.html')

def faculty_dashboard(request):
    return render(request,'faculty/faculty_dashboard.html')

def hod_dashboard(request):
    return render(request,'hod/hod_dashboard.html')

def finance_dashboard(request):
    return render(request, 'finance/finance_dashboard.html')


def logout_user(request):
    logout(request)
    return redirect('Home/login')

