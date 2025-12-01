from view import view1
from P3.coches_system.model import modelo1
from tkinter import messagebox
from tkinter import *




class Controlador:
    @staticmethod
    def coñete(respuesta):
        if respuesta:
            messagebox.showinfo(message=f"GG")
            return True
        else:
            messagebox.showinfo(message=f"FF")


    @staticmethod
    def insertar_coches(id,marca,color,modelo,velocidad,caballaje,plazas):
        respuesta=modelo1.Coches.insertar(id,marca,color,modelo,velocidad,caballaje,plazas)
        Controlador.coñete(respuesta)

    @staticmethod
    def consultar_coches():
        respuesta=modelo1.Coches.consultar()


    @staticmethod
    def cambiar_coches(id,marca,color,modelo,velocidad,caballaje,plazas):
        respuesta=modelo1.Coches.actualizar(id,marca,color,modelo,velocidad,caballaje,plazas)
        Controlador.coñete(respuesta)


    @staticmethod
    def eliminar_coches(id):
        respuesta=modelo1.Coches.eliminar(id)
        Controlador.coñete(respuesta)


    @staticmethod
    def check(id,ventana):
        respuesta=modelo1.Coches.check(id)     
        if respuesta:
            messagebox.showinfo(message=f"Pasa")
            view1.View.actualizar_autos2(ventana,respuesta[0],respuesta[2],respuesta[3],respuesta[4],respuesta[5])
        else:
            messagebox.showinfo(message=f"No pasa pa")