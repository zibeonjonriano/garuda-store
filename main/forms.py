# main/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__" #form itu akan otomatis menyertakan semua field/atribut dari model.
        # name, price, description, thumbnail, category, is_featured, size, dan stock.