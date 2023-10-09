from .models import User
from .serailizer import (UserSerializers, UserLoginSerializers)
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.response import Response


class UserLsit(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers  # Individual object serializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Use UserSerializer to serialize a list
        serializer = UserSerializers(queryset, many=True)
        return Response(serializer.data)


class UserAdd(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def create(self, request, *args, **kwargs):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request, *args, **kwargs):

        email = request.data["email"]
        password = request.data["password"]
        queryset = User.objects.filter(email=email)
        x = len(queryset)
        userData = list(queryset.values())
        print(userData)
        if x != 0:

            if userData[0]["password"] == password:
                return Response({"message": "Login succes ", "data": userData[0], "status": True}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Login Password faild ", "data": None, "status": False}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "User could find", "data": None, "status": False}, status=status.HTTP_401_UNAUTHORIZED)

class UserData(APIView):
    def get(self, request, *args, **kwargs):
        id = request.GET.get("id")
        print(id)
        
        userdata = User.objects.filter(id=id)
        user = list(userdata.values())
        print(userdata)
        return Response({
            "message":"user data",
            "data": user,
            "status": True,
        }, status=status.HTTP_200_OK)
    