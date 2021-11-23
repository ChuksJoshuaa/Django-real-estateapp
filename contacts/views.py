from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactMeForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.user.username
        email = request.user.email
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.user.id
        realtor_email = request.POST['realtor_email']
        # Check if user has made inquiry already:
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/dashboard/')

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id, realtor_email=realtor_email)

        contact.save()

        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry fro ' + listing + '. Sign in to the admin panel for more information.',
             email,
            [realtor_email],
            fail_silently=True
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/dashboard/')

    return render(request, 'contacts/modal.html')