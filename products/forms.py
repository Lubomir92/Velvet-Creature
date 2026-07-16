from django import forms
from .models import Product
from .models import ProductImage


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [
            "name",            
            "description",
            "short_description",
            "image",
            "sku",
            "material",
            "size",
            "weight",
            "price",
            "stock",
            "featured",
            "category",
        ]

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "rows": 5
                }
            ),

            "short_description": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),

        }





class ProductImageForm(forms.ModelForm):

    class Meta:

        model = ProductImage

        fields = [
            "image",
            "alt_text",
        ]