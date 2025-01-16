from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Property, User, Booking
from .serializers import PropertySerializer, UserSerializer,  BookingSerializer
# Create your views here.


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListingViewset(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Pass the user to the serializer
        serializer.save(host=self.request.user)


class BookingViewset(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
