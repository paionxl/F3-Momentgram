from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'Momentgram/register.html')

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        return HttpResponse("Welcome" + email + "to Momentgram")

def signIn(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(username, password)
        if user:
            login(user)
            return user # user if good, None if bad
        else:
            return None
