from rest_framework import serializers
from .models import MovieData


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, default='default.jpg')

    class Meta:
        model = MovieData
        fields = '__all__'
