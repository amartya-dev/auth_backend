from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers


class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"})


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    name = serializers.CharField(max_length=255, required=True)

    def get_cleaned_data(self):
        return {
            "password1": self._validated_data.get("password1", ""),
            "email": self._validated_data.get("email", ""),
            "name": self._validated_data.get("name", ""),
        }

    def custom_signup(self, request, user):
        user.name = self.get_cleaned_data().get("name")
        user.save()
