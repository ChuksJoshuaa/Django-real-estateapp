from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox


class accountform(UserCreationForm):
    email = forms.EmailField()
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
