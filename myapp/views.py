from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .forms import ProductForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
<<<<<<< HEAD
    submitted = False
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
            context = {
                    'form':ProductForm,
                    'submitted':submitted,                        }
            return render(request, 'index.html', context)
        context = {
            'form':form,
        }
        return render(request, 'index.html', context)
=======
    objs = Product.objects.all().values_list('id', 'name')
    return HttpResponse(objs)
>>>>>>> parent of d41fab9... add index.html
