from rest_framework import serializers

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    # type = serializers.IntegerField()

    class Meta:
        model = User
        # fields = '__all__'
        # fields = ['id', 'first_name']
        exclude = ['groups', 'password', 'user_permissions', 'is_active',
                   'is_superuser', 'is_staff']
        # exclude = []
