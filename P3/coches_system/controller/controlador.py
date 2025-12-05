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

class Controlador2:
    @staticmethod
    def coñete(respuesta):
        if respuesta:
            messagebox.showinfo(message=f"Accion realizada con exito")
            return True
        else:
            messagebox.showinfo(message=f"Algo salio mal..")


    @staticmethod
    def insertar_camionetas(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        respuesta=modelo1.Camionetas.insertar(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        Controlador2.coñete(respuesta)

    @staticmethod
    def consultar_camionetas():
        respuesta=modelo1.Camionetas.consultar()
        return respuesta


    @staticmethod
    def cambiar_camionetas(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada,id):
        respuesta=modelo1.Camionetas.actualizar(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
        Controlador2.coñete(respuesta)


    @staticmethod
    def eliminar_camionetas(id):
        confirmar = messagebox.askyesno(
        "Confirmar eliminación",
        "¿Estás seguro de que deseas eliminar esta camioneta?"
        )
        if confirmar:   # Si el usuario presiona YES
            respuesta = modelo1.Camionetas.eliminar(id)
            Controlador2.coñete(respuesta)
        else:
            # Puedes poner algo opcional, como un mensaje o nada
            messagebox.showinfo("Cancelado", "La eliminación ha sido cancelada.")
    
    @staticmethod
    def check_camionetas(ventana,tipo,id):
        respuesta=modelo1.Camionetas.check(id)    
        messagebox.showinfo(message=f"{respuesta}") 
        if respuesta:
            messagebox.showinfo(message=f"Pasa")
            view1.View.cambiar_camionetas2(ventana,tipo,respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6],respuesta[7],respuesta[8])
        else:
            messagebox.showinfo(message=f"No pasa pa")

    @staticmethod
    def check_camionetas2(ventana,tipo,id):
        respuesta=modelo1.Camionetas.check(id)     
        messagebox.showinfo(message=f"{respuesta}") 
        if respuesta:
            messagebox.showinfo(message=f"Pasa")
            view1.View.eliminar_camionetas2(ventana,tipo,respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6],respuesta[7],respuesta[8])
        else:
            messagebox.showinfo(message=f"No pasa pa")
class Controlador3:
    @staticmethod
    def coñete(respuesta):
        if respuesta:
            messagebox.showinfo(message=f"Accion realizada con exito")
            return True
        else:
            messagebox.showinfo(message=f"Algo salio mal..")


    @staticmethod
    def insertar_camiones(color,marca,modelo,velocidad,caballaje,plazas,eje,carga):
        respuesta=modelo1.Camiones.insertar(color,marca,modelo,velocidad,caballaje,plazas,eje,carga)
        Controlador2.coñete(respuesta)

    @staticmethod
    def consultar_camiones():
        respuesta=modelo1.Camiones.consultar()
        return respuesta


    @staticmethod
    def cambiar_camiones(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada,id):
        respuesta=modelo1.Camiones.actualizar(color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
        Controlador2.coñete(respuesta)


    @staticmethod
    def eliminar_camiones(id):
        confirmar = messagebox.askyesno(
        "Confirmar eliminación",
        "¿Estás seguro de que deseas eliminar esta camioneta?"
        )
        if confirmar:   # Si el usuario presiona YES
            respuesta = modelo1.Camiones.eliminar(id)
            Controlador2.coñete(respuesta)
        else:
            # Puedes poner algo opcional, como un mensaje o nada
            messagebox.showinfo("Cancelado", "La eliminación ha sido cancelada.")
    
    @staticmethod
    def check_camiones(ventana,tipo,id):
        respuesta=modelo1.Camiones.check(id)    
        messagebox.showinfo(message=f"{respuesta}") 
        if respuesta:
            messagebox.showinfo(message=f"Pasa")
            view1.View.cambiar_camiones2(ventana,tipo,respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6],respuesta[7],respuesta[8])
        else:
            messagebox.showinfo(message=f"No pasa pa")

    @staticmethod
    def check_camiones2(ventana,tipo,id):
        respuesta=modelo1.Camiones.check(id)     
        messagebox.showinfo(message=f"{respuesta}") 
        if respuesta:
            messagebox.showinfo(message=f"Pasa")
            view1.View.eliminar_camiones2(ventana,tipo,respuesta[0],respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[5],respuesta[6],respuesta[7],respuesta[8])
        else:
            messagebox.showinfo(message=f"No pasa pa")