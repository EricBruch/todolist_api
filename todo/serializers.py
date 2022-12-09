from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',
                  'created_at', 'user', 'time_passed']
