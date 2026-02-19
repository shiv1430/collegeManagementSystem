from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # home page
    path('login/', views.login_page, name='login'),  # login page
    path('dashboard/', views.student_dashboard, name='student_dashboard'),  # student dashboard
    path('logout/', views.logout_user, name='logout'),
]
