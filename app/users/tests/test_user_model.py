from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTest(TestCase):

    def test_user_created(self):
        email = 'leandro@gmail.com'
        password = '12345678'
        name = 'Leandro'

        user = get_user_model().objects.create_user(
            email=email,
            name='Leandro',
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        email = 'leandro@GMAIL.com'
        password = '12345678'
        name = 'Leandro'

        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_user_invalid_name(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='leandro@gmail.com', name=None, password='test123')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'leandro@gmail.com'
            '12345678'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
