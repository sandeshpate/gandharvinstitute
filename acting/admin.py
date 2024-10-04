from django.contrib import admin


from acting.models import ActingSection
from acting.models import  ActingFeature
from acting.models import Acting, ActDuration, ActingFee
from acting.models import Coursesyllbi, ActingSyllabus
from acting.models import ActingCardSliderItem

class DanceSectionAdmin(admin.ModelAdmin):
    list_display = ['heading', 'subheading']
admin.site.register(ActingSection,DanceSectionAdmin)
# admin.py



class DanceFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
admin.site.register(ActingFeature,DanceFeatureAdmin)




class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')
    list_filter = ('title',)
admin.site.register(Acting,CourseAdmin)



class DurationAdmin(admin.ModelAdmin):
    list_display = ('course', 'duration', 'time_slots', 'batches','image')
    search_fields = ('course__title', 'duration', 'time_slots')
    list_filter = ('course',)
admin.site.register(ActDuration,DurationAdmin)


class FeeAdmin(admin.ModelAdmin):
    list_display = ('course', 'basic_price', 'pro_price')
    search_fields = ('course__title', 'basic_price', 'pro_price')
    list_filter = ('course',)

admin.site.register(ActingFee,FeeAdmin)



class CourseSyllabusInline(admin.TabularInline):
    model = ActingSyllabus
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseSyllabusInline]

admin.site.register(Coursesyllbi, CourseAdmin)

# admin.py





class CardSliderItemAdmin(admin.ModelAdmin):
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
admin.site.register(ActingCardSliderItem, CardSliderItemAdmin)


# list_display: Specifies which fields should be displayed in the list view of the admin interface.
# list_filter: Adds a filter sidebar to allow filtering by the specified field.
# search_fields: Adds a search box to the admin interface to search by the specified fields.
# readonly_fields: Marks the specified fields as read-only in the admin interface.
# fieldsets: Organizes fields into sections for a cleaner layout in the admin form.
# ordering: Defines the default ordering of items in the list view.

# Register your models here.



# Register your models here.
