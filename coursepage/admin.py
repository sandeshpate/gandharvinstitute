from django.contrib import admin
from coursepage.models import CourseContent #this is an course section
from coursepage.models import FeatureCard  #this is an course feature section
from coursepage.models import Workshopnew #this is an course workshop section
from coursepage.models import AddDropdownCourses  #add dropdwon for course
from coursepage.models import Servicecard #this is an course service section





class AddDropdownCoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)
admin.site.register(AddDropdownCourses,AddDropdownCoursesAdmin)
# Register your models here.


#this is an course feature section
class FeatureCardAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'description', 'link')

admin.site.register(FeatureCard,FeatureCardAdmin)

#this is an course section
class CourseContentAdmin(admin.ModelAdmin):
    list_display = ('order_index', 'title', 'subtitle', 'paragraph', 'image_url')
    ordering = ['order_index']


admin.site.register( CourseContent, CourseContentAdmin)

#this is an course workshop section

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'place')

admin.site.register( Workshopnew,WorkshopAdmin)

class ServicecardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
admin.site.register( Servicecard ,ServicecardAdmin)


