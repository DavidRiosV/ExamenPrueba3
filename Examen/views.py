from django.shortcuts import render
from .models import Videojuego,Sede,Analisis,Plataforma,Estudio
from django.db.models import Q,Prefetch,Sum


def index(request):
    return render(request, 'Examen/index.html')

#------------------------------------------------------------------------------------------
#Videojuegos cuyo nombre contenga fantasy y su sede sea de Estados Unidos
def videojuego_fantasy(request,t,p):
    videojuegos=Videojuego.objects.filter(titulo__contains=t,estudio_desarrollo__sedes__pais__contains=p).select_related("estudio_desarrollo").prefetch_related("plataforma","analisis").all()

    return render(request,'Examen/videojuego_fantasy.html',{'videojuegos': videojuegos})

#------------------------------------------------------------------------------------------
#Videojuegos cuyo fabricante sea Sony o el nombre del fabricante sea Play Station y su nota de analisis sea mayor de 75
def videojuego_plataforma_analisis(request,f,n,p):
    videojuegos=Videojuego.objects.filter(Q(plataforma__fabricante=f)|Q(plataforma__nombre__contains=n),analisis__puntuacion__gt=p).select_related("estudio_desarrollo").prefetch_related("plataforma","analisis").distinct()[:3]

    return render(request,'Examen/videojuego_plataforma_analisis.html',{'videojuegos': videojuegos})

#------------------------------------------------------------------------------------------
#Videojuegos sin plataformas ordenados por ventas estimadas
def videojuego_sin_plataforma(request):
    videojuegos=Videojuego.objects.filter(plataforma=None).select_related("estudio_desarrollo").prefetch_related("plataforma","analisis").order_by('-ventas_estimadas').all()

    return render(request,'Examen/videojuego_sin_plataforma.html',{'videojuegos': videojuegos})

#------------------------------------------------------------------------------------------
#Estudios que tengan videojuegos que tienen un analisis de un año en concreto ordenados por su puntuacion 
def estudios(request,a):
    estudios=Estudio.objects.filter(videojuegos__analisis__fecha_publicacion__year=a).prefetch_related("videojuegos__analisis","sedes","videojuegos").order_by('-videojuegos__analisis__puntuacion').distinct()

    return render(request,'Examen/estudios.html',{'estudios': estudios})

#------------------------------------------------------------------------------------------
# Errores
def mi_error_404(request,exception=None):
    return render(request, 'Errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'errors/400.html', None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'errors/403.html', None,None,403)

def mi_error_500(request):
    return render(request, 'errors/500.html', None,None,500)