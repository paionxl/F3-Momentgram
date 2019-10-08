from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate

from .forms import PostUploadForm
from .models import Post


def index(request):
    return render(request, 'Momentgram/register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username, email=email).exists():
            return HttpResponse("Username: " + username + " in use. Please try another one.")
        else:
            user = User.objects.create_user(username, email, password)
            return HttpResponse("Welcome to Momentgram, " + user.username)
    return render(request, 'Momentgram/register.html')

def signIn(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(username, password)
        if user:
            login(user)
        return user # user if good, None if bad

def upload_post(request):
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.get(pk='post_id')
            post.image = form.cleaned_data['image']
            post.description = form.cleaned_data['description']
            post.num_likes = form.cleaned_data['likes']
            post.user = form.cleaned_data['username']
            post.save()
            return HttpResponse('image upload success')
    return HttpResponse('allowed only via POST')



def init(request):
    return render(request, 'Momentgram/init.html')

