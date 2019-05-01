from django import forms
from .models import Profesion, Freelancer


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

class FreeForm2(forms.ModelForm):

    class Meta:
        model = Freelancer
        exclude = []
        #fields = ['nombre','apellido','email','foto_de_perfil', 'profesion']