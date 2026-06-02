from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer_name',
            'email',
            'phone',
            'furniture_type',
            'description',
            'reference_image'
        ]

        widgets = {
            'customer_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Full Name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Email'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your WhatsApp Number'
                }
            ),

            'furniture_type': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Example: Wardrobe'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Tell us about your project'
                }
            ),

            'reference_image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }