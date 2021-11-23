from django import forms
from .models import Realtor

class Realtorform(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = [
            'name',
            'image',
            'phone',
            'description',
            'email'
        ]