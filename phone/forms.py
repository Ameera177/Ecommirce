from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class meta:
        model=User
        fields=('username','email','password','password2')


class LoginUserForm(AuthenticationForm):
    class meta:
        model=User
        fields={'username','password'}
