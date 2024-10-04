from django.db import models

# Create your models here.

#add dropdwon for about
class AddCourseabout(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
#this is an about slider
class SlidersImage(models.Model):
    image = models.ImageField(upload_to='about/image')
    alt_text = models.CharField(max_length=255, blank=True)
    
    def __str__(self) :
        return self.alt_text
    
#this is an about automatic slider
class SliderssOne(models.Model):
    img = models.ImageField(upload_to='course/image')
    text = models.CharField(max_length=100)
    desc = models.TextField(default='',blank=True)
class SliderssTwo(models.Model):
    img = models.ImageField(upload_to='course/image')
    text = models.CharField(max_length=100)
    desc= models.TextField(default='',blank=True)


#this is an team member 
class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profiles/')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name