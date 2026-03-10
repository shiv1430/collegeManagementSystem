from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # home page
    path('login/', views.login_page, name='login'),  # login page
    path('student/student_dashboard/', views.student_dashboard, name='student_dashboard'),  # student dashboard
    path('faculty/faculty_dashboard/',views.faculty_dashboard,name='faculty_dashboard'),
    path('hod/hod_dashboard/',views.hod_dashboard,name='hod_dashboard'),
    path('finance/finance_dashboard/', views.finance_dashboard, name='finance_dashboard'),
    path('logout/', views.logout_user, name='logout'),
]
