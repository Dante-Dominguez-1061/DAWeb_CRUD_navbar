from django.urls import path
from videojuego_app import views

urlpatterns = [
    path("videojuego",views.inicio_vistaVideojuego,name="videojuego"),
    path("registrarVideojuego/",views.registrarVideojuego,name="registrarVideojuego"),
    path("seleccionarVideojuego/<id_videojuego>",views.seleccionarVideojuego,name="seleccionarVideojuego"),
    path("editarVideojuego/",views.editarVideojuego,name="editarVideojuego"),
    path("borrarVideojuego/<id_videojuego>",views.borrarVideojuego,name="borrarVideojuego")
]
