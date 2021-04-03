from rest_framework import serializers
from django.contrib.auth.models import User

from accounts.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    cpassword = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'cpassword']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        cpassword = self.validated_data['cpassword']

        if password != cpassword:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        account.set_password(password)
        account.save()

        return account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'username']
