from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category')

        labels = {
            'name':'product name'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'name'}),
            'category':forms.TextInput(attrs={'class':'form-control'})
        }