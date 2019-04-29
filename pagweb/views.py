from django.shortcuts import render

# Create your views here.

def index(request):
    url_homepage = "index.html"
    return render(request, url_homepage)


def busq_categoria(request):
    #lista_resultados = ("Fotografo1","Fotografo2","Fotografo3")
    #resultados = {"lista_resultados": lista_resultados}
    
    #lista_resultado = Freelancer.objects.filter(categoria=request.GET[categoria])
    
    lista_freelancers = Freelancer.objects.all()
    contexto = {"lista_t": lista_freelancers}
    
    return render(request, 'testBusqCategoria.html', resultados)

