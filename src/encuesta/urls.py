from rest_framework import routers
from .views import EncuestaViewSet, PreguntaViewSet, OpcionViewSet, RespuestaViewSet

router = routers.DefaultRouter()

router.register('api/encuestas', EncuestaViewSet, 'encuestas')
router.register('api/preguntas', PreguntaViewSet, 'preguntas')
router.register('api/opciones', OpcionViewSet, 'opciones')
router.register('api/respuesta', RespuestaViewSet, 'respuesta')

urlpatterns = router.urls