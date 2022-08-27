import email
from rest_framework.test import APITestCase
from authentication.models import User 

class TestModel(APITestCase):
    
    def test_create_user(self):
        user = User.objects.create_user('cryce','crycetruly@gmail.com','password123!@')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'crycetruly@gmail.com')

    def test_create_super_user(self):
        user = User.objects.create_user('cryce','crycetruly@gmail.com','password123!@')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'crycetruly@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="",email = 'crycetruly@gmail.com',password = 'password123!@')

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError,'The given username must be set'):
            User.objects.create_user(username='',email='crycetruly@gmail.com', password = 'password@1')
        # with.self.assertRaisesMessage(ValueError,)
        self.assertRaises(ValueError,User.objects.create_user,username="notset",email = "",password = 'password123!@')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="fldskjflk",email = '',password = 'password123!@')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError,'The given email must be set'):
            User.objects.create_user(username='crycetruly@gmail.com',email='', password = 'password@1')
        # with.self.assertRaisesMessage(ValueError,)
        # self.assertRaises(ValueError,User.objects.create_user,username="notset",email = "",password = 'password123!@')

    def test_creates_superuser_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='crycetruly@gmail.com',email='sdfds@gmail.com', password = 'password@1',is_staff=False)
    
    def test_creates_superuser_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='crycetruly@gmail.com',email='sdfds@gmail.com', password = 'password@1',is_superuser=False)

        # user = User.objects.create_user(username = 'cryce',)
        # self.assertIsInstance(user, User)
        # self.assertFalse(user.is_staff)
        # self.assertEqual(user.email, 'crycetruly@gmail.com')

