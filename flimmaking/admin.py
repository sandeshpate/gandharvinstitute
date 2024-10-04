from django.contrib import admin






from flimmaking.models import flimSection
from flimmaking.models import  flimFeature
from flimmaking.models import flimcourse, flimDuration,flimFee
from flimmaking.models import flimCoursesyllbi, flimCourseSyllabus
from flimmaking.models import flimCardSliderItem

class flimSectionAdmin(admin.ModelAdmin):
    list_display = ['heading', 'subheading']
admin.site.register(flimSection,flimSectionAdmin)
# admin.py



class flimFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
admin.site.register(flimFeature,flimFeatureAdmin)




class flimCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')
    list_filter = ('title',)
admin.site.register(flimcourse,flimCourseAdmin)



class flimDurationAdmin(admin.ModelAdmin):
    list_display = ('course', 'duration', 'time_slots', 'batches','image')
    search_fields = ('course__title', 'duration', 'time_slots')
    list_filter = ('course',)
admin.site.register(flimDuration,flimDurationAdmin)


class flimFeeAdmin(admin.ModelAdmin):
    list_display = ('course', 'basic_price', 'pro_price')
    search_fields = ('course__title', 'basic_price', 'pro_price')
    list_filter = ('course',)

admin.site.register(flimFee,flimFeeAdmin)



class flimCourseSyllabusInline(admin.TabularInline):
    model = flimCourseSyllabus
    extra = 1

class setCourseAdmin(admin.ModelAdmin):
    inlines = [flimCourseSyllabusInline]

admin.site.register(flimCoursesyllbi, setCourseAdmin)

# admin.py





class flimCardSliderItemAdmin(admin.ModelAdmin):
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
admin.site.register(flimCardSliderItem, flimCardSliderItemAdmin)


# list_display: Specifies which fields should be displayed in the list view of the admin interface.
# list_filter: Adds a filter sidebar to allow filtering by the specified field.
# search_fields: Adds a search box to the admin interface to search by the specified fields.
# readonly_fields: Marks the specified fields as read-only in the admin interface.
# fieldsets: Organizes fields into sections for a cleaner layout in the admin form.
# ordering: Defines the default ordering of items in the list view.

# Register your models here.





# Register your models here.
