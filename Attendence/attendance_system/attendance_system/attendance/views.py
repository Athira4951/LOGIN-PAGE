from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from .models import Student
from .forms import StudentForm


def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # Check whether the logged-in user is a student
            if Student.objects.filter(user=user).exists():
                return redirect('student_dashboard')

            # Otherwise, treat as teacher
            return redirect('dashboard')

        else:
            return render(
                request,
                'attendance/login.html',
                {'error': 'Invalid username or password'}
            )

    return render(
        request,
        'attendance/login.html'
    )


def dashboard(request):

    total_students = Student.objects.count()

    context = {
        'total_students': total_students,
        'present': 0,
        'absent': 0,
        'attendance_percentage': 0,
    }

    return render(
        request,
        'attendance/dashboard.html',
        context
    )


def student_register(request):

    if request.method == "POST":

        user_form = UserCreationForm(request.POST)

        student_form = StudentForm(
            request.POST,
            request.FILES
        )

        if user_form.is_valid() and student_form.is_valid():

            # Create login account
            user = user_form.save()

            # Create student details
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            return redirect('login')

    else:
        user_form = UserCreationForm()
        student_form = StudentForm()

    return render(
        request,
        'attendance/student_register.html',
        {
            'user_form': user_form,
            'student_form': student_form
        }
    )

def register_view(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "attendance/register.html",
        {"form": form}
    )


def student_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return redirect('dashboard')

    context = {
        'student': student,
    }

    return render(
        request,
        'attendance/student_dashboard.html',
        context
    )