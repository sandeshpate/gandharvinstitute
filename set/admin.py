from django.contrib import admin



from set.models import setSection
from set.models import  setFeature
from set.models import setcourse, setDuration,setFee
from set.models import setCoursesyllbi, setCourseSyllabus
from set.models import setCardSliderItem

class setSectionAdmin(admin.ModelAdmin):
    list_display = ['heading', 'subheading']
admin.site.register(setSection,setSectionAdmin)
# admin.py



class setFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
admin.site.register(setFeature,setFeatureAdmin)




class setCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')
    list_filter = ('title',)
admin.site.register(setcourse,setCourseAdmin)



class setDurationAdmin(admin.ModelAdmin):
    list_display = ('course', 'duration', 'time_slots', 'batches','image')
    search_fields = ('course__title', 'duration', 'time_slots')
    list_filter = ('course',)
admin.site.register(setDuration,setDurationAdmin)


class setFeeAdmin(admin.ModelAdmin):
    list_display = ('course', 'basic_price', 'pro_price')
    search_fields = ('course__title', 'basic_price', 'pro_price')
    list_filter = ('course',)

admin.site.register(setFee,setFeeAdmin)



class setCourseSyllabusInline(admin.TabularInline):
    model = setCourseSyllabus
    extra = 1

class setCourseAdmin(admin.ModelAdmin):
    inlines = [setCourseSyllabusInline]

admin.site.register(setCoursesyllbi, setCourseAdmin)

# admin.py





class setCardSliderItemAdmin(admin.ModelAdmin):
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
admin.site.register(setCardSliderItem, setCardSliderItemAdmin)


# list_display: Specifies which fields should be displayed in the list view of the admin interface.
# list_filter: Adds a filter sidebar to allow filtering by the specified field.
# search_fields: Adds a search box to the admin interface to search by the specified fields.
# readonly_fields: Marks the specified fields as read-only in the admin interface.
# fieldsets: Organizes fields into sections for a cleaner layout in the admin form.
# ordering: Defines the default ordering of items in the list view.

# Register your models here.




