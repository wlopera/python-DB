from tkinter import *
from tkinter import messagebox
import sqlite3

#------------------------- Funciones
def getConnectedDB():
    connection=sqlite3.connect("users.db")
    cursor=connection.cursor()
    try:
        cursor.execute('''
            CREATE TABLE users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FIRSTNAME_USER VARCHAR(50),
            PASSWORD VARCHAR(50),
            LASTNAME_USER VARCHAR(50),
            ADDRESS VARCHAR(50),
            COMMENTS VARCHAR(100))
            ''')
        
        messagebox.showinfo("BDDD", "Bases de datos USUARIOS creada con éxito.!")
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "La base de datos USUARIOS ya existe.!")
    
    cursor.close()
    connection.close()

def exit():
    value=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if value=="yes":
        root.destroy()

def clearFields():
    id.set("")
    firstname.set("")
    password.set("")
    lastname.set("")
    address.set("")
    fieldComment.delete(1.0, END)
    
def create():
    connection=sqlite3.connect("users.db")
    cursor=connection.cursor()
    
    data=firstname.get(), password.get(), lastname.get(), address.get(), fieldComment.get(1.0, END)
    cursor.execute("INSERT INTO users values(NULL,?,?,?,?,?)", data)
    
    # cursor.execute("INSERT INTO users values(NULL, '"+ firstname.get()
    #         + "','" +  password.get() 
    #         + "','" +  lastname.get() 
    #         + "','" + address.get() 
    #         + "','" + fieldComment.get(1.0, END) 
    #         +"')")
    
    connection.commit()
    
    messagebox.showinfo("BDDD", "Registro agregado con exito.!")
    
    cursor.close()
    connection.close()
    
def read():
    connection=sqlite3.connect("users.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM users WHERE ID="+ id.get())
    
    users=cursor.fetchall()
    
    if len(users)==0:
         messagebox.showwarning("Alerta!", "Registro no existe en la DB.!")
         return
     
    print(users)
    user=users[0]
    
    firstname.set(user[1])
    password.set(user[2])
    lastname.set(user[3])
    address.set(user[4])
    fieldComment.delete(1.0, END)
    fieldComment.insert(1.0, user[5])
    
    connection.commit()
           
    cursor.close()
    connection.close()
    
def update():
    connection=sqlite3.connect("users.db")
    cursor=connection.cursor()
    
    try:
        
        data=firstname.get(), password.get(), lastname.get(), address.get(), fieldComment.get(1.0, END)
        cur=cursor.execute("UPDATE users SET FIRSTNAME_USER=?,PASSWORD=?,LASTNAME_USER=?,ADDRESS=?,COMMENTS=? WHERE ID="+id.get(), data)
        print(cursor)
        # cursor.execute("UPDATE users set FIRSTNAME_USER='" + firstname.get()
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
        
def delete():
    try:
        connection=sqlite3.connect("users.db")
        cursor=connection.cursor()
        cursor.execute("DELETE FROM users WHERE ID="+ id.get())
            
        connection.commit()
        
        messagebox.showinfo("BDDD", "Registro borrado exitosamente.!")
        
        cursor.close()
        connection.close()
    except sqlite3.Error as err:
        print(err)
        messagebox.showwarning("Alerta!", "Registro no existe en la DB.!")

       
root=Tk()
#------------------------- MENUS
menuBar=Menu(root)
root.config(menu=menuBar, width=300, height=300)

menuBddd=Menu(menuBar, tearoff=0)
menuBddd.add_command(label="Conectar", command=getConnectedDB)
menuBddd.add_command(label="Salir", command=exit)
    
menuDelete=Menu(menuBar, tearoff=0)
menuDelete.add_command(label="Borrar campos", command=clearFields)    

menuCrud=Menu(menuBar, tearoff=0)
menuCrud.add_command(label="Crear", command=create)    
menuCrud.add_command(label="Leer", command=read)    
menuCrud.add_command(label="Actualizar", command=update)    
menuCrud.add_command(label="Borrar", command=delete)    

menuHelp=Menu(menuBar, tearoff=0)
menuHelp.add_command(label="Licencia")    
menuHelp.add_command(label="Acerca de...")    

menuBar.add_cascade(label="BDDD", menu=menuBddd)
menuBar.add_cascade(label="Borrar", menu=menuDelete)
menuBar.add_cascade(label="CRUD", menu=menuCrud)
menuBar.add_cascade(label="Ayuda", menu=menuHelp)

#------------------------- Frame 1: Campos
frameFields=Frame(root)
frameFields.pack()

id=StringVar()
firstname=StringVar()
password=StringVar()
lastname=StringVar()
address=StringVar()

fieldId=Entry(frameFields, textvariable=id)
fieldId.grid(row=0, column=1,padx=10, pady=10 )

fieldFirstname=Entry(frameFields, textvariable=firstname)
fieldFirstname.grid(row=1, column=1,padx=10, pady=10 )
fieldFirstname.config(fg="red", justify="right")

fieldPassword=Entry(frameFields, textvariable=password)
fieldPassword.grid(row=2, column=1,padx=10, pady=10 )
fieldPassword.config(show="*")

fieldLastname=Entry(frameFields, textvariable=lastname)
fieldLastname.grid(row=3, column=1,padx=10, pady=10 )

fieldAddress=Entry(frameFields, textvariable=address)
fieldAddress.grid(row=4, column=1,padx=10, pady=10 )

fieldComment=Text(frameFields, width=16, height=5)
fieldComment.grid(row=5, column=1,padx=10, pady=10 )
scrollVert=Scrollbar(frameFields, command=fieldComment.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
fieldComment.config(yscrollcommand=scrollVert.set)

#------------------------- Frame 1: Labels
labelId=Label(frameFields, text="Id:")
labelId.grid(row=0, column=0, sticky="e", padx=10, pady=10)

labelFirstname=Label(frameFields, text="Nombre:")
labelFirstname.grid(row=1, column=0, sticky="e", padx=10, pady=10)

labelPassword=Label(frameFields, text="Clave:")
labelPassword.grid(row=2, column=0, sticky="e", padx=10, pady=10)

labelFirstname=Label(frameFields, text="Apellido:")
labelFirstname.grid(row=3, column=0, sticky="e", padx=10, pady=10)

labelAddress=Label(frameFields, text="Dirección:")
labelAddress.grid(row=4, column=0, sticky="e", padx=10, pady=10)

labelComment=Label(frameFields, text="Comentarios:")
labelComment.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#------------------------- Frame 2: Botones
frameButtons=Frame(root)
frameButtons.pack()

buttonCreate=Button(frameButtons, text="Crear", command=create)
buttonCreate.grid(row=1, column=0, sticky="e", padx=10, pady=10)

buttonRead=Button(frameButtons, text="Leer", command=read)
buttonRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)

buttonUpdate=Button(frameButtons, text="Actualizar", command=update)
buttonUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

buttonDelete=Button(frameButtons, text="Borrar", command=delete)
buttonDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)

buttonExit=Button(frameButtons, text="Salir", command=exit)
buttonExit.grid(row=2, column=0, columnspan=4, sticky=W+E, padx=10, pady=5)


root.mainloop()