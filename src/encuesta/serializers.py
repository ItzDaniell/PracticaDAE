from rest_framework import serializers
from .models import Encuesta, Pregunta, Opcion, Respuesta

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ['id', 'texto', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

