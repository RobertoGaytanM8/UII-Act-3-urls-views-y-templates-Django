from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("jaulas/",views.jaulas,name="jaulas"),
    path("empleados/",views.empleados,name="empleado"),
    path("adoptantes/",views.adoptantes,name="adoptante"),
    path("perros/",views.perros,name="perros")

]

                              