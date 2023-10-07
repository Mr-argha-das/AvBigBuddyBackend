from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request=self.context.get('request'), email=email, password = password)
        if not user:
            raise serializers.ValidationError('Incorret crendentials please try again')
        data['user'] = user
        return data