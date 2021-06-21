from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from desafio_tecnico_django.youngers import views

router = routers.DefaultRouter()
router.register('all', views.AllViewSet, basename='all')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(router.urls)),
	path('youngers/', views.Youngers.as_view()),
	path('youngers/<int:pk>/', views.YoungersFilter.as_view()),
	path('olders/', views.Olders.as_view()),
	path('olders/<int:pk>/', views.OldersFilter.as_view()),
	path('peoples/', views.Peoples.as_view()),
	path('peoples/search/<str:pk>/', views.PeoplesSearch.as_view()),
	path('peoples/<str:pk>/', views.ListByCpf.as_view()),
	path('blood-type/stats/', views.Blood.as_view()),
	path('blood-type/stats/<str:pk>/', views.ListByBloodType.as_view()),
	path('gender-distribution/', views.Gender.as_view())
]
