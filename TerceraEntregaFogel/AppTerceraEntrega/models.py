from django.db import models

class Deportista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    altura = models.CharField(max_length=5)
    deporte = models.CharField(max_length=10)

    def __str__(self):
        return f"Nombre: {self.nombre} - Deporte: {self.deporte}"
        

class Futbol(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    posicion = models.CharField(max_length=10)
    contacto = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Posicion: {self.posicion}"

class Voley(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    altura = models.FloatField()
    contacto = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Altura: {self.altura}"

class Handball(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    altura = models.FloatField(max_length=30)
    contacto = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Altura: {self.altura}"

class Tenis(models.Model):
    nombre= models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mano_habil = models.CharField(max_length=30)
    contacto = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Mano Habil: {self.mano_habil}"
    
