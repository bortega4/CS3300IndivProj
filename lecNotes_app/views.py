from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Program, Course, Lecturer, LectureNotes
from .forms import LecNotesForm
# Create your views here.
def index(request):
    #Pulling UCCS Programs
    uccs_programs = Program.objects.all()

    # Render the HTML template index.html with the
    # data in the conext variable
    return render ( request, 'lecNotes_app/index.html', {'uccs_programs':uccs_programs})

'''
class ProgramListView(ListView):
    #declaring program_list but really we are getting list of courses
    #that are within program
    context_object_name = "program_course_list"

    #trying to obtain courses within a specific program
    #might have to do Program.objects.course_set.all()
    queryset = Program.course_set
'''

class ProgramDetailView(DetailView):
    model = Program

    #context_object_name let's you do program_list instead of object_list in html
    context_object_name = 'program'
    
    #overriding get_context_data method from DetailView to fetch courses for program
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = self.get_object()
        context['courses'] = program.course_set.all()
        return context
    
class CourseDetailView(DetailView):
    model = Course

def create_lecNotes(request):
    context = {}
    form = LecNotesForm()
    lecNotes = LectureNotes.objects.all()
    context['lectureNotes'] = lecNotes
    if request.method == 'POST':
        if 'save' in request.POST:
            form = LecNotesForm(request.POST)
            #form.save() #commented out to prevent program from breaking
            
    context['form'] = form

    return render(request, 'lecNotes_app/create_lecNotes.html', context)
#example for a second login page with a basic placeholder response
def login(request):
    return render(HttpResponse, 'Login Page')
