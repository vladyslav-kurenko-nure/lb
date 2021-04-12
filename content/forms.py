from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from .models import *


class AddLinkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Link
        fields = ['title', 'slug', 'content', 'cat']
        widgets = {
            'title': forms.TextInput(),
            'content': forms.URLInput(),
            'slug': forms.TextInput(),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password1')
