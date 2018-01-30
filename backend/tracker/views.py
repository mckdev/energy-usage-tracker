from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from .models import Reading
from .permissions import IsOwnerOrReadOnly
from .serializers import ReadingSerializer, UserSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
