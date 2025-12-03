from view import view1
from model import modelo1
from tkinter import messagebox
from tkinter import *




class Controlador:
    @staticmethod
    def coñete(respuesta):
        if respuesta:
            messagebox.showinfo(message=f"Accion realizada con exito")
            return True
        else:
            messagebox.showinfo(message=f"Algo salio mal..")


    @staticmethod
    def insertar_coches(color,marca,modelo,velocidad,caballaje,plazas):
        respuesta=modelo1.Coches.insertar(color,marca,modelo,velocidad,caballaje,plazas)
        Controlador.coñete(respuesta)

    @staticmethod
    def consultar_coches():
        respuesta=modelo1.Coches.consultar()
        return respuesta


    @staticmethod
    def cambiar_coches(color,marca,modelo,velocidad,caballaje,plazas,id):
        respuesta=modelo1.Coches.actualizar(color,marca,modelo,velocidad,caballaje,plazas,id)
        Controlador.coñete(respuesta)


    @staticmethod
    def eliminar_coches(id):
        respuesta=modelo1.Coches.eliminar(id)
        Controlador.coñete(respuesta)


    @staticmethod
    def check_coches(ventana,tipo,id):
        respuesta=modelo1.Coches.check(id)    
        messagebox.showinfo(message=f"{respuesta}") 
        if respuesta:
            messagebox.showinfo(message=f"Pasa")
            view1.View.cambiar_autos2(ventana,tipo,respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6])
        else:
            messagebox.showinfo(message=f"No pasa pa")

    @staticmethod
    def check_coches2(ventana,tipo,id):
        respuesta=modelo1.Coches.check(id)     
        messagebox.showinfo(message=f"{respuesta}") 
        if respuesta:
            messagebox.showinfo(message=f"Pasa")
            view1.View.eliminar_autos2(ventana,tipo,respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6])
        else:
            messagebox.showinfo(message=f"No pasa pa")        