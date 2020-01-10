from django.test import SimpleTestCase, TestCase, Client
from django.urls import resolve, reverse
from scholarship.views import index, scholarshipview, success, error
from scholarship.models import Scholarship
from django.contrib.auth.models import User

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_index_url_resolve(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_form_url_resolve(self):
        url = reverse('form')
        self.assertEqual(resolve(url).func, scholarshipview)

    def test_success_url_resolve(self):
        url = reverse('success')
        self.assertEqual(resolve(url).func, success)

    def test_error_url_resolve(self):
        url = reverse('error')
        self.assertEqual(resolve(url).func, error)


class TestModels(TestCase):
    def setUp(self) -> None:
        self.project = User.objects.create_user(
            username='myUsername',
            email='myname@asas.com',
            password="testpassword"
        )
        self.scholarship1 = Scholarship.objects.all()

    def test_scholarship_object_created(self):
        self.assertEqual(len(self.scholarship1), 1)


class TestViews(TestCase):
    def test_scholarshipview(self):
        client = Client()

        response = client.get(reverse('form'))

        self.assertEqual(response.status_code, 200)

