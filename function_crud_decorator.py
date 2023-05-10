from tkinter import messagebox
import sqlite3

#------------------------- Funciones

#------------------------- Funcion Decoradora
def con_decorator_dbbb(fun_process):
    def fun_internal(*args):
        try:
            connection=sqlite3.connect(args[0])
            cursor=connection.cursor()
            connection.commit()
            
            result=fun_process(cursor, *args)
            return result
        except sqlite3.Error as err:
            print(err)
            raise err
        finally:
            cursor.close()
            connection.close()
            
    return fun_internal


# Crear base de datos - requerida
# param    dbbb: Nombre de la base de datos
# param    query: Query con tabla y registros a crear en base de datos
# author    wlopera
# Mayo 2023 @wlopera
@con_decorator_dbbb
def createDB(cursor, dbbb, query):
    try:
        cursor.execute(query)        
        messagebox.showinfo("BDDD", "Bases de datos" + dbbb + " creada con éxito.!")
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "La base de datos " + dbbb +" ya existe.!")
          
# Agregar registro en base de datos
# param    dbbb: NOmbre de la base de datos
# param    query: Query de base de datos - crear
# param    data: Valores de los campos a registrar en base de datos
# author    wlopera
# Mayo 2023 @wlopera    
@con_decorator_dbbb
def create(cursor, dbbb, query, data):   
    try:
        cursor.execute(query, data)
        messagebox.showinfo("BDDD", "Registro agregado con exito.!")
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "La base de datos " + dbbb +" ya existe.!")
    
# Consultar registro en base de datos
# param    dbbb: Nopmbre de la base de datos
# param    query: Query de base de datos - consultar
# author    wlopera
# Mayo 2023 @wlopera  
@con_decorator_dbbb  
def read(cursor, dbbb, query):
    users=[]
    try:
        cursor.execute(query)
        users=cursor.fetchall()
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "La base de datos " + dbbb +" ya existe.!")   
        
    return users
    
# Actualizar registro en base de datos
# param    dbbb: Nombre de la base de datos
# param    query:  Query de base de datos - actualizar
# param    data: Valores de los campos a registrar en base de datos
# author    wlopera
# Mayo 2023 @wlopera  
@con_decorator_dbbb    
def update(cursor, dbbb, query, data):
    try:
        cursor.execute(query, data)    
        messagebox.showinfo("BDDD", "Registro actualizado exitosamente.!")        
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "Registro no existe en la DB.!")
        
# Eliminar registro en base de datos
# param    dbbb: Base de datos a consultar
# param    query:  Query de base de datos - borrar
# author    wlopera
# Mayo 2023 @wlopera   
@con_decorator_dbbb       
def delete(cursor, dbbb, query):
    try:
        cursor.execute(query)
        messagebox.showinfo("BDDD", "Registro borrado exitosamente.!")       
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "La base de datos " + dbbb +" ya existe.!")
