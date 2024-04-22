from django.db import models
from django.urls import reverse

# Create your models here.
#Remember that python goes line by line
# If issues arise, you may have to rearrange models
# Refer to PortfolioApp

#blank = True makes a field not required
class Program(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('program-detail', args=[str(self.id)])

class Course(models.Model):
    coursePrefix = models.CharField(max_length=200)
    courseCode = models.IntegerField()
    coursePrefixAndCode = models.CharField(max_length=200)
    courseName = models.CharField(max_length=200, blank=True)
    
    '''
    will try putting courseCode and prefix together
    courseID = coursePrefix + courseCode
    '''

    #define default string to return the name for representing the Model object
    def __str__(self):
        #will think of a way to identify a course...
        #maybe make prefix and code a single field?
        #require course name?
        return self.coursePrefixAndCode

    #Return the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    #add a "View on Site" button to the model's record editing screens in Admin Site
    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.id)])
    
    #course can have multiple lecturers, established in lecturer model
    #multiple lecture notes, relationship established in LectureNotes model
    #many courses to one program
    program = models.ForeignKey(Program, on_delete=models.CASCADE, default = None)

    

class Lecturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    #lecturer can have multiple courses, many lecturers to many courses?
    courses = models.ManyToManyField(Course)
    

class LectureNotes(models.Model):
    coursePrefix = models.CharField(max_length=200)
    courseCode = models.IntegerField()
    courseName = models.CharField(max_length=200, blank = True)
    lectureDate = models.DateField()
    lectureNum = models.IntegerField()
    notesAuthor = models.CharField(max_length=200, blank = True)
    #lectureDocument will go here

    #courseLecturer, may have to come back and play w this field
    #courseLecturer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.lectureNum)
    def get_absolute_url(self):
        return reverse('lecture-detail', args=[str(self.id)])
    
    #lectureNotes belong to one class, many lectureNotes to one course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, default=None)

    
    





