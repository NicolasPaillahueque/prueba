import unittest
from usuario import login
 
 
class Testlogin(unittest.TestCase):

    def test_login(self):
        self.assertEqual(login("usuario","123456"), "usuario", "123456")


if __name__ == '__main__':
    unittest.main()