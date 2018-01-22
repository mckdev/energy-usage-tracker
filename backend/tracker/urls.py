from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = DefaultRouter()
router.register(r'readings', views.ReadingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('v6/', include(router.urls)),
    # Old API versions
    path('v5/', views.api_root, name="api-root"),
    path('v5/users/', views.UserList.as_view(), name="user-list"),
    path('v5/users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('v5/readings/', views.ReadingList.as_view(), name="reading-list"),
    path('v5/readings/<int:pk>/',
         views.ReadingDetail.as_view(), name="reading-detail"),
    path('v4/readings/', views.ReadingList.as_view(), name="reading-list_v4"),
    path('v4/readings/<int:pk>/',
         views.ReadingDetailV4.as_view(), name="reading-detail_v4"),
    path('v3/readings/', views.ReadingListV3.as_view(), name="reading-list_v3"),
    path('v3/readings/<int:pk>/',
         views.ReadingDetailV3.as_view(), name="reading-detail_v3"),
    path('v2/readings/', views.reading_list_v2, name="reading-list_v2"),
    path('v2/readings/<int:pk>/',
         views.reading_detail_v2, name="reading-detail_v2"),
    path('v1/readings/', views.reading_list_v1, name="reading-list_v1"),
    path('v1/readings/<int:pk>/',
         views.reading_detail_v1, name="reading-detail_v1"),
]

# This breaks router urls, but is useful for older API versions
# urlpatterns = format_suffix_patterns(urlpatterns)
