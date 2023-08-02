from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class formAdoptar(forms.Form):
    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=10)
    contacto = forms.CharField(max_length=20)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=30)

class formAdopcion(forms.Form):
    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=10)
    contacto = forms.CharField(max_length=20)
    email = forms.EmailField()
    animal = forms.CharField(max_length=10)

class useredit(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "First name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Last name"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder": "Password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] #'password'
        help_texts = {k:"" for k in fields}

class changeform(PasswordChangeForm):
    old_password = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder": "Old password"}))
    new_password = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder": "New password"}))
    new_password2 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder": "Confirmation password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'new_password2'] 
        help_texts = {k:"" for k in fields}

