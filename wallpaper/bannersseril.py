
from rest_framework import serializers
from .bannermodels import Banners


class BannerSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Banners
        fields = ('id', 'image_url', 'title')