from django import forms

from .models import CustomOrder




class CustomOrderForm(forms.ModelForm):


    class Meta:


        model = CustomOrder


        fields = [


            "name",

            "email",

            "phone",


            "service",


            "description",


            "engraving",

            "engraving_type",

            "engraving_text",

            "engraving_image",



            "material",

            "color",


            "width",

            "height",

            "depth",


            "quantity",


            "model_file",

            "image",

        ]



        widgets = {



            "name": forms.TextInput(

                attrs={

                    "class": "custom-input",

                    "placeholder": "Your name"

                }

            ),




            "email": forms.EmailInput(

                attrs={

                    "class": "custom-input",

                    "placeholder": "your@email.com"

                }

            ),




            "phone": forms.TextInput(

                attrs={

                    "class": "custom-input",

                    "placeholder": "+33 ..."

                }

            ),





            "service": forms.Select(

                attrs={

                    "class": "custom-input"

                }

            ),





            "description": forms.Textarea(

                attrs={

                    "class": "custom-input custom-textarea",

                    "rows": 6,

                    "placeholder":
                    "Describe your project, size, purpose and special requirements..."

                }

            ),





            "engraving": forms.CheckboxInput(

                attrs={

                    "class": "custom-checkbox"

                }

            ),





            "engraving_type": forms.Select(

                attrs={

                    "class": "custom-input"

                }

            ),




            "engraving_text": forms.TextInput(

                attrs={

                    "class": "custom-input",

                    "placeholder":
                    "Example: Lubma3D, name, logo text..."

                }

            ),





            "engraving_image": forms.FileInput(

                attrs={

                    "class": "custom-input"

                }

            ),





            "material": forms.Select(

                attrs={

                    "class": "custom-input"

                }

            ),





            "color": forms.TextInput(

                attrs={

                    "class": "custom-input",

                    "placeholder":
                    "Example: Black, Gold, Red..."

                }

            ),





            "width": forms.NumberInput(

                attrs={

                    "class": "custom-input",

                    "placeholder": "mm"

                }

            ),





            "height": forms.NumberInput(

                attrs={

                    "class": "custom-input",

                    "placeholder": "mm"

                }

            ),





            "depth": forms.NumberInput(

                attrs={

                    "class": "custom-input",

                    "placeholder": "mm"

                }

            ),





            "quantity": forms.NumberInput(

                attrs={

                    "class": "custom-input",

                    "min": 1

                }

            ),





            "model_file": forms.FileInput(

                attrs={

                    "class": "custom-input"

                }

            ),





            "image": forms.FileInput(

                attrs={

                    "class": "custom-input"

                }

            ),



        }





    def clean_quantity(self):


        quantity = self.cleaned_data.get(
            "quantity"
        )


        if quantity < 1:


            raise forms.ValidationError(

                "Quantity must be at least 1."

            )


        return quantity