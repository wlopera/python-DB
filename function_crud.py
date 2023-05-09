from tkinter import messagebox
import sqlite3

#------------------------- Funciones

# Crear base de datos - requerida
# param    dbbb: Nombre de la base de datos
# param    query: Query con tabla y registros a crear en base de datos
# author    wlopera
# Mayo 2023 @wlopera
def createDB(dbbb, query):
    connection=sqlite3.connect(dbbb)
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        
        messagebox.showinfo("BDDD", "Bases de datos" + dbbb + " creada con éxito.!")
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "La base de datos " + dbbb +" ya existe.!")
    
    cursor.close()
    connection.close()
      
# Agregar registro en base de datos
# param    dbbb: NOmbre de la base de datos
# param    query: Query de base de datos - crear
# param    data: Valores de los campos a registrar en base de datos
# author    wlopera
# Mayo 2023 @wlopera    
def create(dbbb, query, data):
    connection=sqlite3.connect(dbbb)
    cursor=connection.cursor()
    
    cursor.execute(query, data)
    
    # cursor.execute("INSERT INTO " + dbbb + " values(NULL, '"+ firstname.get()
    #         + "','" +  password.get() 
    #         + "','" +  lastname.get() 
    #         + "','" + address.get() 
    #         + "','" + fieldComment.get(1.0, END) 
    #         +"')")
    
    connection.commit()
    
    messagebox.showinfo("BDDD", "Registro agregado con exito.!")
    
    cursor.close()
    connection.close()

# Consultar registro en base de datos
# param    dbbb: Nopmbre de la base de datos
# param    query: Query de base de datos - consultar
# author    wlopera
# Mayo 2023 @wlopera    
def read(dbbb, query):
    connection=sqlite3.connect(dbbb)
    cursor=connection.cursor()
    cursor.execute(query)
    
    users=cursor.fetchall()
     
    connection.commit()
           
    cursor.close()
    connection.close()
    
    return users
    
# Actualizar registro en base de datos
# param    dbbb: Nombre de la base de datos
# param    query:  Query de base de datos - actualizar
# param    data: Valores de los campos a registrar en base de datos
# author    wlopera
# Mayo 2023 @wlopera     
def update(dbbb, query, data):
    connection=sqlite3.connect(dbbb)
    cursor=connection.cursor()
    
    try:
        cursor.execute(query, data)
        
        # cursor.execute("UPDATE " + dbbb + " set FIRSTNAME_USER='" + firstname.get()
        #         + "', PASSWORD='" +  password.get() 
        #         + "', LASTNAME_USER='" +  lastname.get() 
        #         + "', ADDRESS='" + address.get() 
        #         + "', COMMENTS='" + fieldComment.get(1.0, END) 
        #         +"' WHERE ID="+ id.get())
        
        connection.commit()
        
        messagebox.showinfo("BDDD", "Registro actualizado exitosamente.!")
        
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "Registro no existe en la DB.!")
    finally:
        cursor.close()
        connection.close()
        
# Eliminar registro en base de datos
# param    dbbb: Base de datos a consultar
# param    query:  Query de base de datos - borrar
# author    wlopera
# Mayo 2023 @wlopera          
def delete(dbbb, query):
    try:
        connection=sqlite3.connect(dbbb)
        cursor=connection.cursor()
        
        cursor.execute(query)
            
        connection.commit()
        
        messagebox.showinfo("BDDD", "Registro borrado exitosamente.!")
        
        cursor.close()
        connection.close()
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "Registro no existe en la DB.!")