from django.shortcuts import render,redirect
from .models import Proveedores
# Create your views here.

def inicio_vistaProveedores(request):
    losproveedores = Proveedores.objects.all()
    return render(request,"gestionarProveedores.html",{"misproveedores":losproveedores})

def registrarProveedor(request):
    id_proveedor = request.POST["txtid"]
    nombre_empresa = request.POST["txtnombreempresa"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    email = request.POST["txtemail"]
    fecha_envio = request.POST["txtfecha"]
    guardarproveedor = Proveedores.objects.create(id_proveedor=id_proveedor,nombre_empresa=nombre_empresa,nombre=nombre,telefono=telefono,direccion=direccion,email=email,fecha_envio=fecha_envio)
    return redirect("proveedores")

def seleccionarProveedor(request,id_proveedor):
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request,"editarProveedor.html",{"misproveedores":proveedor})

def editarProveedor(request):
    id_proveedor = request.POST["txtid"]
    nombre_empresa = request.POST["txtnombreempresa"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    email = request.POST["txtemail"]
    fecha_envio = request.POST["txtfecha"]
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre_empresa = nombre_empresa
    proveedor.nombre = nombre
    proveedor.telefono = telefono
    proveedor.direccion = direccion
    proveedor.email = email
    proveedor.fecha_envio = fecha_envio
    proveedor.save()
    return redirect("proveedores")

def borrarProveedor(request,id_proveedor):
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect("proveedores")