from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializersMethodField()

    class Meta:
        model = Product
        field = '__all__'

    def get_average_rating(self, obj):
        pass