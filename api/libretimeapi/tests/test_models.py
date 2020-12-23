from django.test import TestCase
from libretimeapi.models import User, DJ


class TestUserManager(TestCase):
    def test_create_user(self):
        user = User.objects.create_user('test',
                                        email='test@example.com',
                                        password='test',
                                        type=DJ,
                                        first_name='test',
                                        last_name='user')
        db_user = User.objects.get(pk=user.pk)
        self.assertEqual(db_user.username, user.username)

    def test_create_superuser(self):
        user = User.objects.create_superuser('test',
                                             email='test@example.com',
                                             password='test',
                                             first_name='test',
                                             last_name='user')
        db_user = User.objects.get(pk=user.pk)
        self.assertEqual(db_user.username, user.username)

