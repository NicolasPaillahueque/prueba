from tkinter import *

ventana = Tk()


etiqueta_bienvenida = Label(ventana, text="Bienvenido a la interfaz de registro de clientes")
etiqueta_bienvenida.pack()

etiqueta_rut= Label(ventana, text="Ingrese Rut Cliente:")
etiqueta_rut.pack()
RUT = StringVar()
cuadro_RUT = Entry(ventana, textvariable=RUT)
cuadro_RUT.pack()


etiqueta_nombre = Label(ventana, text="Ingresa el nombre del cliente:")
etiqueta_nombre.pack()
nombre = StringVar()
cuadro_nombre = Entry(ventana, textvariable=nombre)
cuadro_nombre.pack()

etiqueta_APELLIDO = Label(ventana, text="Ingresa el apellido del cliente:")
etiqueta_APELLIDO.pack()
apellido = StringVar()
cuadro_apellido = Entry(ventana, textvariable=apellido)
cuadro_apellido.pack()


etiqueta_ciudad = Label(ventana, text="Ingresa la Ciudad del cliente:")
etiqueta_ciudad.pack()
ciudad = StringVar()
cuadro_ciudad = Entry(ventana, textvariable=ciudad)
cuadro_ciudad.pack()

etiqueta_telefono = Label(ventana, text="Ingresa el telefono del cliente:")
etiqueta_telefono.pack()
telefono = StringVar()
cuadro_telefono = Entry(ventana, textvariable=telefono)
cuadro_telefono.pack()

etiqueta_correo = Label(ventana, text="Ingresa el correo electrónico del cliente:")
etiqueta_correo.pack()
correo = StringVar()
cuadro_correo = Entry(ventana, textvariable=correo)
cuadro_correo.pack()

# Creamos un botón para registrar al cliente
boton_registrar = Button(ventana, text="Registrar")
boton_registrar.pack()

# Ejecutamos el bucle principal de la ventana
ventana.mainloop()