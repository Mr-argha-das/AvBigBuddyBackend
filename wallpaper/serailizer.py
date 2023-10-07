from rest_framework import serializers
from .models import User
class UserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'gender', 'password')

class UserLoginSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email','password')