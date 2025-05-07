
from django.db import models
from django.contrib.auth.models import User  # opcional si usas autenticación

class Encuesta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.nombre

class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, related_name='preguntas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    TIPO_CHOICES = [
        ('texto', 'Texto Abierto'),
        ('opcion_unica', 'Opción Única'),
        ('multiple', 'Selección Múltiple'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='opcion_unica')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def _str_(self):
        return self.texto

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def _str_(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas', on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, null=True, blank=True, on_delete=models.SET_NULL)
    respuesta_texto = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def _str_(self):
        return f"Respuesta de {self.usuario or 'Anónimo'} a {self.pregunta}"