from django.shortcuts import render
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.formularios.formularioPlatos import FormularioPlatos
from web.models import Platos
from web.models import Empleados

# Create your views here.
# TODAS LAS VISTAS SON FUNCIONES DE PYTHON, se ponen en mayusculas, toda vista renderizas

#funcion que activa el html
def Home(request):
    return render (request, 'home.html')


def Menurestaurante(request):

    platosBD=Platos.objects.all()

    data={
        'platos':platosBD
    }

    return render(request,'menuRestaurante.html',data)

def PlatosVista(request):

    #RUTINA PARA consultar platos

    platosConsultar =Platos.objects.all()
    print(platosConsultar)
    
    #esta vista va a utilizar un formulario de django, se cres un objeto de clase FormularioPlatos()
    formulario = FormularioPlatos()

#cramos un diccionario para enviar el formulario al html

    data = {
    'formulario': formulario,
    'bandera': False,
    'platos':platosConsultar
}
#vista es el controlador, por aca RECIBIMOS LOS DATOS DEL FORMULARIO
    if request.method == 'POST':
        datosFormulario = FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data
            print(datosLimpios)

            #CONSTRUIR UN DICCIONARIO PARA ENVIAR DATOS HACIA LA BD
            platoNuevo = Platos(
                nombre = datosLimpios["nombre"],
                descripcion= datosLimpios["descripcion"],
                fotografia = datosLimpios["fotografia"],
                precio = datosLimpios["precio"],
                tipo= datosLimpios["tipo"]
            )

            #intentare llevar mis datos a la base de datos

            try :
                platoNuevo.save()
                data["bandera"] = True
                print("exito guardando")

            except Exception as error:
                print("uppss", error)
                data["bandera"] = False

    
    return render (request, 'menuplatos.html', data)


 #ahora para Empleados   

def EmpleadosVista(request):

    #RUTINA PARA consultar empleados

    EmpleadosConsultar =Empleados.objects.all()
    print(EmpleadosConsultar)

    #esta vista va a utilizar un formulario de django, se cres un objeto de clase FormularioPlatos()
    formulario = FormularioEmpleados()

#cramos un diccionario para enviar el formulario al html

    data = {
    'formulario': formulario,
    'bandera': False,
    'empleados':EmpleadosConsultar
}
    #vista es el controlador, por aca RECIBIMOS LOS DATOS DEL FORMULARIO
    if request.method == 'POST':
        datosFormulario = FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data
            print(datosLimpios)

            #CONSTRUIR UN DICCIONARIO PARA ENVIAR DATOS HACIA LA BD
            empleadoNuevo = Empleados(
                nombre = datosLimpios["nombre"],
                apellidos= datosLimpios["apellidos"],
                foto = datosLimpios["foto"],
                cargo = datosLimpios["cargo"],                
            )

            #intentare llevar mis datos a la base de datos
            try :
                empleadoNuevo.save()
                print("exito guardando")
                data["bandera"] = True

            except Exception as error:
                print("uppss", error)
                data["bandera"] = False
    return render (request, 'registrarEmpleados.html', data)


