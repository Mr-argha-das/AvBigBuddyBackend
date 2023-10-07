from .tagsmodels import Tags
from .tagserailizer import TagsSerializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.response import Response


class TagsLsit(ListAPIView):
    def list(self, request, *args, **kwargs):
        query = Tags.objects.all()
        serializer = TagsSerializers(query, many=True)
        return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)

class TagsAdd(CreateAPIView):
    queryset = Tags.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = TagsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Tag added", "data": serializer.data, "status": True }, status=status.HTTP_200_OK)
        return Response({"message":"Some thing went wrong", "data": None, "status": True }, status=status.HTTP_400_BAD_REQUEST)