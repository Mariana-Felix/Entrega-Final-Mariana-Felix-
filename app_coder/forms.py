from django import forms
from django.forms import ModelForm
from app_coder.models import Avatar,Articles
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArticlesForm(forms.Form):
    title = forms.CharField(max_length=40, min_length=3, label='Title')
    sub_title = forms.CharField(max_length=40, min_length=3, label='Subtitle')
    text = forms.TextInput()

    class Meta:
        model = Articles
        fields = ('title','sub_title','text','image')

class CommentsForm(forms.Form):
    data = forms.TextInput()
    


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='username', min_length=3)
    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )