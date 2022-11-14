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


#funcion para el menu
def Menurestaurante(request):

        platosBD=Platos.objects.all()

        data={
            'entradas': list(filter(lambda x: x.tipo == 1, platosBD)),
            'platos': list(filter(lambda x: x.tipo == 2, platosBD)),
            'bebidas': list(filter(lambda x: x.tipo == 3, platosBD)),
            'postres': list(filter(lambda x: x.tipo == 4, platosBD)),
        }

        return render(request,'menuRestaurante.html',data)

# VISTA EMPLEADOS
def menuEmpleados(request):

        empleadosBD=Empleados.objects.all()

        data={
            'cheffs': list(filter(lambda x: x.cargo == 1, empleadosBD)),
            'administradores': list(filter(lambda x: x.cargo == 2, empleadosBD)),
            'meseros': list(filter(lambda x: x.cargo == 3, empleadosBD)),
            'ayudantes': list(filter(lambda x: x.cargo == 4, empleadosBD)),
        }

        return render(request,'menuEmpleados.html',data)

# VISTA PLATOS

def PlatosVista(request):

    #RUTINA PARA consultar platos

    platosConsultar =Platos.objects.all()
    print(platosConsultar)
    
    #esta vista va a utilizar un formulario de django, se cres un objeto de clase FormularioPlatos()
    formulario = FormularioPlatos()

    #creamos un diccionario para enviar el formulario al html

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


#VISTA EMPLEADOS 

def EmpleadosVista(request):

    #RUTINA PARA consultar empleados

    EmpleadosConsultar =Empleados.objects.all()
    print(EmpleadosConsultar)

    #esta vista va a utilizar un formulario de django, se cres un objeto de clase FormularioPlatos()
    formulario = FormularioEmpleados()

    #creamos un diccionario para enviar el formulario al html

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


