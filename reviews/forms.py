from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review

        fields = [
            "rating",
            "comment"
        ]

        widgets = {

            "comment": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "review-textarea",
                    "placeholder": "Write your review..."
                }
            )

        }