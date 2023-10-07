from django.contrib.auth import (login, logout)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .userloginserializer import UserLoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({'message':'Login successful'})
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)