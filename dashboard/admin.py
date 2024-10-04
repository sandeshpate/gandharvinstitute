from django.contrib import admin



from .models import dashCourse

# Customize how Course appears in the admin panel
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'tutor_name', 'course_date' )
    search_fields = ('course_title', 'tutor_name')
    list_filter = ('course_date',)
    ordering = ('-course_date',)

# Register the Course model
admin.site.register(dashCourse, CourseAdmin)

# Register your models here.
