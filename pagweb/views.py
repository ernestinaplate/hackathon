from django.shortcuts import render
from .models import Freelancer
from .models import Profesion

# Create your views here.

def index(request):
    url_homepage = "index.html"
    listado_prof = Profesion.objects.all()
    contexto = { "lista_profesiones":listado_prof }
    return render(request, url_homepage, contexto)


def busq_categoria(request):
    ####### Prueba GET y objects.filter()
    lista_resultado = Freelancer.objects.filter(profesion=request.GET["c"])

    ####### Prueba objects.all()
    #lista_freelancers = Freelancer.objects.all()
    
    contexto = {"lista": lista_resultado}
    return render(request, 'testCat.html', contexto)

