from django.shortcuts import render
from .models import Freelancer, Profesion
from .forms import FreelancerForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

#from .forms import ImageForm, PostForm

# Create your views here.

def index(request):
    url_homepage = "index2.html"
    listado_prof = Profesion.objects.all()
    contexto = { "lista_profesiones":listado_prof }
    return render(request, url_homepage, contexto)

# Devuelve lista de profesiones con: ID, Nombre, Cantidad de Freelancers
def obtener_profesiones():
    lista_profesiones = Profesion.objects.all()
    stats = []
    for prof in lista_profesiones:
        freelancers = Freelancer.objects.filter(profesion=prof)
        stats.append([prof.id, prof.nombre_profesion,len(freelancers)])
    return stats

def busqueda(request):
    lista_freelancers = []
    encabezado = []

    if "prof" in request.GET:
        lista_freelancers = Freelancer.objects.filter(profesion=request.GET["prof"])
        aux_profesion = Profesion.objects.filter(id=request.GET["prof"])
        encabezado.append("Profesion")
        encabezado.append(aux_profesion[0].nombre_profesion)
        encabezado.append(aux_profesion[0].imagen_grande)
    elif "busq" in request.GET:
        lista_freelancers = Freelancer.objects.filter(descripcion__icontains=request.GET["busq"])
        print("if busq")
        encabezado.append("Busqueda")
        encabezado.append(request.GET["busq"])
        encabezado.append("/media/portadadebusquedas.png")
    
    stats = obtener_profesiones()
    
    contexto = {
         "lista": lista_freelancers, 
         "encabezado":encabezado,
         "lista_profesiones": stats,
         }
    return render(request, 'listafree.html', contexto)

def desplegar_detalle(request):
    #llama a cada porfesional individualmente desplegando detalles
    individuo = Freelancer.objects.filter(id=request.GET["free"])
    contexto = {"individual":individuo}
    return render(request, 'test_detalle.html', contexto)

def crear_freelancer(request):
    if request.method == 'POST':
        parametros_form = request.POST
        print(parametros_form)
        nombre = parametros_form.get('nombre')
        print(nombre)
        apellido = parametros_form.get('apellido')
        foto_de_perfil = parametros_form.get('foto_de_perfil')
        profesion = parametros_form.get('profesion')
        email = parametros_form.get('email')
        domicilio = parametros_form.get('domicilio')
        telefono = parametros_form.get('telefono')
        exp_previa = parametros_form.get('exp_previa')
        descripcion = parametros_form.get('descripcion')
        fotoportfolio = parametros_form.get('fotoportfolio')
        #created = parametros_form.get('created')

        profesion_nueva = Profesion.objects.get(id=int(profesion))
        print(profesion_nueva)
        freelancer_nuevo = Freelancer(nombre=nombre, apellido=apellido, 
                                    foto_de_perfil=foto_de_perfil, profesion=profesion_nueva,
                                    email=email, domicilio=domicilio, telefono=telefono,
                                    exp_previa=exp_previa, descripcion=descripcion,
                                    fotoportfolio=fotoportfolio)
        print(freelancer_nuevo)
        freelancer_nuevo.save()
        return HttpResponse("Se creo el perfil del Freelancer " + str(freelancer_nuevo.nombre) + ' ' + str(freelancer_nuevo.apellido))
    
    else:
        form = FreelancerForm()

    return render(request, 'crearfreelancer.html', {"form":form})

def detalles(request):
    url_homepage = "detalles.html"
    individuo = Freelancer.objects.filter(id=request.GET["free"])
    contexto = {"individual": individuo}
    return render(request, url_homepage, contexto)