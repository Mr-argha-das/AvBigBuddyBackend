from .bannermodels import Banners
from .bannersseril import BannerSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

class BannerAdd(CreateAPIView):
    queryset = Banners.objects.all()
    serializer_class = BannerSerializer
    parser_classes = (MultiPartParser, FormParser)
    def create(self, request, *args, **kwargs):
        serializer = BannerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                "message": "Banner add",
                "data": serializer.data,
                "status": True,
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Some thing went wrong",
            "data": None,
            "status": False,
        }, status=status.HTTP_400_BAD_REQUEST)


class BannerList(ListAPIView):
    queryset = Banners.objects.all()
    serializer_class = BannerSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset)
        return Response(queryset.values(), status=status.HTTP_200_OK)