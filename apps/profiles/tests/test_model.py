from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):
    ''' Testea el modelo del usuario '''

    
    def test_create_user_with_email_successful(self):
        ''' Prueba que la creacion de un usuario sea exitosa '''
    
        payload = {
            'email': 'admin@gmail.com',
            'password': 'abc123/-',
            'name': 'Test',
            'last_name': 'User' 
        }    

        user = get_user_model().objects.create_user(
            email=payload.,
            password=payload.password,
            name=payload.name,
            last_name=payload.last_name
        )

        self.assertEqual(user.name, payload.name) # Pueba que el nombre guardado sea igual al proporcionado
        self.assertEqual(user.email, payload.email) # prueba que el email sea igual al proporcioado
        self.assertTrue(user.check_password(payload.password)) # Prueba que el pasword parseado sea igual al proporcionado
        self.assertEqual(user.last_name, payload.last_name) # Prueba que el last_name sea igual al prporcionado
    
    def test_new_user_email_normalized(self):
        pass