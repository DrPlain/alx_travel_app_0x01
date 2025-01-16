from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Property, User
from .serializers import PropertySerializer, UserSerializer
# Create your views here.


class PropertyListCreateAPIView(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        # Pass the user to the serializer
        serializer.save(host=self.request.user)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
