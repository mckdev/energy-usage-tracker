from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from . import views

schema_view = get_schema_view(title='Energy Usage Tracker')

router = DefaultRouter()
router.register(r'readings', views.ReadingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]
