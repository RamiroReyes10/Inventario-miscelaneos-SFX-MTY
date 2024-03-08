from tkinter.font import Font
from typing import Self
import pyodbc
import tkinter as tk
from tkinter import CENTER, Frame, Label, ttk
from tkinter import messagebox
from PIL import Image, ImageTk

Server = "SFX02EU8JX4HK3"
Database = "miscelaneos_db "
user = "RamiroSFXPruebas"
password = "Danganronpa10"
cadena_conection = f"DRIVER={{SQL SERVER}};SERVER={Server};DATABASE={Database};UID={user};PWD={password}"


try: 
    connection = pyodbc.connect(cadena_conection)
    cursor = connection.cursor()


except Exception as e:
    print(f"Error: {e}")



def Salir_app():
    ventana_princ.destroy()


def Interfaz_entradas():
    #Destruir widgets actuales
    titulo_inv_misc.destroy()
    boton_entradas.destroy()
    boton_salidas.destroy()
    boton_salir.destroy()

    #crear nuevos widgets para la interfaz entradas
    titulo_entradas = Label(ventana_princ, text="Entradas")
    titulo_entradas.pack(anchor=tk.CENTER)

    #se agrega combox para lista desplegable de productos
    combo.place(x=200, y=35)

    #agregar boton que cargara la informacion del combobox
    boton_cargar = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
    boton_cargar.place(x=80, y=35)

    entry.place(x=200, y=75)

    boton_guardar = tk.Button(ventana_princ, text="Guardar", command=guardar_entrada)
    boton_guardar.place(x=200, y=140)

    #Boton para volver
    boton_volver = tk.Button(ventana_princ, text="Volver", command=volver_inter_prin)
    boton_volver.place(x=430, y=140)


def Interfaz_salidas():
    #Destruir widgets actuales
    titulo_inv_misc.destroy()
    boton_entradas.destroy()
    boton_salidas.destroy()
    boton_salir.destroy()

    #crear nuevos widgets para la interfaz entradas
    titulo_salidas = Label(ventana_princ, text="Salidas")
    titulo_salidas.pack(anchor=tk.CENTER)

    #se agrega combox para lista desplegable de productos
    combo.place(x=200, y=35)

    #agregar boton que cargara la informacion del combobox
    boton_cargar_sal = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
    boton_cargar_sal.place(x=80, y=35)

    entry.place(x=200, y=75)

    boton_guardar_sal = tk.Button(ventana_princ, text="Guardar", command=guardar_salida)
    boton_guardar_sal.place(x=200, y=140)

    #Boton para volver
    boton_volver = tk.Button(ventana_princ, text="Volver", command=volver_inter_prin)
    boton_volver.place(x=430, y=140)


def volver_inter_prin():
    global titulo_inv_misc, boton_entradas, boton_salidas, boton_salir

    #Eliminar widgets actuales
    for widget in ventana_princ.winfo_children():
        if widget not in [titulo_inv_misc, boton_entradas, boton_salidas, boton_salir]:
            widget.destroy()

    titulo_inv_misc = Label(ventana_princ, text="\nBienvenido al Sistema de Inventario Miscelaneos SFX MTY! \n Que movimiento desea hacer?")
    titulo_inv_misc.pack(anchor=tk.CENTER)
    titulo_inv_misc.config(fg="black", font=("Verdana, 12"))

    boton_entradas = tk.Button(ventana_princ, text="Entradas", command=Interfaz_entradas)
    boton_entradas.place(x=50, y=125)

    boton_salidas = tk.Button(ventana_princ, text="Salidas")
    boton_salidas.place(x=230, y=125)

    boton_salir = tk.Button(ventana_princ, text="Salir", command=Salir_app)
    boton_salir.place(x=400, y=125)

def cargar_productos():
    try:
        cursor.execute("SELECT [Nombre_del_producto] FROM dbo.Inventarios")
        datos = [fila.Nombre_del_producto for fila in cursor.fetchall()]
        combo['values'] = tuple(datos)
    except Exception as e:
        print(f"Error al cargar productos: {e}")
        


#funcion para guardar stock entrada
def guardar_entrada():
    #Recuperer el nombre del producto seleccionado en el combobox
    nombre_del_producto = combo.get()

    #Recuperar la cantidad ingresada en el Entry
    cantidad = entry.get()

    #Verificart que los campos no esten vacios
    if nombre_del_producto and cantidad:
        try:
            #convertir la cantidad a int
            cantidad = int(cantidad)
            
            #Actuaizar el Stock de la tabla inventarios
            cursor.execute("UPDATE dbo.Inventarios SET stock = stock + ? WHERE Nombre_del_producto = ?", (cantidad, nombre_del_producto))
            
            #Obtener el sotck actualizado del producto
            cursor.execute("SELECT stock FROM dbo.Inventarios WHERE Nombre_del_producto = ?",(nombre_del_producto))
            stock_actual = cursor.fetchone()[0]
            
            #Ejecutar la consulta de SQL con los valores obtenidos
            cursor.execute("INSERT INTO dbo.Entradas (nombre_del_producto, stock_actual, entrada, fecha) VALUES (?, ?, ?, GETDATE())",(nombre_del_producto, stock_actual, cantidad,))

            #este linea hace que se guarden los cambios en la base de datos
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Por favor, selecciona un producto e ingresa una cantidad.")


#funcion para guardar stock Salida
def guardar_salida():
    
    #Mismo proceso para guardar entradas pero ahora restando en el query
    nombre_del_producto_sal = combo.get()

    cantidad_sal = entry.get()
    
    if nombre_del_producto_sal and cantidad_sal:
        try:
            cantidad_sal = int(cantidad_sal)
            
            cursor.execute("UPDATE dbo.Inventarios SET stock = stock - ? WHERE Nombre_del_producto = ?", (cantidad_sal, nombre_del_producto_sal))
            
            cursor.execute("SELECT stock FROM dbo.Inventarios WHERE Nombre_del_producto = ?",(nombre_del_producto_sal))
            stock_actual = cursor.fetchone()[0]
            
            cursor.execute("INSERT INTO dbo.Salidas (nombre_del_producto, stock_actual, salida, fecha) VALUES (?, ?, ?, GETDATE())",(nombre_del_producto_sal, stock_actual, cantidad_sal,))

            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Por favor, selecciona un producto e ingresa una cantidad.")



#Interfaz principal
ventana_princ = tk.Tk()
ventana_princ.title("Inventario Miscelaneos SFX MTY")


ventana_princ.iconbitmap("avion.ico")

ventana_princ.geometry("500x200")
ventana_princ.resizable(width=False, height=False)


titulo_inv_misc = Label(ventana_princ, text="\nBienvenido al Sistema de Inventario Miscelaneos SFX MTY! \n Que movimiento desea hacer?")
titulo_inv_misc.pack(anchor=CENTER)
titulo_inv_misc.config(fg="black",
                       font=("Verdana, 12"))

boton_entradas = tk.Button(ventana_princ, text="Entradas", command=Interfaz_entradas)
boton_entradas.place(x=50, y=125)

boton_salidas = tk.Button(ventana_princ, text="Salidas", command=Interfaz_salidas)
boton_salidas.place(x=230, y=125)

boton_salir = tk.Button(ventana_princ, text="Salir", command=ventana_princ.quit)
boton_salir.place(x=400, y=125)

combo = ttk.Combobox(ventana_princ, font=Font(size=15))
entry = tk.Entry(ventana_princ)


#Ejecutar interfaz principal
ventana_princ.mainloop()
