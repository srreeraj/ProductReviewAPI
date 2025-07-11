from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.persmissions import BasePermission, SAFE_METHODS
# Create your views here.

class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_authenticated and request.user.is_staff

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]