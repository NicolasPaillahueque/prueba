import tkinter as tk


ventana = tk.Tk()
ventana.title("Membresías del gimnasio")
ventana.geometry("400x400")

membresias = {
    "Mensual": (30, 50),
    "Trimestral": (90, 120),
    "Semestral": (180, 200),
    "Anual": (365, 300),
}

def mostrar_detalles():
    membresia_seleccionada = membresia_seleccionada_entry.get()
    if membresia_seleccionada in membresias:
        duracion, costo = membresias[membresia_seleccionada]
        detalles_texto = f"Duración: {duracion} días\nCosto: ${costo}"
        detalles_label.config(text=detalles_texto)
    else:
        detalles_label.config(text="Membresía no válida")

# Crear la lista desplegable de membresías
membresia_seleccionada_entry = tk.StringVar(ventana)
membresia_seleccionada_entry.set("Seleccione una membresía")
opciones_membresias = tk.OptionMenu(ventana, membresia_seleccionada_entry, *membresias.keys())
opciones_membresias.pack()

# Crear una etiqueta para mostrar los detalles de la membresía seleccionada
detalles_label = tk.Label(ventana, text="")
detalles_label.pack()

membresia_seleccionada_entry.trace("w", mostrar_detalles)
