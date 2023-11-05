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
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TagsSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TagsAdd(CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers

    def create(self, request, *args, **kwargs):
        serializer = TagsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Tag added", "data": serializer.data, "status": True}, status=status.HTTP_200_OK)
        return Response({"message": "Some thing went wrong", "data": None, "status": False}, status=status.HTTP_400_BAD_REQUEST)


class TagsByBannerId(ListAPIView):
    def list(self, request, *args, **kwargs):
        ba_id = request.GET.get("ba_id")
        query = Tags.objects.filter(banner_id=ba_id)
        user = list(query.values())
        return Response({
            "messsage": "Tags Found",
            "data": user,
            "status": True,
        }, status=status.HTTP_200_OK)
