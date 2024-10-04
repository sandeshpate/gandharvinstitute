from django.contrib import admin
from aboutus.models import AddCourseabout #add dropdwon for about
from aboutus.models import SlidersImage #this is an about slider
from aboutus.models import SliderssOne, SliderssTwo #this is an automatic slider

from aboutus.models import TeamMembers #this is an team member

class AddCourseaboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)
admin.site.register( AddCourseabout,AddCourseaboutAdmin)

#this is an about slider
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'alt_text')
    search_fields = ('alt_text',)
admin.site.register( SlidersImage,SliderImageAdmin)


#this is an automatic slider
class SliderssOneAdmin(admin.ModelAdmin):
    list_display = ('text', 'img',  'desc')
    search_fields = ('text','desc',)
admin.site.register(SliderssOne, SliderssOneAdmin)
#this is an automatic slider
class SliderssTwoAdmin(admin.ModelAdmin):
    list_display = ('text', 'img', 'desc')
    search_fields = ('text','desc',)


admin.site.register(SliderssTwo, SliderssTwoAdmin)

#this is an about traineing team member 
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'email', 'verified')
    list_filter = ('department', 'verified')
    search_fields = ('name', 'email', 'department')
    ordering = ('name',)
    list_editable = ('verified',)
    fieldsets = (
        (None, {
            'fields': ('name', 'department', 'email', 'profile_image', 'verified')
        }),
        ('Social Media Links', {
            'classes': ('collapse',),
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'youtube_url'),
        }),
    )

admin.site.register(TeamMembers, TeamMembersAdmin)

# Register your models here.
