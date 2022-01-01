from django.contrib import messages
from .forms import Realtorform
from django.views.generic import CreateView


class realtor_view(CreateView):
    form_class = Realtorform
    template_name = "realtors/realtor_form.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, f"You have successfully registered as a Realtor")
        return "/realtors/realtor/"


