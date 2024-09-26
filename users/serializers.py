from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserPhoneSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "phone"
        ]
