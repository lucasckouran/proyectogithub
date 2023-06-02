from django.urls import path
from App import views
from .views import (
    canejo,
    pruebita,
    diaDeHoy,
    contexto,
    index
)

urlpatterns = [
    path('cursos/', views.curso, name="Cursos"),
    path('canejo', canejo),
    path('prueba2/', pruebita),
    path('dia/', diaDeHoy),
    path('template/', contexto),
    path('index/',index)

]