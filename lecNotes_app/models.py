from django.db import models
from django.urls import reverse

# Create your models here.
#Remember that python goes line by line
# If issues arise, you may have to rearrange models
# Refer to PortfolioApp

class Course(models.Model):
    coursePrefix = models.CharField(max_length=200)
    courseCode = models.IntegerField()
    courseName = models.CharField(max_length=200, blank=True)
    #decided to make lecturer a required field
    courseLecturer = models.CharField(max_length=200)

#define default string to return the name for representing the Model object
def __str__(self):
    #will think of a way to identify a course...
    #maybe make prefix and code a single field?
    #require course name?
    return self.coursePrefix

#Return the URL to access a particular instance of MyModelName.
#if you define this method then Django will automatically
#add a "View on Site" button to the model's record editing screens in Admin Site
def get_absolute_url(self):
    return reverse('course-detail', args=[str(self.id)])




