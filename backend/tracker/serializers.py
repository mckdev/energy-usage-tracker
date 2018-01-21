from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Reading


class UserSerializer(serializers.ModelSerializer):
    readings = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Reading.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'readings')


class ReadingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Reading
        fields = ('id', 'user', 'date', 'value')
