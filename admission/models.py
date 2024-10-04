from django.db import models



# models.py

class Admissionform(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15,null=True)
    email = models.EmailField()
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=15)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=15)
    permanent_address = models.TextField()
    temporary_address = models.TextField(blank=True, null=True)
    street_address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    previous_school = models.CharField(max_length=200)
    qualification = models.CharField(max_length=100)
    degree_name = models.CharField(max_length=100)
    previous_training = models.TextField(blank=True, null=True)
    theatre_experience = models.TextField(blank=True, null=True)
    performance_experience = models.TextField(blank=True, null=True)
    special_skills = models.TextField(blank=True, null=True)
    acting_group = models.TextField(blank=True, null=True)
    desired_course = models.CharField(max_length=100,default='Default Course')
    experience_level = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    drama_certificate = models.FileField(upload_to='certificates/')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
