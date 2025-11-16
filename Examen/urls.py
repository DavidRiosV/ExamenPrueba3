from django.urls import path,re_path
from.import views

urlpatterns = [
        path('',views.index,name='index'),
        path('videojuego/<str:t>/<str:p>/', views.videojuego_fantasy, name='videojuego_fantasy'),
        path('videojuego/<str:f>/<str:n>/<str:p>', views.videojuego_plataforma_analisis, name='videojuego_plataforma_analisis'),
        path('videojuego/plataforma', views.videojuego_sin_plataforma, name='videojuego_sin_plataforma'),
        path('estudios/<int:a>', views.estudios, name='estudios'),
        path('videojuego/<str:e>/<str:p>', views.videojuego_estudio, name='videojuego_estudio'),
        path('videojuego/analisis/<str:c>/<str:f>/<str:s>', views.analisis_critico, name='analisis_critico')
]