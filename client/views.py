import imp
from django.shortcuts import render

from product.models import Product
from rest_framework.views import APIView

# Create your views here.
class ClientPageView(APIView):
    def get():
        products=Product.objects.all()

