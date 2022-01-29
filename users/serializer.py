from rest_framework import serializers, exceptions

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")

        if User.objects.filter(username=username).exists():
            raise exceptions.ValidationError("given username exists")
        elif len(password) < 4:
            raise exceptions.ValidationError("given password too short")

        user = User.objects.create_user(username=username, password=password)
        return user
