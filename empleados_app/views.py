from django.shortcuts import render,redirect
from .models import Empleados
# Create your views here.

def inicio_vistaEmpleados(request):
    losempleados = Empleados.objects.all()
    return render(request,"gestionarEmpleados.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombres = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    email = request.POST["txtemail"]
    sueldo = request.POST["numsueldo"]
    puesto = request.POST["txtpuesto"]
    direccion = request.POST["txtdireccion"]
    guardarempleado = Empleados.objects.create(id_empleado=id_empleado,nombres=nombres,apellidos=apellidos,email=email,sueldo=sueldo,puesto=puesto,direccion=direccion)
    return redirect("empleados")

def seleccionarEmpleado(request,id_empleado):
    empleado = Empleados.objects.get(id_empleado=id_empleado)
    return render(request,"editarEmpleado.html",{"misempleados":empleado})

def editarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombres = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    email = request.POST["txtemail"]
    sueldo = request.POST["numsueldo"]
    puesto = request.POST["txtpuesto"]
    direccion = request.POST["txtdireccion"]
    empleado = Empleados.objects.get(id_empleado=id_empleado)
    empleado.nombres = nombres
    empleado.apellidos = apellidos
    empleado.email = email
    empleado.sueldo = sueldo
    empleado.puesto = puesto
    empleado.direccion = direccion
    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request,id_empleado):
    empleado = Empleados.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleados")