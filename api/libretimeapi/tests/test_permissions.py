from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from django.test import TestCase, Client, RequestFactory
from libretimeapi.permissions import IsSystemTokenOrUser
from libretimeapi.models import DJ

class TestIsSystemTokenOrUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.path = "/api/v2/files/"
        cls.client = Client()

    def test_unauthorized(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 403)

    def test_user_logged_in(self):
        user = get_user_model().objects.create_user('test',
                                                    email='test@example.com',
                                                    password='test',
                                                    type=DJ,
                                                    first_name='test',
                                                    last_name='user')
        self.client.login(username='test', password='test')
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

    def test_token_incorrect(self):
        token = 'doesnotexist'
        request = RequestFactory().get(self.path)
        request.user = AnonymousUser()
        request.META['Authorization'] = f'Api-Key {token}'
        allowed = IsSystemTokenOrUser().has_permission(request, None)
        self.assertFalse(allowed)

    def test_token_correct(self):
        token = settings.CONFIG.get('general', 'api_key')
        request = RequestFactory().get(self.path)
        request.user = AnonymousUser()
        request.META['Authorization'] = f'Api-Key {token}'
        allowed = IsSystemTokenOrUser().has_permission(request, None)
        self.assertTrue(allowed)

