from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
#from django.template import loader
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Program, Course, Lecturer, LectureNotes
from .forms import LecNotesForm, CourseForm
# Create your views here.
def index(request):
    #Pulling UCCS Programs
    uccs_programs = Program.objects.all()

    # Render the HTML template index.html with the
    # data in the conext variable
    return render ( request, 'lecNotes_app/index.html', {'uccs_programs':uccs_programs})


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

    #passing 'lectureNotes' queryset to context, but in this instance it is not
    #used in the template. If trying to display existing lecture notes alongside form
    #you may iterate over this queryset in tempplate to display them
    context['lectureNotes'] = lecNotes

    if request.method == 'POST':
        form = LecNotesForm(request.POST)
        if 'save' in request.POST:
            if form.is_valid():
                #setting course code based on selected course, same w lecturer
                course = form.cleaned_data['existing_course']
                lecturer = form.cleaned_data['existing_lecturer']

                lecture_note = form.save(commit=False)
                lecture_note.course = course
                lecture_note.courseCode = course.courseCode
                lecture_note.lecturer = lecturer
                lecture_note.save()
                
                '''
                Another way to simply save form without anything extra:
                form.save() #save form data if 'save' button is pressed

                Optional: you can redirect user to another page after saving lecNotes form
                '''
                #constructing URL for course detail page
                course_detail_url = reverse('course-detail', args=[course.id])
                return redirect(course_detail_url)
            
    context['form'] = form

    return render(request, 'lecNotes_app/create_lecNotes.html', context)

#refer to create_lecNotes view as a master class. gpt has code somwhere
def create_course(request):
    context = {}
    form = CourseForm()
    courses = Course.objects.all()
    context['courses'] = courses
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if 'save' in request.POST:
            if form.is_valid():
                form.save()
                #return redirect('redirect-url-here')
    else:
        form = CourseForm()
        
    return render(request, 'lecNotes_app/create_course.html', {'form': form})

class SearchResultsView(ListView):
    model = Course
    template_name = 'lecNotes_app/search_results.html'
    context_object_name = 'search_results_list'

    #try def get_queryset(request) next
    #changed this from def get_queryset(self) to:
    def get_queryset(self):
        #retrieving value of query parameter named 'q' from URL's query string
        query = self.request.GET.get('q')
        #search method refers to coursePrefixAndCode/coursePrefix/courseCode
        search_method = self.request.GET.get('search_method')

        
        #performing search based on selected search method
        if search_method == 'coursePrefixAndCode':
            search_results_list = Course.objects.filter(coursePrefixAndCode__icontains=query)
            #template = loader.get_template('lecNotes_app/search_results.html')
            context = {
                'search_results_list' : search_results_list,
            }
        elif search_method == 'coursePrefix':
            '''
            search_results_list = Course.objects.filter(Q(coursePrefix__icontains=query))
            #template = loader.get_template('lecNotes_app/search_results.html')
            context = {
                'search_results_list' : search_results_list,
            }
            '''
            return Course.objects.filter(coursePrefix__icontains=query)

        elif search_method == 'courseCode':
            search_results_list = Course.objects.filter(courseCode__icontains=query)
            #template = loader.get_template('lecNotes_app/search_results.html')
            context = {
                'search_results_list' : search_results_list,
            }
        

        #search_results = Course.objects.filter(courseCode__icontains=query)
        #return render('lecNotes_app/search_results.html', context)
        
        else:
            #return an empty queryset and set a flag to indicate error
            #error_message = "Please verify search query aligns with search method."
            return Course.objects.none()#, error_message #returning empty queryset and error message

    


#example for a second login page with a basic placeholder response
def login(request):
    return render(HttpResponse, 'Login Page')
