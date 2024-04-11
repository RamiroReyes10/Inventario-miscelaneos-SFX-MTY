import tkinter
from tkinter import ANCHOR, CENTER, CURRENT, LEFT, Label, ttk
from tkinter import filedialog
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
        boton_consulta.place(x=50, y=80)
        boton_intransit.place(x=175, y=80)


def cargar_productos():
    try:
        cursor.execute("SELECT [Nombre_del_producto] FROM dbo.Inventarios")
        datos = [fila.Nombre_del_producto for fila in cursor.fetchall()]
        combo['values'] = tuple(datos)
    except Exception as e:
        print(f"Error al cargar productos: {e}")


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

def show_consultas():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

    boton_consultas.place(x=110, y=95)
    boton_consuta_int.place(x=285, y=95)
    boton_volver.place(x=370, y=150)

    titulo_consultas_reg = tk.Label(ventana_princ, text="Que registro deseas ver?")
    titulo_consultas_reg.place(x=140, y=13)
    titulo_consultas_reg.config(bg="white",
                                font=("Arial Black",12))


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

def show_intransit_interfaz():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

        boton_agregar_int.place(x=50, y=100)
        boton_registo_int.place(x=350, y=100)
        boton_recibo_material.place(x=200, y=100)
        boton_volver.place(x=390, y=153)

        titulo_intransit = tk.Label(ventana_princ, text="Que movimiento deseas realizar en Intransit?")
        titulo_intransit.place(x=75, y=10)
        titulo_intransit.config(bg="white",
                                font=("Arial Black",10))


def show_agregar_instransit():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

        combo.place(x=200, y=35)
        boton_cargar_sal.place(x=50, y=35)
        entry.place(x=200, y=75)
        boton_guardar_ints.place(x=230, y=150)
        boton_volver_main_int.place(x=300, y=150)

def show_recibo_material_intransit():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

        combo.place(x=200, y=35)
        boton_cargar_sal.place(x=50, y=35)
        entry.place(x=200, y=75)
        boton_guardar_recibo_material.place(x=300, y=150)
        boton_volver_main_int.place(x=390, y=150)

def show_consulta_accion():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

    titulo_salidas.pack(anchor=tk.CENTER)
    combo.place(x=200, y=35)
    boton_selec_prod_accion.place(x=50, y=35)
    stock_textbox.place(x=130, y=95)
    accion_textbox.place(x=355, y=95)
    boton_consultar_produc_accion.place(x=230, y=150)
    boton_volver_consultas.place(x=330, y=150)

    cantidad_prod = tk.Label(ventana_princ, text="Stock Actual")
    cantidad_prod.place(x=30, y=95)
    cantidad_prod.config(bg="white",
                         font=("Arial Black",8))

    estado_prod = tk.Label(ventana_princ, text="Status")
    estado_prod.place(x=300, y=95)
    estado_prod.config(bg="white",
                         font=("Arial Black",8))

def show_consulta_de_intransit():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

        combo.place(x=200, y=35)
        boton_selec_prod_in_int.place(x=50, y=35)
        stock_int.place(x=200, y=95)
        boton_consultar_in_intransit.place(x=250, y=150)
        boton_volver_consultas.place(x=360, y=150)



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
            messagebox.showinfo("Exito", "Entrada guardada correctamente")
        except Exception as e:
            messagebox.showerror(f"Error: {e}")
    else:
        messagebox.showerror("error", f"Por favor, selecciona un producto e ingresa una cantidad.")


#funcion para guardar stock Salida
def guardar_salida():
    nombre_del_producto_sal = combo.get()
    cantidad_sal = entry.get()
    
    if nombre_del_producto_sal and cantidad_sal:
        try:
            cantidad_sal = int(cantidad_sal)
            
            cursor.execute("UPDATE dbo.Inventarios SET stock = stock - ? WHERE Nombre_del_producto = ?", (cantidad_sal, nombre_del_producto_sal))
            
            cursor.execute("SELECT stock, Punto_Reorden FROM dbo.Inventarios WHERE Nombre_del_producto = ?",(nombre_del_producto_sal,))
            resultado = cursor.fetchone()  
            if resultado:  
                stock_actual, punto_de_reorden = resultado
                
                cursor.execute("INSERT INTO dbo.Salidas (nombre_del_producto, stock_actual, salida, fecha) VALUES (?, ?, ?, GETDATE())",(nombre_del_producto_sal, stock_actual, cantidad_sal,))
    
                if stock_actual < punto_de_reorden:
                    cursor.execute("UPDATE dbo.Inventarios SET Accion = 'Comprar' WHERE Nombre_del_Producto = ?", (nombre_del_producto_sal,))
                    connection.commit()
    
                messagebox.showinfo("Exito", "Salida guardada correctamente")
            else:
                messagebox.showerror("Error", "Producto no encontrado en el inventario.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    else:
        messagebox.showerror("Error", "Por favor, selecciona un producto e ingresa una cantidad.")

def guardar_intransit():
    nombre_del_producto_ints = combo.get()
    cantidad_ints = entry.get()

    if nombre_del_producto_ints and cantidad_ints:
        try:
            cantidad_ints = int(cantidad_ints)
            cursor.execute("UPDATE dbo.inventarios SET Accion = 'En Transito' WHERE Nombre_del_producto = ?", (nombre_del_producto_ints,))
            cursor.execute("UPDATE dbo.Inventarios SET intran = ISNULL(intran,0) + ? WHERE Nombre_del_producto = ?", (cantidad_ints, nombre_del_producto_ints))
            cursor.execute("Select stock FROM dbo.Inventarios where Nombre_del_producto = ?",(nombre_del_producto_ints))
            stock_actual = cursor.fetchone()[0]
            cursor.execute("INSERT INTO dbo.Intransit (nombre_del_producto, stock_actual, intransit, fecha) VALUES (?, ?, ?, GETDATE())",(nombre_del_producto_ints, stock_actual, cantidad_ints))
            connection.commit()
            messagebox.showinfo("Exito", "Informacion guardada correctamente")

        except Exception as e:
            messagebox.showerror(f"Error: {e}")
    else:
        messagebox.showerror("error", f"Por favor seleccione un producto y una cantidad.") 


def recibir_material_instransit():
    nombre_de_producto_inst_rm = combo.get()
    cantidad_ints_rm = entry.get()

    if nombre_de_producto_inst_rm and cantidad_ints_rm:
        try:
            cantidad_ints_rm = int(cantidad_ints_rm)
            cursor.execute("UPDATE dbo.Inventarios SET intran = intran - ? WHERE Nombre_del_producto = ?", (cantidad_ints_rm, nombre_de_producto_inst_rm))
            cursor.execute("Select stock FROM dbo.Inventarios where Nombre_del_producto = ?",(nombre_de_producto_inst_rm))
            stock_actual = cursor.fetchone()[0]
            cursor.execute("INSERT INTO dbo.Intransit (nombre_del_producto, stock_actual, recibo_de_material, fecha) VALUES (?, ?, ?, GETDATE())",(nombre_de_producto_inst_rm, stock_actual, cantidad_ints_rm))
            connection.commit()

            messagebox.showinfo("exito", "Informacion guardada correctamente")

        except Exception as e:
            messagebox.showerror(f"Error: {e}")
    else:
        messagebox.showerror("error", f"Por favor seleccione un producto y una cantidad")

def actualizacion_stock_consulta():
    producto_seleccionado = combo.get()
    cursor.execute("SELECT stock, Accion FROM dbo.inventarios WHERE Nombre_del_producto = ?", (producto_seleccionado,))
    resultado = cursor.fetchone()

    if resultado:
        stock_textbox.delete(0, tk.END) 
        stock_textbox.insert(0, resultado[0])  

        accion_textbox.delete(0, tk.END)  
        accion_textbox.insert(0, resultado[1])
 
    else:
        messagebox.showerror("error", f"Producto no encontrado")

def actualizacion_intransit_consulta():
    producto_seleccionado = combo.get()
    cursor.execute("SELECT intran FROM dbo.Inventarios WHERE Nombre_del_producto = ?", (producto_seleccionado,))
    resultado = cursor.fetchone()
    connection.commit()

    if resultado:
        stock_int.delete(0, tk.END)
        stock_int.insert(0, resultado[0])

    else:
        messagebox.showerror("Error", f"Producto no encontrado")


def export_excel_inventario():
    try:
        query_inventario = "select * from dbo.inventarios"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_inventario, cursor)
             file_path_inv = filedialog.asksaveasfilename(defaultextension='xlsx',
                                                          filetypes=[("Excel files", "*.xlsx")])
             if file_path_inv == "":
                messagebox.showinfo("Informacion", "Informacion Cancelada sin guardar!")
                return

             df_i.to_excel(file_path_inv, index=False)
             messagebox.showinfo("Exito!", "Informacion guardada correctamente")

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion del inventario a excel: {str(e)}")

def export_excel_entradas():
    try:
        query_entradas = "select * from dbo.entradas;"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_entradas, cursor)
             file_path_ent = filedialog.asksaveasfilename(defaultextension='xlsx',
                                                          filetypes=[("Excel files", "*.xlsx")])
             if  file_path_ent == "":
                 messagebox.showinfo("Informacion", "Informacion Cancelada sin guardar!")
                 return

             df_i.to_excel(file_path_ent, index=False)
             messagebox.showinfo("Exito", "Informacion exportada a Excel correctamente!")

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion de las entradas a excel: {str(e)}")

def export_excel_salidas():
    try:
        query_salidas = "select * from dbo.salidas"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_salidas, cursor)
             file_path_sal = filedialog.asksaveasfilename(defaultextension='xlsx',
                                                          filetypes=[("Ecel files", "*.xlsx")])
             if file_path_sal == "":
                 messagebox.showinfo("Informacion", "Informacion cancelada sin guadar!")
                 return

             df_i.to_excel(file_path_sal, index=False)
             messagebox.showinfo("Exito", "Informacion exportada correctamente!")

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion de las salidas a excel: {str(e)}")

def export_excel_intransit():
    try:
        query_intransit="select * from dbo.intransit"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_intransit, cursor)
             file_path_intransit = filedialog.asksaveasfilename(defaultextension='xlsx',
                                                           filetypes=[("Excel files", "*.xlsx")])
             if file_path_intransit =="":
                 messagebox.showinfo("Informacion", "Informacion cancelada sin guardar!")
                 return

             df_i.to_excel(file_path_intransit, index=False)
             messagebox.showinfo("Exito", "Informacion guardada correctamente!")

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion a excel: {str(e)}")


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

#Botones de interfaz principal
boton_entradas = tk.Button(ventana_princ, text="Entradas", command=show_entradas)
boton_salidas = tk.Button(ventana_princ, text="Salidas", command=show_salidas)
boton_registros = tk.Button(ventana_princ, text="Registros", command=show_registros)
boton_salir = tk.Button(ventana_princ, text="Salir", command=Salir_app)
boton_consulta = tk.Button(ventana_princ, text="Consulta", command=show_consultas)
boton_intransit = tk.Button(ventana_princ, text="Intransit", command=show_intransit_interfaz)

#Botones, combobox titulos y mas
titulo_entradas = tk.Label(ventana_princ, text="Entradas")
boton_cargar = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
entry = tk.Entry(ventana_princ)
boton_guardar = tk.Button(ventana_princ, text="Guardar", command=guardar_entrada)
boton_volver = tk.Button(ventana_princ, text="Volver", command=show_main)


titulo_salidas = tk.Label(ventana_princ, text="Salidas")
boton_cargar_sal = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
boton_guardar_sal = tk.Button(ventana_princ, text="Guardar", command=guardar_salida)

boton_agregar_int = tk.Button(ventana_princ, text="Agregar a intransit", command=show_agregar_instransit)
boton_registo_int = tk.Button(ventana_princ, text="Registros", command=export_excel_intransit)
boton_recibo_material = tk.Button(ventana_princ, text="Recibo de material", command=show_recibo_material_intransit)
boton_guardar_recibo_material = tk.Button(ventana_princ, text="guardar", command=recibir_material_instransit)

boton_selec_prod_in_int = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
boton_consultar_in_intransit = tk.Button(ventana_princ, text="Consultar", command=actualizacion_intransit_consulta)

boton_guardar_ints =tk.Button(ventana_princ, text="Guardar", command=guardar_intransit)
boton_volver_main_int =tk.Button(ventana_princ, text="volver", command=show_intransit_interfaz)

titulo_consultas = tk.Label(ventana_princ, text="Consultas")
boton_consultas = tk.Button(ventana_princ, text="Consulta de stock", command=show_consulta_accion)
boton_consuta_int = tk.Button(ventana_princ, text="Consulta de Intrasit", command=show_consulta_de_intransit)
boton_selec_prod_accion = tk.Button(ventana_princ, text="consultar producto", command=cargar_productos)
boton_consultar_produc_accion = tk.Button(ventana_princ, text="Consultar", command=actualizacion_stock_consulta)
boton_volver_consultas = tk.Button(ventana_princ, text="volver", command=show_consultas)
accion = tk.Entry(ventana_princ)

boton_reg_entradas = tk.Button(ventana_princ, text="Registro de entradas", command=export_excel_entradas)
boton_reg_salidas = tk.Button(ventana_princ, text="Registro de Salidas", command=export_excel_salidas)
boton_inventario = tk.Button(ventana_princ, text="Inventario", command=export_excel_inventario)

stock_textbox = tk.Entry(ventana_princ)
stock_textbox.pack(pady=5)
 
accion_textbox = tk.Entry(ventana_princ)
accion_textbox.pack(pady=5)

stock_int = tk.Entry(ventana_princ)


combo = ttk.Combobox(ventana_princ, state="readonly", font=Font(size=15))

show_main()

#Ejecutar interfaz principal
ventana_princ.mainloop()
