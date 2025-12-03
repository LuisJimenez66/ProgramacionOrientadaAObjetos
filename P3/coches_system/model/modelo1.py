from conexionBD import *
class Coches:
    @staticmethod
    def insertar(color,marca,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute(
                "insert into coches values(null,%s,%s,%s,%s,%s,%s)",
                (color,marca,modelo,velocidad,caballaje,plazas)
            )
            conexion.commit()
            return True
        except:  
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from coches")   
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def actualizar(color,marca,modelo,velocidad,caballaje,plazas, id_coche):
        try:
            cursor.execute(
                "update coches set color=%s, marca=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s where id_coches=%s",
                (color, marca, modelo, velocidad, caballaje, plazas, id_coche)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id_coche):
        try:
            cursor.execute("delete from coches where id_coches=%s", (id_coche,))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def check(id):
        try:
            cursor.execute(
                "select * from coches where id_coches=%s",(id,)
            )
            return cursor.fetchone()
        except:
            return False    

class Camionetas:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        try:
            cursor.execute(
                "insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from camionetas")
            
            return cursor.fetchall()
        except:
            print("\n\t..::No hay autos registrados::..")
            return []
        
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas, traccion, cerrada, id_camioneta):
        try:
            cursor.execute(
                "update camionetas set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s,traccion=%s, cerrada=%s where id_camioneta=%s",
                (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta)
            )
            conexion.commit()
            return True
        except:
            print("\t\n..::No se pudo actualizar::..")
            return False
        
    @staticmethod
    def eliminar(id_camioneta):
        try:
            cursor.execute("delete from camionetas where id_camioneta=%s", (id_camioneta,))
            conexion.commit()
            return True
        except:
            print("\n\t..:: No se pudo elmiminar ::..")
            return False
        
    @staticmethod
    def check(id):
        try:
            cursor.execute(
                "select * from operaciones where id_operacion=%s",(id,)
            )
            return cursor.fetchone()
        except:
            return False    

class Camiones:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        try:
            cursor.execute(
                "insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                (marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from camiones")
            
            return cursor.fetchall()
        except:
            print("\n\t..::No hay autos registrados::..")
            return []
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas, eje, capacidadCarga, id_camion):
        try:
            cursor.execute(
                "update camiones set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadCarga=%s where id_camion=%s",
                (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id_camion)
            )
            conexion.commit()
            return True
        except:
            print("\t\n..::No se pudo actualizar::..")
            return False
    
    @staticmethod
    def eliminar(id_camion):
        try:
            cursor.execute("delete from camiones where id_camion=%s", (id_camion,))
            conexion.commit()
            return True
        except:
            print("\n\t..:: No se pudo elmiminar ::..")
            return False
        

    @staticmethod
    def check(id):
        try:
            cursor.execute(
                "select * from operaciones where id_operacion=%s",(id,)
            )
            return cursor.fetchone()
        except:
            return False    