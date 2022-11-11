from tkinter import ttk 
from tkinter import *

class usuario:
    def __init__(self, root):
        self.wind = root 
        self.wind.title("Login")
        self.wind.geometry("850x600")
        self.wind.config(bg="teal")

        frame1 = LabelFrame(self.wind, text="Nombre de Usuario", font=("calibri", 14))
        frame2 = LabelFrame(self.wind, text="Contraseña de Usuario", font=("calibri", 14))

        frame1.pack(fill="both", expand="yes", padx=20, pady=15)
        frame2.pack(fill="both", expand="yes", padx=20, pady=15)
        lbl1 = Label(frame1, text="ID del Usuario", width=20)
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        self.ent1 = Entry(frame1)
        self.ent1.grid(row=0, column=1, padx=5, pady=3)

       
        lbl2 = Label(frame1, text="Contraseña del Usuario", width=20)
        lbl2.grid(row=2, column=0, padx=5, pady=3)
        self.ent2 = Entry(frame1)
        self.ent2.grid(row=2, column=1, padx=5, pady=3)


if __name__=='__main__':
    root = Tk()
    usuario = usuario(root)
    root.mainloop()
