import tkinter as tk
import tkinter as tk
import tkinter.messagebox

class App:
    def __init__(self, master):
        self.master = master
        self.init_widgets()
    
    def init_widgets(self):
        # Crea una etiqueta para la fecha
        self.lbl_date = tk.Label(self.master, text="Fecha:")
        self.lbl_date.pack()
        
        # Crea una lista desplegable para seleccionar la fecha
        self.dates = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.selected_date = tk.StringVar()
        self.selected_date.set(self.dates[0])
        self.menu_date = tk.OptionMenu(self.master, self.selected_date, *self.dates)
        self.menu_date.pack()
        
        # Crea una etiqueta para la hora
        self.lbl_time = tk.Label(self.master, text="Hora:")
        self.lbl_time.pack()
        
        # Crea una lista desplegable para seleccionar la hora
        self.times = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"]
        self.selected_time = tk.StringVar()
        self.selected_time.set(self.times[0])
        self.menu_time = tk.OptionMenu(self.master, self.selected_time, *self.times)
        self.menu_time.pack()
        
        # Crea una etiqueta para el instructor
        self.lbl_instructor = tk.Label(self.master, text="Instructor:")
        self.lbl_instructor.pack()
        
        # Crea una lista desplegable para seleccionar el instructor
        self.instructors = ["Juan", "Pedro", "Ana", "Laura"]
        self.selected_instructor = tk.StringVar()
        self.selected_instructor.set(self.instructors[0])
        self.menu_instructor = tk.OptionMenu(self.master, self.selected_instructor, *self.instructors)
        self.menu_instructor.pack()
        
        # Crea un botón para registrar la clase
        self.btn_register = tk.Button(self.master, text="Registrar")
        self.btn_register.pack() 
        self.btn_register.place(x=100, y=200, height= 50, width= 100)
    

# Crea la ventana principal y la instancia de la aplicación
root = tk.Tk()
root.title("Registrar Horario")
root.geometry("300x300")
app = App(root)
root.mainloop()    
