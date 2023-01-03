import unittest
from usuario import login
 
 
class Testlogin(unittest.TestCase):

    def test_login(self):
        self.assertTrue(login("programador","123456"))

    def test_login_contraseña_incorrecta(self):
        self.assertFalse(login('usuario', '1234567'))

    def test_login_wrong_username(self):
        self.assertFalse(login('juna', '123456'))    


if __name__ == '__main__':
    unittest.main()
