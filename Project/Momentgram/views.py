from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    return render(request, 'Momentgram/register.html')

def signUp(request):
    username = request.POST.get('Name')
    email = request.POST.get('email')
    password = request.POST.get('psw')
    user = User.objects.create_user(username, email, password)
    return HttpResponse("Welcome" + email + "to Momentgram")