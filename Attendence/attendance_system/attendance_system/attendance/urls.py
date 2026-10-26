from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'student/dashboard/',
        views.student_dashboard,
        name='student_dashboard'
    ),

    path(
        'student/register/',
        views.student_register,
        name='student_register'
    ),

    path(
        "register/",
        views.register_view,
        name="register"
    ),
]