from django.test import TestCase
from lecNotes_app.forms import CreateUserForm, LecNotesForm
from django.contrib.auth.models import User
from lecNotes_app.models import Course, Lecturer, LectureNotes, Program

# Create your tests here.
class CreateUserFormTest(TestCase):
    def test_create_user_form_valid(self):
        form = CreateUserForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertTrue(form.is_valid())

    def test_create_user_form_invalid(self):
        form = CreateUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class LecNotesFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data for courses and lecturers
        cls.program = Program.objects.create(name="Test Program")
        cls.course = Course.objects.create(coursePrefix="CS", courseCode=101, courseName="Test Course", program=cls.program)
        cls.lecturer = Lecturer.objects.create(name="Test Lecturer")

    def test_lecNotes_form_valid(self):
        form = LecNotesForm(data={
            'lectureNum': 1,
            'lectureDate': '2024-04-26',
            'existing_course': self.course.id,
            'existing_lecturer': self.lecturer.id
        })
        self.assertTrue(form.is_valid())

    def test_lecNotes_form_invalid(self):
        form = LecNotesForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
