from django.urls import path,re_path
from.import views

urlpatterns = [
        path('',views.index,name='index'),
        path('videojuego/<str:t>/<str:p>/', views.videojuego_fantasy, name='videojuego_fantasy'),
         path('videojuego/<str:f>/<str:n>/<str:p>', views.videojuego_plataforma_analisis, name='videojuego_plataforma_analisis'),
]