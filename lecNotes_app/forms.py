from django import forms
from django.forms import ModelForm
from .models import Course, LectureNotes, Program, Lecturer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class for course form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        #may have to come back and remove courseName, will see how it plays out
        fields = ['coursePrefix', 'courseCode', 'coursePrefixAndCode', 'courseName', 'program']

#create class for lecNotes form
class LecNotesForm(ModelForm):
   #defining field for selecting existing courses and lecturers
   existing_course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True, label='Select Exisiting Course')
   existing_lecturer = forms.ModelChoiceField(queryset=Lecturer.objects.all(), required=True, label='Slect Existing Lecturer')
   
   '''
   #defining field for creating a new course, refer to chatGPT for creating new course
   #and to finish this portion
   new_course = forms.
   '''

   class Meta:
       model = LectureNotes
       widgets = {
           'summary': forms.Textarea(attrs={'rows':80, 'cols':20}),
       }
       fields = ['lectureNum', 'lectureDate', 'existing_course', 'existing_lecturer']