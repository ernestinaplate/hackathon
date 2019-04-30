from django.shortcuts import render
from .models import Freelancer, Profesion
from .forms import FreelancerForm
from django.contrib import messages
from django.http import HttpResponseRedirect

#from .forms import ImageForm, PostForm

# Create your views here.

def index(request):
    url_homepage = "index.html"
    return render(request, url_homepage)


def busq_categoria(request):
    
    #lista_resultados = ("Fotografo1","Fotografo2","Fotografo3")
    #resultados = {"lista_resultados": lista_resultados}
    
    ####### Prueba GET y objects.filter()
    lista_resultado = Freelancer.objects.filter(profesion=request.GET["c"])
    #######

    ####### Prueba objects.all()
    lista_freelancers = Freelancer.objects.all()
    #######
    
    contexto = {"lista": lista_resultado}
    
    return render(request, 'testBusqCategoria.html', contexto)

def crear_freelancer(request):
    parametros_form = request.GET
    nombre = parametros_form.get('nombre')
    apellido = parametros_form.get('apellido')
    foto_de_perfil = parametros_form.get('foto_de_perfil')
    profesion = parametros_form.get('profesion')
    email = parametros_form.get('email')
    domicilio = parametros_form.get('domicilio')
    telefono = parametros_form.get('telefono')
    exp_previa = parametros_form.get('exp_previa')
    descripcion = parametros_form.get('descripcion')
    fotoportfolio = parametros_form.get('fotoportfolio')
    created = parametros_form.get('created')

    profesion_nueva = Profesion.objects.get(id=profesion)
    freelancer_nuevo = Freelancer(nombre=nombre, apellido=apellido, 
                                foto_de_perfil=foto_de_perfil, profesion=profesion_nueva,
                                email=email, domicilio=domicilio, telefono=telefono,
                                exp_previa=exp_previa, descripcion=descripcion,
                                fotoportfolio=fotoportfolio, created=created)
    freelancer_nuevo.save()
    return("Se creo el perfil del Freelancer " + str(freelancer_nuevo.nombre) + ' ' + str(freelancer_nuevo.apellido))

