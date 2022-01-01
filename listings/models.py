from django.db import models
from django.urls import reverse
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.IntegerField(default=0)
    photo_main = models.ImageField(upload_to='Real_Estate/listings/media/')
    photo_1 = models.ImageField(upload_to='Real_Estate/listings/media/', blank=True)
    photo_2 = models.ImageField(upload_to='Real_Estate/listings/media/', blank=True)
    photo_3 = models.ImageField(upload_to='Real_Estate/listings/media/', blank=True)
    photo_4 = models.ImageField(upload_to='Real_Estate/listings/media/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"id": self.id})