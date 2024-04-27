from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from lecNotes_app.models import Program, Course, Lecturer, LectureNotes, NotesAuthor
from lecNotes_app.views import index, create_lecNotes, create_course

class ProgramViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data here
        cls.program = Program.objects.create(name="Test Program")

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lecNotes_app/index.html')


class LectureNotesViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data for lectures, courses, and lecturers
        cls.program = Program.objects.create(name="Test Program")
        cls.course = Course.objects.create(coursePrefix="CS", courseCode=101, courseName="Test Course", program=cls.program)
        cls.lecturer = Lecturer.objects.create(name="Test Lecturer")
        cls.lecture_note = LectureNotes.objects.create(coursePrefix="CS", courseCode=101, courseName="Test Course", lectureDate="2024-04-26", lectureNum=1, lecturer=cls.lecturer, course=cls.course)

    def test_create_lecNotes_view_get(self):
        # Test GET request to create_lecNotes view
        response = self.client.get(reverse('create_lecNotes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lecNotes_app/create_lecNotes.html')



    
