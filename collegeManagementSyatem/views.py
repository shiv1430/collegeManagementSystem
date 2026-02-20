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

            if user.role == 'Student':
                return redirect('student_dashboard')

            elif user.role == 'Faculty':
                return redirect('faculty_dashboard')

            elif user.role == 'HOD':
                return redirect('hod_dashboard')
            
            elif user.role == 'Financial Office':
                return redirect('accountant_dashboard')
            
            elif user.role == 'Registrar Office':
                return redirect('registrar_dashboard')

        else:
            return render(request, 'Home/login.html', {'error': 'Invalid credentials'})

    return render(request, 'Home/login.html')


def student_dashboard(request):
    return render(request, 'student/student_dashboard.html')

def faculty_dashboard(request):
    return render(request, 'faculty/faculty_dashboard.html')

def hod_dashboard(request):
    return render(request, 'hod/hod_dashboard.html')

def accountant_dashboard(request):
    return render(request, 'accountant/accountant_dashboard.html')

def registrar_dashboard(request):
    return render(request, 'registrar/registrar_dashboard.html')



def logout_user(request):
    logout(request)
    return redirect('Home/login')


