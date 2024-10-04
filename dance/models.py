from django.db import models
  

# models.py


class DanceSection(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    button_text = models.CharField(max_length=50)
    button_link = models.URLField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.heading
    


class DanceFeature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title




class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Coursesyllbi(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images/')
    
    def __str__(self):
        return self.title

class CourseSyllabus(models.Model):
    course = models.ForeignKey(Coursesyllbi, related_name='syllabus', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Duration(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100)
    time_slots = models.TextField()
    batches = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)

    def __str__(self):
        return f"Duration for {self.course.title}"

class Fee(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    basic_price = models.DecimalField(max_digits=6, decimal_places=2)
    pro_price = models.DecimalField(max_digits=6, decimal_places=2)
    text=models.TextField(default=True, null=True)
    text2=models.TextField(default=True, null=True)
    def __str__(self):
        return f"Fees for {self.course.title}"








class CardSliderItem(models.Model):
    title = models.CharField(max_length=255,default=False,blank=False,null=False)
    # subtitle = models.CharField(max_length=255, default=False,blank=False,null=False)
    # description = models.TextField()
    image = models.ImageField(upload_to='slider_images/' ,blank=True, null=True)
    register_button_text = models.CharField(max_length=50, default="Register Now")
    register_button_link = models.URLField(default="#")
    view_button_text = models.CharField(max_length=50, default="View More")
    view_button_link = models.URLField(default="#")

    def __str__(self):
        return self.title

