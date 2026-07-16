from django import forms
from .models import Order


class ShippingForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            "carrier",
            "tracking_number",
        ]

        widgets = {

            "carrier": forms.TextInput(
                attrs={
                    "placeholder": "GLS, Packeta, DPD..."
                }
            ),

            "tracking_number": forms.TextInput(
                attrs={
                    "placeholder": "Tracking number"
                }
            ),
        }