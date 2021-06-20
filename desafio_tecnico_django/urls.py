from django.contrib import admin
from django.urls import path, include
from desafio_tecnico_django.youngers.views import YoungersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'youngers', YoungersViewSet, basename='youngers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
