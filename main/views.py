from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.


def login_reg(request):
    return render(request, 'login_reg.html')


def create_user(request):
    errors = User.objects.user_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')

    # Needs BCrypt functionality and user in session

    user1 = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=request.POST['password'],
    )

    return redirect('/dashboard')


def login_user(request):
    # Need to be finished
    return redirect('/dashboard')


def dashboard(request):
    return render(request, 'dashboard.html')
