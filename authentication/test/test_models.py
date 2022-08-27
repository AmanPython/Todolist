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
        with self.assertRaisesMessage(ValueError,'The given email must be set'):
            User.objects.create_user(username='',email='crycetruly@gmail.com', password = 'password@1')
        # with.self.assertRaisesMessage(ValueError,)
        self.assertRaises(ValueError,User.objects.create_user,username="notset",email = "",password = 'password123!@')


    

        # user = User.objects.create_user(username = 'cryce',)
        # self.assertIsInstance(user, User)
        # self.assertFalse(user.is_staff)
        # self.assertEqual(user.email, 'crycetruly@gmail.com')

