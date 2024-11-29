from django.shortcuts import render,redirect
from .models import Videojuego
# Create your views here.
def inicio_vistaVideojuego(request):
    losvideojuegos = Videojuego.objects.all()
    return render(request,"gestionarVideojuegos.html",{"misvideojuegos":losvideojuegos})

def registrarVideojuego(request):
    id_videojuego = request.POST["txtid"]
    titulo = request.POST["txttitulo"]
    genero = request.POST["txtgenero"]
    compañia = request.POST["txtcompañia"]
    precio = request.POST["numprecio"]
    fecha_lanzamiento = request.POST["txtfecha"]
    stock = request.POST["numstock"]
    guardarvideojuego = Videojuego.objects.create(id_videojuego=id_videojuego,titulo=titulo,genero=genero,compañia=compañia,precio=precio,fecha_lanzamiento=fecha_lanzamiento,stock=stock)
    return redirect("videojuego")

def seleccionarVideojuego(request,id_videojuego):
    videojuego = Videojuego.objects.get(id_videojuego=id_videojuego)
    return render(request,"editarVideojuegos.html",{"misvideojuegos":videojuego})

def editarVideojuego(request):
    id_videojuego = request.POST["txtid"]
    titulo = request.POST["txttitulo"]
    genero = request.POST["txtgenero"]
    compañia = request.POST["txtcompañia"]
    precio = request.POST["numprecio"]
    fecha_lanzamiento = request.POST["txtfecha"]
    stock = request.POST["numstock"]
    videojuego = Videojuego.objects.get(id_videojuego=id_videojuego)
    videojuego.titulo = titulo
    videojuego.genero = genero
    videojuego.compañia = compañia
    videojuego.precio = precio
    videojuego.fecha_lanzamiento = fecha_lanzamiento
    videojuego.stock = stock
    videojuego.save()
    return redirect("videojuego")

def borrarVideojuego(request,id_videojuego):
    consola = Videojuego.objects.get(id_videojuego=id_videojuego)
    consola.delete()
    return redirect("videojuego")