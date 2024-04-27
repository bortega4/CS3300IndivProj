from django.test import TestCase
from django.urls import reverse
from lecNotes_app.models import Program, Course, Lecturer, LectureNotes, NotesAuthor
from django.contrib.auth.models import User


# Create your tests here.
class ProgramModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Program.objects.create(name='Computer Science')

    def test_name_label(self):
        program = Program.objects.get(id=1)
        field_label = program._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        program = Program.objects.get(id=1)
        max_length = program._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        program = Program.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(program.get_absolute_url(), '/programs/1')



class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Program.objects.create(name='Computer Science')
        Course.objects.create(coursePrefix='CSCI', courseCode=101, coursePrefixAndCode='CSCI 101', program_id=1)

    def test_course_prefix_and_code_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('coursePrefixAndCode').verbose_name
        self.assertEqual(field_label, 'coursePrefixAndCode')

    def test_course_name_blank(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.courseName, '')

    def test_course_program(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.program.name, 'Computer Science')   
        
