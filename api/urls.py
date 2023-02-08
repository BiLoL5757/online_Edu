from django.urls import path
from .views import *


urlpatterns = [
    path('contact/', APIContact.as_view(), name='api_contact')    
]