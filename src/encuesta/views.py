from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Encuesta, Pregunta, Opcion, Respuesta
from .serializers import EncuestaSerializer, PreguntaSerializer, OpcionSerializer, RespuestaSerializer

class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer
    permission_classes = [permissions.AllowAny]

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [permissions.AllowAny]

class OpcionViewSet(viewsets.ModelViewSet):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    permission_classes = [permissions.AllowAny]

class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [permissions.AllowAny]