from django.db import models


    

#add dropdwon for homepage
class AddCourse(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    

#this is home page of an service card section
class ClassCard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_class = models.ImageField(upload_to='course/image',  max_length=50)

    def __str__(self):
        return self.title
    

   
#this is an homepage slider
class Play(models.Model):
    heading = models.CharField(max_length=255)
    type = models.CharField(max_length=100, blank=True, null=True)
    descrip = models.TextField()
    image = models.ImageField(upload_to='course/image', blank=True, null=True)
    btn_text=models.CharField(max_length=100,default=True,blank=True)
    button_url=models.URLField(max_length=250,default=False ,blank=True)
    

    def __str__(self):
        return self.heading



      






    
#this is an home page of an about section 
class Photo(models.Model):
    image = models.ImageField(upload_to='posters/')
    position = models.CharField(max_length=20, choices=[('left', 'Left'), ('right', 'Right')])
    speed = models.CharField(max_length=20, choices=[('slower', 'Slower'), ('lower50', 'Lower50')])
    size = models.CharField(max_length=20, choices=[('bottom', 'Bottom'), ('top', 'Top')])

    def __str__(self):
        return f'{self.position} - {self.image.name}'
#this is an home page of an about section
class Feature(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
    




# class Servicecard(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.ImageField(upload_to='posters/img')
#     link = models.URLField(max_length=200, blank=True)

#     def __str__(self):
#         return self.title


# Create your models here.