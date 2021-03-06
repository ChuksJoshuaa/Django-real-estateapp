from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.views.generic import TemplateView
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ListingForm
import folium

from .models import Listing


def home_view(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 5)
    page = request.GET.get('page')
    listings_page = paginator.get_page(page)

    context = {
        'listings': listings_page
    }

    return render(request, 'listings/listing.html', context)


class listings_detail(DetailView):
    model = Listing
    template_name = 'listings/list_detail.html'

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Listing, id=id)


class ListingCreate(LoginRequiredMixin, CreateView):
    form_class = ListingForm
    template_name = "listings/list_create.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, f"A new Listing has been approved")
        return "/listings/home/"


def search_view(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # STATE
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # CITY
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # BEDROOMS
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # PRICE
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET,
    }

    return render(request, 'listings/search.html', context)

class update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ListingForm
    template_name = "listings/list_create.html"
    queryset = Listing.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Listing, id=id)


    def test_func(self):
        Listing = self.get_object()
        if Listing.realtor:
            return True
        else:
            return False

    def get_success_url(self):
        return "/listings/home/"

class delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    template_name = "listings/list_delete.html"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Listing, id=id)

    def test_func(self):
        Listing = self.get_object()
        if Listing.realtor:
            return True
        else:
            return False

    def get_success_url(self):
        return "/listings/home/"


#Using Folium map
class FoliumView(TemplateView):
    template_name = "listings/map.html"

    def get_context_data(self, **kwargs):
        figure = folium.Figure()
        m = folium.Map(
            location=[6.465422, 3.406448],
            zoom_start=7,
            tiles='Stamen Terrain'
        )
        m.add_to(figure)

        folium.Marker(
            location=[6.4698, 3.601521],
            popup='Lekki Lagos',
            icon=folium.Icon(icon='darkblue')
        ).add_to(m)

        folium.Marker(
            location=[9.0479, 7.5155],
            popup='Asokoro Abuja',
            icon=folium.Icon(color='green')
        ).add_to(m)

        folium.Marker(
            location=[6.4667, 3.4500],
            popup='Banana Island, Lagos',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

        folium.Marker(
            location=[6.063996, 7.476005],
            popup='Agwu, Enugu',
            icon=folium.Icon(color='gray')
        ).add_to(m)

        figure.render()
        return {"map": figure}
