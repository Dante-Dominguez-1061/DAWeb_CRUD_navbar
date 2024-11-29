from django.urls import path
from consola_app import views

urlpatterns = [
    path("consola",views.inicio_vistaConsola,name="consola"),
    path("registrarConsola/",views.registrarConsola,name="registrarConsola"),
    path("seleccionarConsola/<id_consola>",views.seleccionarConsola,name="seleccionarConsola"),
    path("editarConsola/",views.editarConsola,name="editarConsola"),
    path("borrarConsola/<id_consola>",views.borrarConsola,name="borrarConsola")
]