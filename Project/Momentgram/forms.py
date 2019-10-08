from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    name = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'name')


class PostUploadForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('username','description')
