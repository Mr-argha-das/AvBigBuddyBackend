from rest_framework import serializers
from .tagsmodels import Tags

class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'name')