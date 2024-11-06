# artapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Category
from .serializers import ArtistSerializer, CategorySerializer

@api_view(['GET'])
def get_artists_by_category(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
        artists = Artist.objects.filter(category=category)
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_blockbuster_artists(request):
    blockbuster_artists = Artist.objects.filter(blockbuster=True)
    serializer = ArtistSerializer(blockbuster_artists, many=True)
    return Response({"2024 Art Blockbuster": serializer.data})

@api_view(['GET'])
def shop_by_price(request, min_price, max_price):
    artists = Artist.objects.filter(price__gte=min_price, price__lte=max_price)
    serializer = ArtistSerializer(artists, many=True)
    return Response({"Shop by Price": serializer.data})
