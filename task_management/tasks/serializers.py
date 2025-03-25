from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer
from users.models import User  # Import the User model


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

class AssignTaskSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ['assigned_users']
