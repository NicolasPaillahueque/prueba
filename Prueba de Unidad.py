import unittest

def ingresar(usuario1, contra):
    if usuario1.get()=="programador" and contra.get()=="123456":
        root.title("Correcto")
    else:
        root.title("Incorrecto")

class TestIngresar(unittest.TestCase):
    def test_ingresar_con_credenciales_validas(self):
        usuario1 = "programador"
        contra = "123456"
        ingresar(usuario1, contra)
        self.assertEqual(root.title, "Correcto")

    def test_ingresar_con_credenciales_invalidas(self):
        usuario1 = "usuario123"
        contra = "contrasena123"
        ingresar(usuario1, contra)
        self.assertEqual(root.title, "Incorrecto")

if __name__ == '__main__':
    unittest.main()

