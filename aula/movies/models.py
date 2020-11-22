from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone



class Alumno(models.Model):
    Codigo = models.CharField(max_length=200,null=True,blank=True, unique =True)
    Nombre =  models.CharField(max_length=200,blank=True, null=True)
    Apellido = models.CharField(max_length=200,blank=True, null=True)
    Email = models.CharField(max_length=200,blank=True, null=True)
    Grado = models.CharField(max_length=200,blank=True, null=True)
    Seccion = models.CharField(max_length=200,blank=True, null=True)
    Genero = models.CharField(max_length=200,blank=True, null=True)
    nacimiento = models.CharField(max_length=200,blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    fechaingreso = models.DateTimeField(
        blank=True, null=True)
    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s %s %s' % (self.Codigo,self.Nombre, self.Apellido, self.Grado)

    class Meta:
            ordering = ('Apellido',)

class Materia(models.Model):
    Nombre_Materia  =   models.CharField(max_length=130)
    Fecha_Ingreso = models.DateTimeField(default=timezone.now,blank=True, null=True)
	
    def publish(self):
    	self.Fecha_Ingreso = timezone.now()
    	self.save()

    def __str__(self):
        return '%s' % (self.Nombre_Materia)
        
    class Meta:
        ordering = ('Nombre_Materia',)


class Asignacion_Materia (models.Model):

    Nota_Final  = models.CharField(max_length=200,null=True,blank=True, unique =True)

    Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    Alumno  = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    
    def __str__(self):
        return '%s %s %s' % (self.Materia, self.Alumno, self.Nota_Final)