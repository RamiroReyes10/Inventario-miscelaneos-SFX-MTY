import tkinter
from tkinter import ANCHOR, CENTER, Label, ttk
from tkinter.font import Font
import pyodbc
import tkinter as tk
import pandas as pd
from tkinter import messagebox
from PIL import Image, ImageTk

Server = "SFX02EU8JX4HK3"
Database = "miscelaneos_db "
user = "RamiroSFXPruebas"
password = "Danganronpa10"

from sqlalchemy.engine import URL
cadena_conection = f"DRIVER={{SQL SERVER}};SERVER={Server};DATABASE={Database};UID={user};PWD={password}"
url_conection = URL.create("mssql+pyodbc", query={"odbc_connect": cadena_conection})

from sqlalchemy import create_engine
engine = create_engine(url_conection)

try: 
    connection = pyodbc.connect(cadena_conection)
    cursor = connection.cursor()

    
except Exception as e:
    print(f"Error: {e}")


def show_entradas():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

    titulo_entradas.pack(anchor=tk.CENTER)
    combo.place(x=200, y =35)
    boton_cargar.place(x=50, y=35)
    entry.place(x=200, y=75)
    boton_guardar.place(x=230, y=150)
    boton_volver.place(x=300, y=150)


def show_salidas():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

    titulo_salidas.pack(anchor=tk.CENTER)
    combo.place(x=200, y=35)
    boton_cargar_sal.place(x=50, y=35)
    entry.place(x=200, y=75)
    boton_guardar_sal.place(x=230, y=150)
    boton_volver.place(x=300, y=150)


def show_registros():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

        boton_reg_entradas.place(x=40, y =40)
        boton_reg_salidas.place(x=40, y=85)
        boton_inventario.place(x=40, y=135)
        boton_volver.place(x=380, y=150)

        titulo_reg = tk.Label(ventana_princ, text="Que informacion deseas ver?")
        titulo_reg.place(x=210, y=13)
        titulo_reg.config(bg="white",
                          font=("Arial Black",12))


def show_main():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

        titulo = tk.Label(ventana_princ, text="Bienvenido al Sistema de Inventario Miscelaneos SFX MTY! \n Que movimiento desea hacer?")
        titulo.place(x=50, y=4)
        titulo.config(bg="white",
                      font=("Arial Black",10))

        boton_entradas.place(x=50, y=140)
        boton_salidas.place(x=175, y=140)
        boton_registros.place(x=290, y=140)
        boton_salir.place(x=395, y=140)

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

    #Verificar que los campos no esten vacios
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


def export_excel_inventario():
    try:
        query_inventario = "select * from dbo.inventarios"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_inventario, cursor)
             excel_file_inven = "Inventario.xlsx"
             df_i.to_excel(excel_file_inven, index=False)

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion del inventario a excel: {str(e)}")

def export_excel_entradas():
    try:
        query_entradas = "select * from dbo.entradas;"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_entradas, cursor)
             excel_file_ent = "entradas.xlsx"
             df_i.to_excel(excel_file_ent, index=False)

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion de las entradas a excel: {str(e)}")

def export_excel_salidas():
    try:
        query_salidas = "select * from dbo.salidas;"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_salidas, cursor)
             excel_file_sal = "salidas.xlsx"
             df_i.to_excel(excel_file_sal, index=False)

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion de las salidas a excel: {str(e)}")

def Salir_app():
    ventana_princ.destroy()


#Interfaz principal y funciones 
ventana_princ = tk.Tk()
ventana_princ.title("Inventario Miscelaneos SFX MTY")
ventana_princ.geometry("500x200")
ventana_princ.resizable(width=False, height=False)

img = ImageTk.PhotoImage(Image.open("capy.jpg")) 
Label(ventana_princ, image=img, anchor="nw").pack()

ventana_princ.iconbitmap("avion.ico")

boton_entradas = tk.Button(ventana_princ, text="Entradas", command=show_entradas)
boton_salidas = tk.Button(ventana_princ, text="Salidas", command=show_salidas)
boton_registros = tk.Button(ventana_princ, text="Registros", command=show_registros)
boton_salir = tk.Button(ventana_princ, text="Salir", command=Salir_app)

titulo_entradas = tk.Label(ventana_princ, text="Entradas")
boton_cargar = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
entry = tk.Entry(ventana_princ)
boton_guardar = tk.Button(ventana_princ, text="Guardar", command=guardar_entrada)
boton_volver = tk.Button(ventana_princ, text="Volver", command=show_main)

titulo_salidas = tk.Label(ventana_princ, text="Salidas")
boton_cargar_sal = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
boton_guardar_sal = tk.Button(ventana_princ, text="Guardar", command=guardar_salida)

boton_reg_entradas = tk.Button(ventana_princ, text="Registro de entradas", command=export_excel_entradas)
boton_reg_salidas = tk.Button(ventana_princ, text="Registro de Salidas", command=export_excel_salidas)
boton_inventario = tk.Button(ventana_princ, text="Inventario", command=export_excel_inventario)

combo = ttk.Combobox(ventana_princ, font=Font(size=15))

show_main()

#Ejecutar interfaz principal
ventana_princ.mainloop()
