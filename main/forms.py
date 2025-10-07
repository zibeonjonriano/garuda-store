# main/forms.py
from django import forms
from .models import Product
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","price", "description", "thumbnail", "category", "is_featured", "size", "stock"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter product name"
            }),
            "price": forms.NumberInput(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter price"
            }),
            "description": forms.Textarea(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter product description",
                "rows": 4
            }),
            "thumbnail": forms.URLInput(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter thumbnail URL"
            }),
            "category": forms.Select(attrs={
                "class": "bg-gray-800 text-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "text-[#b3f300] focus:ring-[#b3f300] rounded"
            }),
            "size": forms.Select(attrs={
                "class": "bg-gray-800 text-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
            }),
            "stock": forms.NumberInput(attrs={
                "class": "bg-gray-800 text-white placeholder-white px-3 py-2 rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-[#b3f300] focus:border-transparent",
                "placeholder": "Enter stock"
            }),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)
