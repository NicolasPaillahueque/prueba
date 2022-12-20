import unittest
from tkinter import Tk, Button

class TestButton(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.button = Button(self.root, text="Click me")
        self.button.pack()

    def test_button_click(self):
        def callback():
            self.button["text"] = "Clicked"

        self.button["command"] = callback
        self.button.invoke()

        self.assertEqual(self.button["text"], "Clicked")

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
