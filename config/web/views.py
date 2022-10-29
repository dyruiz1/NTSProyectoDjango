from django.shortcuts import render
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.formularios.formularioPlatos import FormularioPlatos

# Create your views here.
# TODAS LAS VISTAS SON FUNCIONES DE PYTHON, se ponen en mayusculas, toda vista renderizas

#funcion que activa el html
def Home(request):
    return render (request, 'home.html')

def Platos(request):
    
    #esta vista va a utilizar un formulario de django, se cres un objeto de clase FormularioPlatos()
    formulario = FormularioPlatos()

#cramos un diccionario para enviar el formulario al html

    data = {
    'formulario': formulario
}
    
    return render (request, 'menuplatos.html', data)

def Empleados(request):
    #esta vista va a utilizar un formulario de django, se cres un objeto de clase FormularioPlatos()
    formulario = FormularioEmpleados()

#cramos un diccionario para enviar el formulario al html

    data = {
    'formulario': formulario
}
    
    return render (request, 'registrarEmpleados.html', data)


