from django.shortcuts import render
from django.core.paginator import Paginator
from django.apps import apps
Listing = apps.get_model('listings', 'Listing')
Realtor = apps.get_model('realtors', 'Realtor')

from listings.choices import price_choices, bedroom_choices, state_choices


def home_view(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listing = paginator.get_page(page)

    context = {
        'listings': page_listing,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/home.html', context)


def about_view(request):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)