from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'churches', views.ChurchViewSet)
router.register(r'people', views.PersonViewSet)
