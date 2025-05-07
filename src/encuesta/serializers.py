from rest_framework import serializers
from .models import Encuesta, Pregunta, Opcion, Respuesta

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ['id', 'texto', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)

    class Meta:
        model = Pregunta
        fields = ['id', 'texto', 'tipo', 'opciones', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class EncuestaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Encuesta
        fields = ['id', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'preguntas', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']