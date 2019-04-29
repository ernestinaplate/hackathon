from django.shortcuts import render

# Create your views here.

def busq_categoria(request):
    lista_resultados = ("Fotografo1","Fotografo2","Fotografo3")
    resultados = {"lista_resultados": lista_resultados}
    #lista_resultado = Freelancer.objects.filter(categoria=request.GET[categoria])
    return render(request, 'testBusqCategoria.html', resultados)