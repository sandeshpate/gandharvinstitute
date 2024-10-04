from django.contrib import admin



from singing.models import singingSection
from singing.models import  singingFeature
from singing.models import singingcourse, singingDuration,singingFee
from singing.models import singingCoursesyllbi, singingCourseSyllabus
from singing.models import singingCardSliderItem

class singingSectionAdmin(admin.ModelAdmin):
    list_display = ['heading', 'subheading']
admin.site.register(singingSection,singingSectionAdmin)
# admin.py



class singingFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
admin.site.register(singingFeature,singingFeatureAdmin)




class singingCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')
    list_filter = ('title',)
admin.site.register(singingcourse, singingCourseAdmin)



class singingDurationAdmin(admin.ModelAdmin):
    list_display = ('course', 'duration', 'time_slots', 'batches','image')
    search_fields = ('course__title', 'duration', 'time_slots')
    list_filter = ('course',)
admin.site.register(singingDuration,singingDurationAdmin)


class singingFeeAdmin(admin.ModelAdmin):
    list_display = ('course', 'basic_price', 'pro_price')
    search_fields = ('course__title', 'basic_price', 'pro_price')
    list_filter = ('course',)

admin.site.register(singingFee,singingFeeAdmin)



class setCourseSyllabusInline(admin.TabularInline):
    model = singingCourseSyllabus
    extra = 1

class setCourseAdmin(admin.ModelAdmin):
    inlines = [setCourseSyllabusInline]

admin.site.register(singingCoursesyllbi, setCourseAdmin)

# admin.py





class singingCardSliderItemAdmin(admin.ModelAdmin):
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
admin.site.register(singingCardSliderItem, singingCardSliderItemAdmin)


# list_display: Specifies which fields should be displayed in the list view of the admin interface.
# list_filter: Adds a filter sidebar to allow filtering by the specified field.
# search_fields: Adds a search box to the admin interface to search by the specified fields.
# readonly_fields: Marks the specified fields as read-only in the admin interface.
# fieldsets: Organizes fields into sections for a cleaner layout in the admin form.
# ordering: Defines the default ordering of items in the list view.

# Register your models here.




