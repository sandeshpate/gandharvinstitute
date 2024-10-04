from django.contrib import admin


# admin.py
from costume.models import costumeSection
from costume.models import  costumeFeature

from costume.models import costumecourse, costumeDuration,costumeFee
from costume.models import costumeCoursesyllbi, costumeCourseSyllabus
from costume.models import costumeCardSliderItem

class costumesectionAdmin(admin.ModelAdmin):
    list_display = ['heading', 'subheading']
admin.site.register(costumeSection, costumesectionAdmin)




class costumeFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
admin.site.register( costumeFeature,costumeFeatureAdmin)




class costumeCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    search_fields = ('title', 'description')
    list_filter = ('title',)
admin.site.register(costumecourse,costumeCourseAdmin)



class costumeDurationAdmin(admin.ModelAdmin):
    list_display = ('course', 'duration', 'time_slots', 'batches','image')
    search_fields = ('course__title', 'duration', 'time_slots')
    list_filter = ('course',)
admin.site.register(costumeDuration,costumeDurationAdmin)


class costumeFeeAdmin(admin.ModelAdmin):
    list_display = ('course', 'basic_price', 'pro_price')
    search_fields = ('course__title', 'basic_price', 'pro_price')
    list_filter = ('course',)

admin.site.register(costumeFee,costumeFeeAdmin)



class costumeCourseSyllabusInline(admin.TabularInline):
    model =  costumeCourseSyllabus
    extra = 1

class setCourseAdmin(admin.ModelAdmin):
    inlines = [costumeCourseSyllabusInline]

admin.site.register(costumeCoursesyllbi, costumeCourseAdmin)

# admin.py





class costumeCardSliderItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    list_filter = ('title',)
    search_fields = ('title', )
   
    fieldsets = (
        (None, {
            'fields': ('title',  'image')
        }),
        ('Buttons', {
            'fields': ('register_button_text', 'register_button_link', 'view_button_text', 'view_button_link')
        }),
    )
    # filter_horizontal = ()
    ordering = ('title',)
admin.site.register(costumeCardSliderItem, costumeCardSliderItemAdmin)


# list_display: Specifies which fields should be displayed in the list view of the admin interface.
# list_filter: Adds a filter sidebar to allow filtering by the specified field.
# search_fields: Adds a search box to the admin interface to search by the specified fields.
# readonly_fields: Marks the specified fields as read-only in the admin interface.
# fieldsets: Organizes fields into sections for a cleaner layout in the admin form.
# ordering: Defines the default ordering of items in the list view.

# Register your models here.




