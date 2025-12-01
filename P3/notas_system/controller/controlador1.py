from tkinter import messagebox
from model import usuario,nota
from view import view_1
class Controlador:
    @staticmethod
    def registro(nombre,apellidos,email,password,ventana):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info", message=f"{nombre} {apellidos} se registro correctamente con el email: {email}", title="Exito")
            view_1.View.login(ventana)
        else:
            messagebox.showwarning(icon="warning",message=f"Error al insertar en la base de datos", title="Error")

        


    @staticmethod
    def login(email,password, ventana):
        resultado=usuario.Usuario.iniciar_sesion(email,password)
        if resultado ==False:
            messagebox.showwarning(icon="warning",message=f"email o contraseña incorrectos", title="Error")
        else:
            messagebox.showinfo(icon="info", message=f"Bienvenido {resultado[1]} {resultado[2]}", title="Exito")
            view_1.View.Entrar(ventana,resultado[0],resultado[1],resultado[2])

    
