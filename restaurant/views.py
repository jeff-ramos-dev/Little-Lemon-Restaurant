from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import generics, viewsets 
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission, SAFE_METHODS
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from .forms import BookingForm
import datetime
import json

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


# Create your views here.
def index(request):
    current_year = str(datetime.date.today()).split('-')[0]
    return render(request, 'index.html', {"current_year": current_year})

def about(request):
    current_year = str(datetime.date.today()).split('-')[0]
    return render(request, 'about.html', {"current_year": current_year})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(
            reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                Name=data['Name'],
                No_of_guests=data['No_of_guests'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date', datetime.datetime.today().date())
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type='application/json')

def reservations(request):
    bookings = Booking.objects.all().order_by('reservation_date')
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":bookings, "bookings_json": booking_json})

def menu(request):
    menu_data = MenuItem.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = MenuItem.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 