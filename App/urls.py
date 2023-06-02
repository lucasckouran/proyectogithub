from django.urls import path
from App import views
from .views import (
    canejo,
    pruebita,
    diaDeHoy,
    contexto,
)

urlpatterns = [
    path('cursos/', views.cursos, name="Cursos"),
    path('canejo', canejo),
    path('prueba2/', pruebita),
    path('dia/', diaDeHoy),
    path('template/', contexto)

]