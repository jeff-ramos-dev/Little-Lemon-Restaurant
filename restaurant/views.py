from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
