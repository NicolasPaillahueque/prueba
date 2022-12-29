import tkinter as tk

ventana = tk.Tk()
ventana.title("Reserva de horas de gimnasio")
ventana.geometry("400x400")

profesores = {
    "Juan": ["Lunes 10:00-12:00", "Martes 16:00-18:00"],
    "Ana": ["Miércoles 10:00-12:00", "Jueves 16:00-18:00"],
    "Pablo": ["Viernes 10:00-12:00", "Sábado 16:00-18:00"],
}


profesor_seleccionado = tk.StringVar(ventana)
profesor_seleccionado.set("Seleccione un profesor")
opciones_profesores = tk.OptionMenu(ventana, profesor_seleccionado, *profesores.keys())
opciones_profesores.pack()



etiqueta_horarios = tk.Label(ventana, text="Horarios disponibles:")
opciones_horarios = tk.OptionMenu(ventana, profesor_seleccionado, *profesores.keys())
etiqueta_horarios.pack()
