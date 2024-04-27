from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Program, Course, Lecturer, LectureNotes, NotesAuthor, get_current_user
from .forms import LecNotesForm, CourseForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required

#@login_required decorator will redirect a user who isn't logged in to
#login page before they can view the page

#@unauthenticated_user will redirect a user that is logged in - useful for registerPage function in
#views.py because a logged in user should not be able to create a new user

#@allowed_users allows us to specify which role is allowed to view the page
#@allowed_users(allowed_roles=['author_role'])

# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='author_role')
            user.groups.add(group)
            author = NotesAuthor.objects.create(user=user)
            author.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
    context = { 'form':form}
    return render(request, 'registration/register.html', context)


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

@login_required(login_url='login')
def create_lecNotes(request):
    context = {}
    #getting current logged-in user
    #user = request.user
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
                #lecture_note.user = get_current_user(request)
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


    

'''
#example for a second login page with a basic placeholder response
def login(request):
    return render(HttpResponse, 'Login Page')
'''
