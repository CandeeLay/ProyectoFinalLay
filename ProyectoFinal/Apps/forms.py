from django import forms

class formAdoptar(forms.Form):
    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=10)
    edad = forms.IntegerField()
    email = forms.EmailField()
