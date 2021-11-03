from django.contrib.auth import forms
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def sign_up(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =UserCreationForm()
    context = {
        'form': form
    }

    return render(request, 'members/sign_up.html', context)
