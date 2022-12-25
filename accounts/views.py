from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import accountform
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.apps import apps
Contact = apps.get_model('contacts', 'Contact')

# Create your views here.


def account_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = accountform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Your account has been created! You are now able to log in")
            return redirect('account-user_login')

    else:
        form = accountform()
    context = {
        "form": form
    }
    return render(request, "accounts/account-user_register.html", context)


@login_required
def dashboard(request):
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'other/dashboard.html', context)
