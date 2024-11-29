from django.shortcuts import render,redirect
from .models import Clientes
# Create your views here.

def inicio_vistaClientes(request):
    losclientes = Clientes.objects.all()
    return render(request,"gestionarClientes.html",{"misclientes":losclientes})

def registrarCliente(request):
    id_cliente = request.POST["txtid"]
    nombres = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    foto = request.POST["blobfoto"]
    guardarcliente = Clientes.objects.create(id_cliente=id_cliente,nombres=nombres,apellidos=apellidos,direccion=direccion,telefono=telefono,email=email,foto=foto)
    return redirect("clientes")

def seleccionarCliente(request,id_cliente):
    cliente = Clientes.objects.get(id_cliente=id_cliente)
    return render(request,"editarCliente.html",{"misclientes":cliente})

def editarCliente(request):
    id_cliente = request.POST["txtid"]
    nombres = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    foto = request.POST["blobfoto"]
    cliente = Clientes.objects.get(id_cliente=id_cliente)
    cliente.nombres = nombres
    cliente.apellidos = apellidos
    cliente.direccion = direccion
    cliente.telefono = telefono
    cliente.email = email
    cliente.foto = foto
    cliente.save()
    return redirect("clientes")

def borrarCliente(request,id_cliente):
    cliente = Clientes.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes")