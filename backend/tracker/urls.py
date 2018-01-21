from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v4/readings/', views.ReadingListV4.as_view(), name="reading_list_v4"),
    path('api/v4/readings/<int:pk>/', views.ReadingDetailV4.as_view(), name="reading_detail_v4"),
    path('api/v3/readings/', views.ReadingListV3.as_view(), name="reading_list_v3"),
    path('api/v3/readings/<int:pk>/', views.ReadingDetailV3.as_view(), name="reading_detail_v3"),
    path('api/v2/readings/', views.reading_list_v2, name="reading_list_v2"),
    path('api/v2/readings/<int:pk>/', views.reading_detail_v2, name="reading_detail_v2"),
    path('api/v1/readings/', views.reading_list_v1, name="reading_list_v1"),
    path('api/v1/readings/<int:pk>/',
         views.reading_detail_v1, name="reading_detail_v1"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
