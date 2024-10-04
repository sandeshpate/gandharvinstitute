
# models.py

# models.py

from django.db import models
from django.utils.html import mark_safe

class SliderImage(models.Model):
    image = models.ImageField(upload_to='posters/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.alt_text if self.alt_text else "Slider Image"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="150" height="auto" />')
        return "No Image"
    image_tag.short_description = 'Image Preview'


# Create your models here.
