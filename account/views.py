from django.shortcuts import render,redirect
from .forms import ContributorCreationForm
from .models import Contributor
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm

# Create your views here.
def signup(response):
    if response.method == "POST":
        form = ContributorCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = ContributorCreationForm()
    return render(response,"registration/signup.html",{"form":form})



