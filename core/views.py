from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from userprofile.models import UserProfile


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def plans(request):
    return render(request, 'core/plans.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')

def contact(request):
    return render(request, 'core/contact.html')

def user_manual(request):
    return render(request, 'core/user-manual.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:index')
        else:
            return render(request, "core/login.html", {
                "message": "Invalid email and/or password!"
            })
    return render(request, "core/login.html")
        

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:index'))

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, 'core/register.html', {
                "message": "Passwords must match!"
            })
        
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'core/register.html', {
                "message": "User already exists!"
            })
        login(request, user)

        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile(user=request.user)
            user_profile.save()

        return HttpResponseRedirect(reverse("core:index"))
    return render(request, 'core/register.html')

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('core:index')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'core/change_password.html', {
        "form": form
    })