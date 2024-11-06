# artapp/serializers.py
from rest_framework import serializers
from .models import Artist, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ArtistSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested serializer to show category details

    class Meta:
        model = Artist
        fields = ['id', 'name', 'art', 'price', 'category', 'blockbuster']
