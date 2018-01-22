from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Reading


class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Reading
        fields = ('url', 'id', 'user', 'date', 'value')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    readings = serializers.HyperlinkedRelatedField(
        many=True, view_name='reading-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'readings')
