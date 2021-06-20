from django.contrib import admin
from django.urls import path, include
from desafio_tecnico_django.youngers.views import AllViewSet, YoungersViewSet, YoungersFilter, OldersViewSet, OldersFilter, ListaTipoSangue
from rest_framework import routers
from desafio_tecnico_django.youngers import views

router = routers.DefaultRouter()
router.register('all', AllViewSet, basename='all')
router.register('younger', YoungersViewSet, basename='younger')
router.register('older', OldersViewSet, basename='older')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(router.urls)),
	path('bloodtype/<str:pk>/', ListaTipoSangue.as_view()),
	path('youngers/<int:pk>/', YoungersFilter.as_view()),
	path('olders/<int:pk>/', OldersFilter.as_view())
]
