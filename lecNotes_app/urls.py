from django.urls import path
from . import views

urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>
    path('', views.index, name='index'),

    #needed /<pk>, any time go into anything in a list, a specific item in database
    path('program_details/<pk>', views.ProgramDetailView.as_view(), name='program-detail'),

    path('course_details/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),

    path('create_lecNotes/', views.create_lecNotes, name = 'create_lecNotes'),

    path('login/', views.login, name='login'),
]