from tkinter import ttk 
from tkinter import *

root=Tk()
root.title("Login")
root.geometry("300x150")
root.resizable(width=False, height=False)
root.config(bg="Blue")

usuario=Label(root, text="Ingrese nombre de usuario:")
usuario.pack()

usuario1=StringVar()
usu=Entry(root, width=30, textvariable=usuario1)
usu.pack()

contraseña=Label(root, text="Contraseña:")
contraseña.pack()

contra=StringVar()
contra1=Entry(root, width=30, textvariable=contra, show="*")
contra1.pack()

def ingresar():
    if usuario1.get()=="programador" and contra.get()=="123456":
        root.title("Correcto")
    else:
        root.title("Incorrecto")

bt=Button(root, text="Entrar", command=ingresar)
bt.pack(side=BOTTOM)


root.mainloop()