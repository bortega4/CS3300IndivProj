from django.contrib import admin

# Register your models here.
from .models import Program, Course, Lecturer, LectureNotes

admin.site.register(Course)
admin.site.register(Lecturer)
admin.site.register(LectureNotes)
admin.site.register(Program)