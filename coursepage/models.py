from django.db import models

 #add dropdwon for course
class AddDropdownCourses(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


#this is an course section
class CourseContent(models.Model):
    title = models.CharField(max_length=255 ,  blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    paragraph = models.TextField(default=False, blank=True)
    image_url = models.ImageField(upload_to='course/image' ,blank=True,null=True)
    order_index = models.IntegerField()
    alt_text = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f"{self.title} (Order: {self.order_index})"

#this is an course feature section
class FeatureCard(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(default='#')

    def __str__(self):
        return self.title

#this is an course workshop section

class Workshopnew(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=50)
    place = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='workshops/')
    thumbnail1 = models.ImageField(upload_to='workshops/')
    thumbnail2 = models.ImageField(upload_to='workshops/')
    thumbnail3 = models.ImageField(upload_to='workshops/')
    facebook_icon = models.URLField(max_length=200)
    instagram_icon = models.URLField(max_length=200)
    twitter_icon = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Servicecard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posters/img')
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
    # class Servicecard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posters/img')
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title



# Create your models here.
