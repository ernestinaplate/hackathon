from django import forms
from .models import Profesion


class FreelancerForm(forms.Form):
    nombre = forms.CharField(label='Nombres', max_length=30)
    apellido = forms.CharField(label='Apellidos', max_length=50)
    foto_de_perfil = forms.FileField(label='Foto de perfil')
    profesion = forms.ModelChoiceField(queryset=Profesion.objects.all())
    email = forms.EmailField(label='E-mail')
    domicilio = forms.CharField(label='Domicilio', widget=forms.Textarea)
    telefono = forms.CharField(label='Telefono', max_length=15)
    exp_previa = forms.CharField(label='Experiencia previa', widget=forms.Textarea)
    descripcion = forms.CharField(label='Descripcion', widget=forms.Textarea)
    fotoportfolio = forms.FileField(label='Fotoportfolio')
