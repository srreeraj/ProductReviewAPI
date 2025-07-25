from rest_framework import serializers
from .models import Product
from review.models import Review

class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_average_rating(self, obj):
        reviews = Review.objects.filter(product=obj)
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 2)
        return None