from django.shortcuts import render

# Create your views here.
# TODAS LAS VISTAS SON FUNCIONES DE PYTHON, se ponen en mayusculas, toda vista renderizas

#funcion que activa el html
def Home(request):
    return render (request, 'home.html')
