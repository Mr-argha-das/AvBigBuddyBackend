
from rest_framework import serializers
from .bannermodels import Banners

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ('id', 'image_path', 'title')