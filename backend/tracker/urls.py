from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v2/readings/', views.reading_list, name="reading_list"),
    path('api/v2/readings/<int:pk>/', views.reading_detail, name="reading_detail"),
    path('api/v1/readings/', views.reading_list_v1, name="reading_list_v1"),
    path('api/v1/readings/<int:pk>/',
         views.reading_detail_v1, name="reading_detail_v1"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
