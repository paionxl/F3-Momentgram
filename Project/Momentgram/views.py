# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import SignUpForm
def index(request):
    #return render(request, 'Momentgram/register.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)
            # login(request, user)
            
            #return redirect('init')
            return HttpResponseRedirect(reverse("init"))
    else:
        form = SignUpForm()

    return render(request, "Momentgram/register.html", {
        'form': form,
    })




def init(request):
    
    return render(request, 'Momentgram/init.html')

