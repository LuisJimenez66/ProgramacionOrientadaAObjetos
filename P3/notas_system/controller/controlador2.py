from tkinter import messagebox
from model import nota
from view import view_1

class ControladorNotas:

    @staticmethod
    def resp(respuesta):
        if respuesta:
            messagebox.showinfo(message=f"GG")
        else:
            messagebox.showinfo(message=f"FF")

    @staticmethod
    def insertar(usuario_id,titulo,descripcion):
        resultado=nota.Nota.crear(usuario_id,titulo,descripcion)
        ControladorNotas.resp(resultado)

    @staticmethod
    def mostrar(usuario_id):
        resultado=nota.Nota.mostrar(usuario_id)

        res=""
        for i in resultado:
            res=res+f"{i[0]:<10}{i[1]}{i[2]:>7}{i[4]:>9}{i[3]:>10}\n" 
            return res

    @staticmethod
    def cambiar(id_nota,titulo,descripcion):
        resultado=nota.Nota.actualizar(id_nota,titulo,descripcion)   
        ControladorNotas.resp(resultado)     

    @staticmethod
    def eliminar(id_nota):
        resultado=nota.Nota.eliminar(id_nota)   
        ControladorNotas.resp(resultado) 