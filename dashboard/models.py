from django.db import models





class dashCourse(models.Model):
    tutor_name = models.CharField(max_length=100,default=True)
    tutor_image = models.ImageField(upload_to='tutors/')
    course_title = models.CharField(max_length=200)
    course_date = models.DateField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    # video_count = models.IntegerField(default=False,blank=False)
    registration_link = models.URLField()

    def __str__(self):
        return self.course_title

# Create your models here.
