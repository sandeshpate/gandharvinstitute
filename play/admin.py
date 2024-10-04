from django.contrib import admin

# Register your models here.
# admin.py


from play.models import SliderImage
from django.utils.html import mark_safe

class SliderImageAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('image_preview', 'alt_text')
    
    # Fields to search by in the admin search bar
    search_fields = ('alt_text',)
    
    # Fields that appear on the detail/edit page
    fields = ('image', 'alt_text')
    
    # Method to display image preview in the list view
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="auto" />')
        return "No Image"
    image_preview.short_description = 'Image Preview'

# Registering the model with the custom admin class
admin.site.register(SliderImage, SliderImageAdmin)

