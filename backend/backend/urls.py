from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/', include('tracker.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name="home.html")),
]
