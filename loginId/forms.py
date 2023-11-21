
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# these two below are imported because of LoginForm.
from django import forms 
from django.forms.widgets import PasswordInput, TextInput

# Create/Register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Authenticate a user (Model Form)
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
