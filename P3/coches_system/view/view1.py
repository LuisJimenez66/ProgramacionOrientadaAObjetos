from tkinter import *
from tkinter import messagebox
class View():
    def __init__(self,ventana):
        ventana.title("Coches system")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrar_pantalla(ventana):
        for i in ventana.winfo_children():
            i.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text="Bienvenido a cohes system")
        lbl_titulo.pack(pady=10)
        btn_coches=Button(ventana, text="Coches", command=lambda:View.menu_acciones(ventana,"Coches"))    
        btn_coches.pack(pady=5)
        btn_camionetas=Button(ventana, text="Camionetas", command=lambda:View.menu_acciones(ventana,"Camionetas")) 
        btn_camionetas.pack(pady=5)
        btn_camiones=Button(ventana, text="Camiones", command=lambda:View.menu_acciones(ventana,"Camiones")) 
        btn_camiones.pack(pady=5)
        btn_salir=Button(ventana, text="Salir", command=ventana.destroy)
        btn_salir.pack(pady=5)

    @staticmethod
    def menu_acciones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido al menu de {tipo}")
        lbl_titulo.pack(pady=10)
        btn_insertar=Button(ventana, text="Insertar", command=lambda:View.insertar_coches(ventana,tipo))    
        btn_insertar.pack(pady=5)
        btn_mostrar=Button(ventana, text="Mostrar", command=lambda:View.consultar_autos(ventana,tipo)) 
        btn_mostrar.pack(pady=5)
        btn_Modificar=Button(ventana, text="Modificar", command=lambda:View.cambiar_autos(ventana,tipo)) 
        btn_Modificar.pack(pady=5)   
        btn_Eliminar=Button(ventana, text="Eliminar", command=lambda:View.eliminar_autos(ventana,tipo)) 
        btn_Eliminar.pack(pady=5)   
        btn_volver=Button(ventana, text="Regresar", command=lambda:View.menu_principal(ventana)) 
        btn_volver.pack(pady=5)  

    def insertar_coches(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a insertar {tipo}")
        lbl_titulo.pack(pady=10)

        lbl_marca=Label(ventana,text="Ingresa la marca")
        lbl_marca.pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Ingresa la color")
        lbl_color.pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Ingresa la velocidad")
        lbl_velocidad.pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caba=Label(ventana,text="Ingresa la caballaje")
        lbl_caba.pack(pady=5)
        txt_caba=Entry(ventana)
        txt_caba.pack(pady=5)

        lbl_plazas=Label(ventana,text="Ingresa el no de plazas")
        lbl_plazas.pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)

        if tipo=="Camionetas":
            lbl_traccion=Label(ventana,text="Ingresa la traccion")
            lbl_traccion.pack(pady=5)
            txt_traccion=Entry(ventana)
            txt_traccion.pack(pady=5)

            lbl_plazas=Label(ventana,text="Selecciona una opcion")
            lbl_plazas.pack(pady=5)
            opcion = StringVar()
            opcion1 = Radiobutton(ventana,text="Cerrada",variable=opcion,value="Cerrada")
            opcion1.pack()
            opcion2 = Radiobutton(ventana,text="Abierta",variable=opcion,value="Abierta")
            opcion2.pack()
            bnt_insertar_camionetas=Button(ventana,text="Insertar")
            bnt_insertar_camionetas.pack(pady=5)
        elif tipo=="Camiones":
            lbl_eje=Label(ventana,text="Ingresa el eje")
            lbl_eje.pack(pady=5)
            txt_eje=Entry(ventana)
            txt_eje.pack(pady=5)

            lbl_carga=Label(ventana,text="Ingresa la capacidad de carga")
            lbl_carga.pack(pady=5)
            txt_carga=Entry(ventana)
            txt_carga.pack(pady=5)

            bnt_insertar_camiones=Button(ventana,text="Insertar")
            bnt_insertar_camiones.pack(pady=5)

        else:
            bnt_insertar_coches=Button(ventana,text="Insertar")
            bnt_insertar_coches.pack(pady=5)    
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5)   

    @staticmethod
    def consultar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a consultar coches"))
        lbl_titulo.pack(pady=5) 
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a cambiar coches"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del coche a cambiar"))
        lbl_id.pack(pady=5)     
        txt_id=Entry(ventana)
        txt_id.pack()
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    @staticmethod
    def eliminar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a eliminar coches"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del coche a eliminar"))
        lbl_id.pack(pady=5) 
        txt_id=Entry(ventana)
        txt_id.pack()          
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

        

