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
        if tipo=="Coches":
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
        elif tipo=="Camiones":
            lbl_titulo=Label(ventana, text=f"Bienvenido al menu de {tipo}")
            lbl_titulo.pack(pady=10)
            btn_insertar=Button(ventana, text="Insertar", command=lambda:View.insertar_camiones(ventana,tipo))    
            btn_insertar.pack(pady=5)
            btn_mostrar=Button(ventana, text="Mostrar", command=lambda:View.consultar_camiones(ventana,tipo)) 
            btn_mostrar.pack(pady=5)
            btn_Modificar=Button(ventana, text="Modificar", command=lambda:View.cambiar_camiones(ventana,tipo)) 
            btn_Modificar.pack(pady=5)   
            btn_Eliminar=Button(ventana, text="Eliminar", command=lambda:View.eliminar_camiones(ventana,tipo)) 
            btn_Eliminar.pack(pady=5)   
            btn_volver=Button(ventana, text="Regresar", command=lambda:View.menu_principal(ventana))
            btn_volver.pack(pady=5)  
        elif tipo=="Camionetas":
            lbl_titulo=Label(ventana, text=f"Bienvenido al menu de {tipo}")
            lbl_titulo.pack(pady=10)
            btn_insertar=Button(ventana, text="Insertar", command=lambda:View.insertar_camionetas(ventana,tipo))    
            btn_insertar.pack(pady=5)
            btn_mostrar=Button(ventana, text="Mostrar", command=lambda:View.consultar_camionetas(ventana,tipo)) 
            btn_mostrar.pack(pady=5)
            btn_Modificar=Button(ventana, text="Modificar", command=lambda:View.cambiar_camionetas(ventana,tipo)) 
            btn_Modificar.pack(pady=5)   
            btn_Eliminar=Button(ventana, text="Eliminar", command=lambda:View.eliminar_camionetas(ventana,tipo)) 
            btn_Eliminar.pack(pady=5)   
            btn_volver=Button(ventana, text="Regresar", command=lambda:View.menu_principal(ventana))    
            btn_volver.pack(pady=5)        

    @staticmethod
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
        btn_insertar=Button(ventana,text="Insertar") 
        btn_insertar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5)   

    @staticmethod
    def consultar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a consultar coches"))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=[("1","Sida","Negro","2002","120","100","2")]
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nAuto: {num_nota} \n ID: {i[0]} -Marca: {i[1]} Color: {i[2]} Modelo: {i[3]} \n Velocidad: {i[4]} Caballaje: {i[5]} Plazas: {i[6]}\n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay coches registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a cambiar coches"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del coche a cambiar"))
        lbl_id.pack(pady=5)     
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()
        btn_buscar=Button(ventana,text="Buscar", command=lambda:View.cambiar_autos2(ventana,tipo)) 
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_autos2(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a actualizar {tipo}")
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
        btn_actualizar=Button(ventana,text="Actualizar") 
        btn_actualizar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.cambiar_autos(ventana,tipo)) 
        btn_volver.pack(pady=5)

    @staticmethod
    def eliminar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a eliminar coches"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del coche a eliminar"))
        id=IntVar()
        lbl_id.pack(pady=5) 
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()          
        btn_buscar=Button(ventana,text="Buscar", command=lambda:View.eliminar_autos2(ventana,tipo)) 
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    def eliminar_autos2(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Coche a eliminar: "))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=[("1","Sida","Negro","2002","120","100","2")]
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nAuto: {num_nota} \n ID: {i[0]} -Marca: {i[1]} Color: {i[2]} Modelo: {i[3]} \n Velocidad: {i[4]} Caballaje: {i[5]} Plazas: {i[6]}\n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay coches registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_borrar=Button(ventana,text="Borrar") 
        btn_borrar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.eliminar_autos(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    @staticmethod
    def insertar_camionetas(ventana,tipo):
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
            
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5)   

    @staticmethod
    def consultar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a consultar camionetas"))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=[("1","Tupac","Negro","2025","120","150","6","Trasera","Cerrada")]
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nCamioneta: {num_nota} \n ID: {i[0]} -Marca: {i[1]} Color: {i[2]} Modelo: {i[3]}  Velocidad: {i[4]} \nCaballaje: {i[5]} Plazas: {i[6]} Traccion: {i[7]} Cerrada: {i[8]} \n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay coches registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a cambiar camionetas"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id de la camioneta a cambiar"))
        id=IntVar()
        lbl_id.pack(pady=5)     
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()
        btn_buscar=Button(ventana,text="Buscar", command=lambda:View.cambiar_camionetas2(ventana,tipo)) 
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_camionetas2(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a actualizar {tipo}")
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
        btn_actualizar=Button(ventana,text="Actualizar") 
        btn_actualizar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.cambiar_camionetas(ventana,tipo)) 
        btn_volver.pack(pady=5)   
     
    @staticmethod
    def eliminar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a eliminar camionetas"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id de la camioneta a eliminar"))
        lbl_id.pack(pady=5) 
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()          
        btn_buscar=Button(ventana,text="Buscar", command=lambda:View.eliminar_camionetas2(ventana,tipo)) 
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    def eliminar_camionetas2(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Camioneta a eliminar"))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=[("1","Tupac","Negro","2025","120","150","6","Trasera","Cerrada")]
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nCamioneta: {num_nota} \n ID: {i[0]} -Marca: {i[1]} Color: {i[2]} Modelo: {i[3]}  Velocidad: {i[4]} \nCaballaje: {i[5]} Plazas: {i[6]} Traccion: {i[7]} Cerrada: {i[8]} \n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay coches registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_borrar=Button(ventana,text="Borrar") 
        btn_borrar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.eliminar_camionetas(ventana,tipo)) 
        btn_volver.pack(pady=5)

    @staticmethod
    def insertar_camiones(ventana,tipo):
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

        if tipo=="Camiones":
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
    
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5)   

    @staticmethod
    def consultar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a consultar camiones"))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=[("1","Tron","Blanco","2020","120","150","6","4","2000")]
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nCamioneta: {num_nota} \n ID: {i[0]} -Marca: {i[1]} Color: {i[2]} Modelo: {i[3]}  Velocidad: {i[4]} \nCaballaje: {i[5]} Plazas: {i[6]} Eje: {i[7]} Capacidad de carga: {i[8]} \n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay coches registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a cambiar camiones"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del camion a cambiar"))
        lbl_id.pack(pady=5)     
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()
        btn_buscar=Button(ventana,text="buscar", command=lambda:View.cambiar_camiones2(ventana,tipo)) 
        btn_buscar.pack(pady=5) 
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    @staticmethod
    def cambiar_camiones2(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a actualizar {tipo}")
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

        if tipo=="Camiones":
            lbl_eje=Label(ventana,text="Ingresa el eje")
            lbl_eje.pack(pady=5)
            txt_eje=Entry(ventana)
            txt_eje.pack(pady=5)

            lbl_carga=Label(ventana,text="Ingresa la capacidad de carga")
            lbl_carga.pack(pady=5)
            txt_carga=Entry(ventana)
            txt_carga.pack(pady=5)
        btn_actualizar=Button(ventana,text="Actualizar") 
        btn_actualizar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.cambiar_camiones(ventana,tipo)) 
        btn_volver.pack(pady=5)


    @staticmethod
    def eliminar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a eliminar camiones"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del camion a eliminar"))
        lbl_id.pack(pady=5) 
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()          
        btn_buscar=Button(ventana,text="buscar", command=lambda:View.eliminar_camiones2(ventana,tipo)) 
        btn_buscar.pack(pady=5) 
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    @staticmethod
    def eliminar_camiones2(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Camion a eliminar:"))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=[("1","Tron","Blanco","2020","120","150","6","4","2000")]
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nCamioneta: {num_nota} \n ID: {i[0]} -Marca: {i[1]} Color: {i[2]} Modelo: {i[3]}  Velocidad: {i[4]} \nCaballaje: {i[5]} Plazas: {i[6]} Eje: {i[7]} Capacidad de carga: {i[8]} \n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay coches registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_borrar=Button(ventana,text="Borrar") 
        btn_borrar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 
