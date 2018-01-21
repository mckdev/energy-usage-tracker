from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('api/v1/readings/', views.reading_list, name="reading_list"),
    path('api/v1/readings/<int:pk>/', views.reading_detail, name="reading_detail"),
]
