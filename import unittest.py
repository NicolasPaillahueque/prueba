import unittest
from Interfaz_Usuario import ingresar

class   testinterfaz(unittest.TestCase):
    
    def test_loggin(self):
        self.assertEqual(ingresar("programador","123456"), "programador", "123456")
        
if __name__ == '__main__':
    unittest.main()