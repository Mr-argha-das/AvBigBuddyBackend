from .models import User
from .serailizer import UserSerializers
from rest_framework import status
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
        serializer = UserSerializers(queryset, many=True)  # Use UserSerializer to serialize a list
        return Response(serializer.data)


class UserAdd(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    def create(self, request, *args, **kwargs):
       serializer = UserSerializers(data=request.data)
       if serializer.is_valid():
           serializer.save() 
           return Response({"message": "Login True",
                            "status":True,
                            "data":serializer.data}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)