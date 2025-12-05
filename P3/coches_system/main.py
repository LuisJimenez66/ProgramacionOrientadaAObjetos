'''
Diciembre 1
    1)Implementacion de MVC
    2)POO
    3)Interfaces:
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()
        3.4 consultar_autos()
        3.5 cambiar_autos()
        3.6 borrar_autos()

Productos entregarbles:
    Estructura del proyecto basado en MVC
    Modulo principal "main"
    Interaccion con las interfaces 
    Nombre del commit: "commit_01_12_25"

Diciembre 2
    1) Interfaces:
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()
        2.1 insertar_camiones()
        2.2 consultar_camiones()
        2.3 cambiar_camiones()
        2.4 borrar_camiones()    

    Productos entregables: 
        Interaccion con todas las interfaces
        nombre del commit: commit_02_12_25


Diciembre 3
    1) Controlador:
        1.1 menu_principal()
        1.2 menu_acciones()
        1.3 insertar_autos()
        1.4 consultar_autos()
        1.5 cambiar_autos()
        1.6 borrar_autos()

    Productos entregables:
        Interaccion con la funcionalidad (controlador) de las interfaces anteriores
        Nombre del Commit: "commit_03_12_25"      

Diciembre 4
    1) Controlador:
    1.1 insertar_camionetas()
    1.2 consultar_camionetas()
    1.3 cambiar_camionetas()
    1.4 borrar_camionetas()  

    Productos entregables:
        Interaccion con la funcionalidad (controlador) de las interfaces anteriores
        Nombre del Commit: "commit_04_12_25"        

Diciembre 5
    1) Controlador:
    1.1 insertar_camiones()
    1.2 consultar_camiones()
    1.3 cambiar_camiones()
    1.4 borrar_camiones()  

    Productos entregables:
        Interaccion con la funcionalidad (controlador) de las interfaces anteriores
        Nombre del Commit: "commit_05_12_25"        

'''
from tkinter import *
from view import view1
  
class App:
    @staticmethod
    def main (ventana):
        view=view1.View(ventana)


if __name__=="__main__":
    ventana=Tk()
    App.main(ventana)
    ventana.mainloop()