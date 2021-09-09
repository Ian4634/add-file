from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
# Create your views here.

def index(request):
    objs = Product.objects.all().values_list('id', 'name')
    return HttpResponse(objs)