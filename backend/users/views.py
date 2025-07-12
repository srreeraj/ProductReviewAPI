from rest_framework import generics,permissions
from .models import User
from .serializers import RegisterSerializer
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
