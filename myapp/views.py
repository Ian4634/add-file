from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(Product.objects.all().values())