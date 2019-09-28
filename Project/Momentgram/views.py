# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm



def index(request):
    #return render(request, 'Momentgram/register.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()
    return render(request, "Momentgram/register.html", {
        'form': form,
    })


def init(request):
    
    return render(request, 'Momentgram/init.html')