from django.forms import ModelForm
from .models import Course, LectureNotes, Program
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form
class LecNotesForm(ModelForm):
   class Meta:
       model = LectureNotes
       fields = ['lectureNum', 'lectureDate', 'course', 'lecturer']