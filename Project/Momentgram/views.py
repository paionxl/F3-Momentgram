from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Momentgram.models import Profile, Post, Follow
from datetime import datetime, timedelta
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404




def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("publish"))
    return render(request, 'Momentgram/init.html')

@login_required
def entry(request):
    return render(request, 'Momentgram/entry.html')

@login_required
def view_post(request):
    return render(request, 'Momentgram/post_visualitzation.html')


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists() or User.objects.filter(email = email).exists():
            return HttpResponse("Username: " + username + " or mail: " + email +  " in use. Please try another one.")
        else:
            user = User.objects.create_user(username, email, password)
            return HttpResponseRedirect(reverse("login"))

    if request.method == 'GET':
        if request.user.is_authenticated:
            #return HttpResponse("You are already registered and logged in using: "+ request.user.username)
            # if init page is done, send him there
            return HttpResponseRedirect(reverse("publish"))
        return render(request, 'Momentgram/register.html')

def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password = password)
        if user:
            login(request, user = user)
            if 'next' in request.session:
                next = request.session['next']
                request.session['next'] = None
                return redirect(next)
            return HttpResponseRedirect(reverse("publish"))
        else:
            return HttpResponse("Failed. Username or password not correct")

    if request.method == 'GET':
        if request.user.is_authenticated:
            # return HttpResponse("You are already logged in using: " + request.user.username)
            return HttpResponseRedirect(reverse("publish"))
            # if init page is done, send him there
        if request.GET.get('next',''):
            request.session['next'] = request.GET.get('next', '/')
        return render(request, 'Momentgram/login.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def publish_post(request):
    if request.method == 'POST':
        date = datetime.now()
        image_name = request.FILES['image'].name
        image = request.FILES['image']
        description = request.POST.get('description')
        post = Post()
        post.description = description
        post.image = image
        post.user = request.user
        post.date = date
        post.save()
        context ={
            'username' : post.user.username,
            'description' : post.description,
            'image_name' : image_name,
            'date' : date
        }
        return render(request, 'Momentgram/post_visualitzation.html', context)
    if request.method == 'GET':
        return render(request, 'Momentgram/post.html')

@login_required
def show_profile(request, username):
    user = User.objects.filter(username=username)[0]
    yourProfile = False
    followed = False
    if user.username == request.user.username:
        yourProfile = True
    else:
        if(request.user in Profile.objects.filter(user=user)[0]).get_followers()):
            followed = True
    context{
        'followed' : followed,
        'yourProfile' : yourProfile,
        'username' : user.username,
        'n_posts' : #getPosts,
        'n_followed' : (Profile.objects.filter(user=user)[0]).get_following().count(),
        'n_followers' : (Profile.objects.filter(user=user)[0]).get_followers().count(),
        'description' : (Profile.objects.filter(user=user)[0]).bio,
        'fullName' : user.first_name + " " + user.last_name
    }
    return render(request, 'Momentgram/profile.html', context)


@login_required
def manage_friend(request, username):
    user = User.objects.filter(username=username)[0]
    followed = False
    if(request.user in Profile.objects.filter(user=user)[0]).get_followers()):
        followed = True

    if(followed == True):
        Follow.objects.filter(follower.username=request.user, following.username=following)[0].delete()
        context ={
            'followed' : followed,
            'yourProfile' : False,
            'username' : user.username,
            'n_posts' : #getPosts,
            'n_followed' : (Profile.objects.filter(user=user)[0]).get_following().count(),
            'n_followers' : (Profile.objects.filter(user=user)[0]).get_followers().count(),
            'description' : (Profile.objects.filter(user=user)[0]).bio,
            'fullName' : user.first_name + " " + user.last_name,
        }
    else:
        #crearFollow
        context ={
            'followed' : followed,
            'yourProfile' : True,
            'username' : user.username,
            'n_posts' : #getPosts,
            'n_followed' : (Profile.objects.filter(user=user)[0]).get_following().count(),
            'n_followers' : (Profile.objects.filter(user=user)[0]).get_followers().count(),
            'description' : (Profile.objects.filter(user=user)[0]).bio,
            'fullName' : user.first_name + " " + user.last_name,
        }


    return reverse('profile', context)




