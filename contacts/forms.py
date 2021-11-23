from django import forms
from .models import Contact

class ContactMeForm(forms.Form):
    class Meta:
        model = Contact
        fields = [
            'listing_id',
            'listing',
            'name',
            'email',
            'phone',
            'message',
            'user_id',
            'realtor_email',
        ]
