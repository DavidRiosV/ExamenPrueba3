from django.db import models

# Create your models here.

#------------------------------- Estudio ------------------------------------------  
class Estudio(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre}"
    
#------------------------------- Sede ------------------------------------------  
class Sede(models.Model):
    nombre = models.CharField(max_length=10)
    pais = models.CharField(max_length=10)

    estudio=models.ForeignKey(Estudio,on_delete=models.CASCADE,related_name='sedes')

    def __str__(self):
        return f"{self.nombre}"
    
#------------------------------- Plataforma ------------------------------------------  
class Plataforma(models.Model):
    nombre = models.CharField(max_length=10)
    fabricante=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre}"

#------------------------------- Videojuego ------------------------------------------  
class Videojuego(models.Model):
    nombre = models.CharField(max_length=10)
    titulo = models.CharField(max_length=10)
    ventas_estimadas=models.FloatField(max_length=10)

    estudio_desarrollo=models.ForeignKey(Estudio,on_delete=models.CASCADE,related_name='videojuegos')
    plataforma=models.ManyToManyField(Plataforma,blank=True,related_name='videojuegos')

    def __str__(self):
        return f"{self.nombre}"

#------------------------------- Analisis ------------------------------------------
class Analisis(models.Model):
    nombre = models.CharField(max_length=10)
    puntuacion=models.FloatField(max_length=3)
    critico=models.CharField(max_length=10)
    fecha_publicacion=models.DateField(auto_now=True)

    videojuego=models.ForeignKey(Videojuego,on_delete=models.CASCADE,related_name='analisis')

    def __str__(self):
        return f"{self.nombre}"