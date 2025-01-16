from django.urls import path
from listings.views import PropertyListCreateAPIView, UserListCreateAPIView

urlpatterns = [
    path('listing/', PropertyListCreateAPIView.as_view(), name='listing'),
    path('user/', UserListCreateAPIView.as_view(), name='user')
]
