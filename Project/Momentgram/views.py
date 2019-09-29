from django.http import HttpResponse
import pyrebase
from django.shortcuts import render

config = {
    'apiKey': "AIzaSyCQRNHU0SMwMws_Zt5NZCR0q0XOTL5MY9M",
    'authDomain': "momentgram-7f5a3.firebaseapp.com",
    'databaseURL': "https://momentgram-7f5a3.firebaseio.com",
    'projectId': "momentgram-7f5a3",
    'storageBucket': "momentgram-7f5a3.appspot.com",
    'messagingSenderId': "903804373398",
    'appId': "1:903804373398:web:60bd1d367411d20d63f5b7"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def index(request):
    return render(request, 'Momentgram/register.html')

def signUp(request):
    email = request.POST.get('email')
    password = request.POST.get('psw')

    auth.create_user_with_email_and_password(email, password)
    return HttpResponse("Welcome" + email + "to Momentgram")