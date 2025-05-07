from rest_framework import serializers
from .models import Encuesta, Pregunta, Opcion, Respuesta

class OpcionSerializer(serializers.ModelSerializer):
    pregunta = serializers.PrimaryKeyRelatedField(queryset=Pregunta.objects.all())
    respuesta = serializers.PrimaryKeyRelatedField(queryset=Respuesta.objects.all(), allow_null=True)  # Permitir que la respuesta sea nula
    class Meta:
        model = Opcion
        fields = ['id', 'texto', 'pregunta', 'respuesta', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)
    encuesta = serializers.PrimaryKeyRelatedField(queryset=Encuesta.objects.all()) 

    class Meta:
        model = Pregunta
        fields = ['id', 'texto', 'tipo', 'encuesta', 'opciones', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class EncuestaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Encuesta
        fields = ['id', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado', 'preguntas', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class RespuestaSerializer(serializers.ModelSerializer):
    pregunta = serializers.PrimaryKeyRelatedField(queryset=Pregunta.objects.all())
    opcion = serializers.PrimaryKeyRelatedField(queryset=Opcion.objects.all(), allow_null=True)  # Permitir que la opción sea nula
    class Meta:
        model = Respuesta
        fields = ['id', 'pregunta', 'opcion', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
