from django.contrib import admin

from myservice.models import ClassCard #this is home page of an service card section
from myservice.models import Play  #this is an homepage slider
from myservice.models import Photo, Feature #this is an home page of an about section
from myservice.models import AddCourse #add dropdwon for homepage

# from myservice.models import Servicecard #this is an course service section



# class ServicecardAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description')
# admin.site.register( Servicecard ,ServicecardAdmin)

class AddCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)
admin.site.register( AddCourse,AddCourseAdmin)












#this is an home page for about section   
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'position', 'speed', 'size')  # Columns to display in the admin list view
    list_filter = ('position', 'speed', 'size')  # Filters to narrow down results
    search_fields = ('image',)  # Enables searching by the image name
admin.site.register( Photo,PhotoAdmin)
#this is an home page of an about section
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('description',)  # Columns to display in the admin list view
    search_fields = ('description',)  # Enables searching by the feature description


admin.site.register( Feature,FeatureAdmin)






#this is home page of an service card section
class  MyserviceAdmin(admin.ModelAdmin):
    list_display=('title' ,  'description')
    
   
admin.site.register(ClassCard,MyserviceAdmin)

#this is an homepage slider
class  MyplayAdmin(admin.ModelAdmin):
    list_display=('heading' , 'type', 'descrip','button_url', 'btn_text')
    


admin.site.register(Play,MyplayAdmin)











# Register your models here.
