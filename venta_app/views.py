from django.shortcuts import render,redirect
from .models import Venta
# Create your views here.

def inicio_vistaVenta(request):
    lasventas = Venta.objects.all()
    return render(request,"gestionarVentas.html",{"misventas":lasventas})

def registrarVenta(request):
    id_venta = request.POST["idventa"]
    id_cliente = request.POST["idcliente"]
    id_empleado = request.POST["idempleado"]
    fecha_venta = request.POST["txtfecha"]
    total = request.POST["numtotal"]
    impuesto = request.POST["numimpuesto"]
    producto_vendido = request.POST["txtproducto"]
    guardarventa = Venta.objects.create(id_venta=id_venta,id_cliente=id_cliente,id_empleado=id_empleado,fecha_venta=fecha_venta,total=total,impuesto=impuesto,producto_vendido=producto_vendido)
    return redirect("ventas")

def seleccionarVenta(request,id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    return render(request,"editarVenta.html",{"misventas":venta})

def editarVenta(request):
    id_venta = request.POST["idventa"]
    id_cliente = request.POST["idcliente"]
    id_empleado = request.POST["idempleado"]
    fecha_venta = request.POST["txtfecha"]
    total = request.POST["numtotal"]
    impuesto = request.POST["numimpuesto"]
    producto_vendido = request.POST["txtproducto"]
    venta = Venta.objects.get(id_venta=id_venta)
    venta.id_cliente = id_cliente
    venta.id_empleado = id_empleado
    venta.fecha_venta = fecha_venta
    venta.total = total
    venta.impuesto = impuesto
    venta.producto_vendido = producto_vendido
    venta.save()
    return redirect("ventas")

def borrarVenta(request,id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("ventas")