from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import ContactSerializer
from .models import *

# Create your views here.
class APIContact(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer