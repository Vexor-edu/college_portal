from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
    path('student-login/', views.student_login, name='student_login'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('contact/', views.contact, name='contact'),
    path('faculty/', views.faculty_page, name='faculty'),
    path('print/<int:pk>/', views.admin_print_application, name='admin_print_application'),
]
