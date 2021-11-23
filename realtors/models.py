from django.db import models
from django.core.files.storage import default_storage as storage
from datetime import datetime
from PIL import Image
# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Real_Estate/realtors/media/', null=False, blank=False)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name and self.description:
            return

        super(Realtor, self).save()
        if self.image:
            size = 200, 200
            image = Image.open(self.image)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            format = 'png'
            image.save(fh, format)
            fh.close()