from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")  # default login view
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")  # redirect to login if not authenticated
    return render(request, "registration/profile.html", {"user": request.user})