from django.contrib import admin



from django.contrib import admin
from .models import Admissionform

class AdmissionAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 
        'last_name', 
        'email', 
        'contact', 
        'desired_course', 
        'experience_level', 
        'dob'
    )
    search_fields = (
        'first_name', 
        'last_name', 
        'email', 
        'father_name', 
        'mother_name'
    )
    list_filter = ('gender', 'desired_course', 'experience_level')
    ordering = ('last_name', 'first_name')
    list_editable = ('desired_course', 'experience_level')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If we are editing an existing object
            return ['photo', 'drama_certificate']  # Make fields read-only
        return []

admin.site.register(Admissionform, AdmissionAdmin)

# Register your models here.
