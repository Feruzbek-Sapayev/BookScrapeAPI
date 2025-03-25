from rest_framework import serializers
from .models import Book
from .utils import euro
from decimal import Decimal

class BookSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'image', 'description', 'slug']
    
    def get_price(self, obj):
        price = Decimal(obj.price) * Decimal(str(euro()))
        return  int(price) 