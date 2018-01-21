from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v5/', views.api_root, name="api-root"),
    path('api/v5/users/', views.UserList.as_view(), name="user-list"),
    path('api/v5/users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('api/v5/readings/', views.ReadingList.as_view(), name="reading-list"),
    path('api/v5/readings/<int:pk>/',
         views.ReadingDetail.as_view(), name="reading-detail"),
    # Old API versions
    path('api/v4/readings/', views.ReadingList.as_view(), name="reading-list_v4"),
    path('api/v4/readings/<int:pk>/',
         views.ReadingDetailV4.as_view(), name="reading-detail_v4"),
    path('api/v3/readings/', views.ReadingListV3.as_view(), name="reading-list_v3"),
    path('api/v3/readings/<int:pk>/',
         views.ReadingDetailV3.as_view(), name="reading-detail_v3"),
    path('api/v2/readings/', views.reading_list_v2, name="reading-list_v2"),
    path('api/v2/readings/<int:pk>/',
         views.reading_detail_v2, name="reading-detail_v2"),
    path('api/v1/readings/', views.reading_list_v1, name="reading-list_v1"),
    path('api/v1/readings/<int:pk>/',
         views.reading_detail_v1, name="reading-detail_v1"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
