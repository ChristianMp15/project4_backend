from django.shortcuts import render
from .models import Suit
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SuitSerializer

# Create your views here.

class SuitViewSet(viewsets.ModelViewSet):
    queryset = Suit.objects.all()
    serializer_class = SuitSerializer
    permission_class = [permissions.AllowAny]
