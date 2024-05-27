from multiprocessing import Value
from re import X
from tkinter import ANCHOR, CENTER, CURRENT, LEFT, Label, ttk
from tkinter import filedialog
from tkinter.font import Font
from turtle import window_height, window_width
from typing import Text
from numpy import size
import pyodbc
import tkinter as tk
import pandas as pd
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import datetime

from sqlalchemy.orm import state

Server = "SFX02EU8JX4HK3"
Database = "miscelaneos_db "
user = "RamiroSFXPruebas"
password = "Danganronpa11"

from sqlalchemy.engine import URL
cadena_conection = f"DRIVER={{SQL SERVER}};SERVER={Server};DATABASE={Database};UID={user};PWD={password}"
url_conection = URL.create("mssql+pyodbc", query={"odbc_connect": cadena_conection})

from sqlalchemy import create_engine, values
engine = create_engine(url_conection)

try: 
    connection = pyodbc.connect(cadena_conection)
    cursor = connection.cursor()

    
except Exception as e:
    print(f"Error: {e}")


def show_main():
    clear_window()    

    titulo = tk.Label(ventana_princ, text="Bienvenido al Sistema de Inventario Miscelaneos SFX MTY! \n Que movimiento desea hacer?")
    titulo.place(x=50, y=4)
    titulo.config(bg="white",
                      font=("Arial Black",10))

    footer_version = tk.Label(ventana_princ, text= "Version 1.0 \nBETA-DEMO")
    footer_version.place(x=415, y=160)
    footer_version.config(bg="white",
                          font=("MS Sans Serif", 8))

    boton_entradas.place(x=50, y=140)
    boton_salidas.place(x=175, y=140)
    boton_registros.place(x=290, y=80)
    boton_salir.place(x=395, y=80)
    boton_consulta.place(x=50, y=80)
    boton_intransit.place(x=175, y=80)
    boton_materiales.place(x=290, y=140)
    
def clear_window():
    for widget in ventana_princ.winfo_children():
        widget.place_forget()

def tamano_ventana_uno():
     ventana_princ.geometry("1210x600")

def tamano_ventana_dos():
    ventana_princ.geometry("500x200")
        


def cargar_productos():
    try:
        cursor.execute("SELECT [Nombre_del_producto] FROM dbo.Inventarios")
        datos = [fila.Nombre_del_producto for fila in cursor.fetchall()]
        combo['values'] = tuple(datos)
    except Exception as e:
        print(f"Error al cargar productos: {e}")

        
def cargar_productos_del():
        try:
            cursor.execute("SELECT [Nombre_del_producto] FROM dbo.Inventarios")
            datos = [fila.Nombre_del_producto for fila in cursor.fetchall()]
            print("Datos recuperados:", datos) 
            combobox_productos_del['values'] = tuple(datos)
        except Exception as e:
              print(f"Error al cargar productos: {e}")



def show_entradas():
    clear_window()

    titulo_entradas.pack(anchor=tk.CENTER)
    combo.place(x=200, y =35)
    boton_cargar.place(x=50, y=35)
    entry.place(x=200, y=75)
    boton_guardar.place(x=230, y=150)
    boton_volver.place(x=300, y=150)


def show_salidas():
    clear_window()

    titulo_salidas.pack(anchor=tk.CENTER)
    combo.place(x=200, y=35)
    boton_cargar_sal.place(x=50, y=35)
    entry.place(x=200, y=75)
    boton_guardar_sal.place(x=230, y=150)
    boton_volver.place(x=300, y=150)

def show_consultas():
    clear_window()

    boton_consultas.place(x=110, y=95)
    boton_consuta_int.place(x=285, y=95)
    boton_volver.place(x=370, y=150)

    titulo_consultas_reg = tk.Label(ventana_princ, text="Que registro deseas ver?")
    titulo_consultas_reg.place(x=140, y=13)
    titulo_consultas_reg.config(bg="white",
                                font=("Arial Black",12))


def show_registros():
    clear_window()

    boton_reg_entradas.place(x=40, y =40)
    boton_reg_salidas.place(x=40, y=85)
    boton_inventario.place(x=40, y=135)
    boton_volver.place(x=380, y=150)

    titulo_reg = tk.Label(ventana_princ, text="Que informacion deseas ver?")
    titulo_reg.place(x=210, y=13)
    titulo_reg.config(bg="white",
                          font=("Arial Black",12))

def show_intransit_interfaz():
    clear_window()

    boton_agregar_int.place(x=150, y=100)
    boton_registo_int.place(x=280, y=100)
    #boton_recibo_material.place(x=200, y=100)
    boton_volver.place(x=390, y=153)

    titulo_intransit = tk.Label(ventana_princ, text="Que movimiento deseas realizar en Intransit?")
    titulo_intransit.place(x=75, y=10)
    titulo_intransit.config(bg="white",
                                font=("Arial Black",10))


def show_agregar_instransit():
    clear_window()

    combo.set("")
    entry.delete(0, "end")

    combo.place(x=200, y=35)
    boton_cargar_sal.place(x=50, y=35)
    entry.place(x=200, y=75)
    boton_guardar_ints.place(x=230, y=150)
    boton_volver_main_int.place(x=300, y=150)

"""
def show_recibo_material_intransit():
    clear_window()

    combo.place(x=200, y=35)
    boton_cargar_sal.place(x=50, y=35)
    entry.place(x=200, y=75)
    boton_guardar_recibo_material.place(x=300, y=150)
    boton_volver_main_int.place(x=390, y=150)
"""
def show_consulta_accion():
    clear_window()

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
    clear_window()

    combo.place(x=200, y=35)
    boton_selec_prod_in_int.place(x=50, y=35)
    stock_int.place(x=200, y=95)
    boton_consultar_in_intransit.place(x=250, y=150)
    boton_volver_consultas.place(x=360, y=150)

def materiales_alta_baja_delete():
    clear_window()

    boton_alta_producto.place(x=100, y=90)
    boton_actualizar_producto.place(x=220, y=90)
    boton_baja_producto.place(x=340, y=90)
    boton_volver.place(x=340, y=150)
    
        
def baja_materiales():
    clear_window()
  
    no_parte_interno_del.place(x=250, y=60)
    material_label = tk.Label(ventana_princ, text="Numero de parte interno")
    material_label.place(x=50, y=60)
    material_label.config(bg="white",
                         font=("Arial Black",10))

    nombre_producto_del.place(x=580, y=60)
    material_label_1 = tk.Label(ventana_princ, text="Nombre del producto")
    material_label_1.place(x=400, y=60)
    material_label_1.config(bg="white",
                         font=("Arial Black",10))
    
    no_parte_del.place(x=930, y=60)
    material_label_2 = tk.Label(ventana_princ, text="Numero de parte")
    material_label_2.place(x=790, y=60)
    material_label_2.config(bg="white",
                         font=("Arial Black",10))

    presentancion_del.place(x=170, y=120)
    material_label_3 = tk.Label(ventana_princ, text="Presentacion")
    material_label_3.place(x=50, y=120)
    material_label_3.config(bg="white",
                         font=("Arial Black",10))

    stock_del.place(x=390, y=120)
    material_label_4 = tk.Label(ventana_princ, text="Stock")
    material_label_4.place(x=320, y=120)
    material_label_4.config(bg="white",
                         font=("Arial Black",10))

    precio_unitario_del.place(x=675, y=120)
    material_label_5 = tk.Label(ventana_princ, text="Precio unitario")
    material_label_5.place(x=540, y=120)
    material_label_5.config(bg="white",
                         font=("Arial Black",10))

    moneda_del.place(x=130, y=180)
    material_label_6 = tk.Label(ventana_princ, text="Moneda")
    material_label_6.place(x=50, y=180)
    material_label_6.config(bg="white",
                         font=("Arial Black",10))

    lead_time_del.place(x=370, y=180)
    material_label_7 = tk.Label(ventana_princ, text="Lead time")
    material_label_7.place(x=270, y=180)
    material_label_7.config(bg="white",
                         font=("Arial Black",10))

    demanda_diaria_del.place(x=650, y=180)
    material_label_8 = tk.Label(ventana_princ, text="Demanda diaria")
    material_label_8.place(x=510, y=180)
    material_label_8.config(bg="white",
                         font=("Arial Black",10))

    min_del.place(x=840, y=180)
    material_label_9 = tk.Label(ventana_princ, text="Min")
    material_label_9.place(x=790, y=180)
    material_label_9.config(bg="white",
                         font=("Arial Black",10))

    punto_reorden_del.place(x=950, y=120)
    material_label_10 = tk.Label(ventana_princ, text="Punto Reorden")
    material_label_10.place(x=820, y=120)
    material_label_10.config(bg="white",
                         font=("Arial Black",10))

    max_del.place(x=100, y=240)
    material_label_11 = tk.Label(ventana_princ, text="Max")
    material_label_11.place(x=50, y=240)
    material_label_11.config(bg="white",
                         font=("Arial Black",10))
    
    dias_del.place(x=305, y=240)
    material_label_12 = tk.Label(ventana_princ, text="Dias")
    material_label_12.place(x=250, y=240)
    material_label_12.config(bg="white",
                         font=("Arial Black",10))

    Accion_del.place(x=530, y=240)
    material_label_13 = tk.Label(ventana_princ, text="Accion")
    material_label_13.place(x=450, y=240)
    material_label_13.config(bg="white",
                         font=("Arial Black",10))

    Qty_to_Order_del.place(x=730, y=240)
    material_label_14 = tk.Label(ventana_princ, text="Qty")
    material_label_14.place(x=680, y=240)
    material_label_14.config(bg="white",
                         font=("Arial Black",10))

    intran_del.place(x=950, y=240)
    material_label_15 = tk.Label(ventana_princ, text="Intran")
    material_label_15.place(x=880, y=240)
    material_label_15.config(bg="white",
                         font=("Arial Black",10))

    comentarios_de_po_del.place(x=210, y=300)
    material_label_16 = tk.Label(ventana_princ, text="Comentarios de po")
    material_label_16.place(x=50, y=300)
    material_label_16.config(bg="white",
                         font=("Arial Black",10))

    notas_del.place(x=430, y=300)
    material_label_17 = tk.Label(ventana_princ, text="Notas")
    material_label_17.place(x=360, y=300)
    material_label_17.config(bg="white",
                         font=("Arial Black",10))

    no_proveedor_del.place(x=730, y=300)
    material_label_18 = tk.Label(ventana_princ, text="No. de Proveedor")
    material_label_18.place(x=580, y=300)
    material_label_18.config(bg="white",
                         font=("Arial Black",10))

    proveedor_del.place(x=980, y=300)
    material_label_19 = tk.Label(ventana_princ, text="Proveedor")
    material_label_19.place(x=880, y=300)
    material_label_19.config(bg="white",
                         font=("Arial Black",10))

    contacto_del.place(x=140, y=360)
    material_label_20 = tk.Label(ventana_princ, text="Contacto")
    material_label_20.place(x=50, y=360)
    material_label_20.config(bg="white",
                         font=("Arial Black",10))

    sistema_del.place(x=360, y=360)
    material_label_21 = tk.Label(ventana_princ, text="Sistema")
    material_label_21.place(x=280, y=360)
    material_label_21.config(bg="white",
                         font=("Arial Black",10))

    centro_cuenta_del.place(x=650, y=360)
    material_label_22 = tk.Label(ventana_princ, text="Centro de cuenta")
    material_label_22.place(x=500, y=360)
    material_label_22.config(bg="white",
                         font=("Arial Black",10))

    ubicacion_del.place(x=890, y=360)
    material_label_23 = tk.Label(ventana_princ, text="Ubicacion")
    material_label_23.place(x=790, y=360)
    material_label_23.config(bg="white",
                         font=("Arial Black",10))

    centro_del.place(x=120, y=420)
    material_label_24 = tk.Label(ventana_princ, text="Centro")
    material_label_24.place(x=50, y=420)
    material_label_24.config(bg="white",
                         font=("Arial Black",10))

    cuenta_del.place(x=345, y=420)
    material_label_25 = tk.Label(ventana_princ, text="Cuenta")
    material_label_25.place(x=270, y=420)
    material_label_25.config(bg="white",
                         font=("Arial Black",10))

    Orden_ubicacion_one_del.place(x=650, y=420)
    material_label_26 = tk.Label(ventana_princ, text="Orden Ubicacion 1")
    material_label_26.place(x=490, y=420)
    material_label_26.config(bg="white",
                         font=("Arial Black",10))

    Orden_ubicacion_two_del.place(x=960, y=420)
    material_label_27 = tk.Label(ventana_princ, text="Orden Ubicacion 2")
    material_label_27.place(x=800, y=420)
    material_label_27.config(bg="white",
                         font=("Arial Black",10))

    category_del.place(x=140, y=480)
    material_label_29 = tk.Label(ventana_princ, text="Categoria")
    material_label_29.place(x=50, y=480)
    material_label_29.config(bg="white",
                         font=("Arial Black",10))

    po_or_req_del.place(x=400, y=480)
    material_label_30 = tk.Label(ventana_princ, text="po or req")
    material_label_30.place(x=300, y=480)
    material_label_30.config(bg="white",
                         font=("Arial Black",10))

    boton_volver_menu_abc.place(x=1000, y=540)
    boton_para_escoger_produto_del.place(x=500, y=540)
    
    boton_eliminar_producto = tk.Button(ventana_princ, text="Eliminar Producto", command=eliminar_matrial_inventario)
    boton_eliminar_producto.place(x=700, y=540)
    
def cargar_fila_producto(producto_seleccionado):
    try:
        cursor.execute("SELECT * FROM dbo.Inventarios WHERE [Nombre_del_producto] = ?", (producto_seleccionado,))
        fila_producto = cursor.fetchone()

        if fila_producto:
            return fila_producto
        else:
            print("No se encontró ninguna fila para el producto seleccionado")
            return None
    except Exception as e:
        print(f"Error al cargar la fila del producto: {e}")
        return None

    
def ventana_lista_de_productos_del():
    def aceptar():
        producto_seleccionado = combobox_productos_del.get()
        fila_producto = cargar_fila_producto(producto_seleccionado)
        if fila_producto:
            cargar_datos_en_ventana_del(fila_producto)
            ventana_princ.deiconify()
            ventana_prod_del.destroy()

    ventana_princ.withdraw()

    ventana_prod_del = tk.Toplevel(ventana_princ)
    ventana_prod_del.title("Producto-Materiales")
    ventana_prod_del.geometry("500x200")
    ventana_prod_del.resizable(width=False, height=False)
    ventana_prod_del.config(bg="white")
    ventana_prod_del.iconbitmap("avion.ico")

    combobox_productos_del = ttk.Combobox(ventana_prod_del)
    combobox_productos_del.place(x=250, y=50)
    combobox_productos_del.config(font=("Arial Black", 10))

    try:
        cursor.execute("SELECT [Nombre_del_producto] FROM dbo.Inventarios")
        datos = [fila.Nombre_del_producto for fila in cursor.fetchall()]
        combobox_productos_del['values'] = tuple(datos)
    except Exception as e:
        print(f"Error al cargar productos: {e}")

    subtitulo = tk.Label(ventana_prod_del, text="Seleccione el producto")
    subtitulo.place(x=50, y=50)
    subtitulo.config(bg="white", font=("Arial Black", 10))

    boton_aceptar = tk.Button(ventana_prod_del, text="Aceptar", command=aceptar)
    boton_aceptar.place(x=200, y=100)
    

def limpiar_campos_del():
    no_parte_interno_del.delete(0, tk.END)
    nombre_producto_del.delete(0, tk.END)
    no_parte_del.delete(0, tk.END)
    presentancion_del.delete(0, tk.END)
    stock_del.delete(0, tk.END)
    precio_unitario_del.delete(0, tk.END)
    moneda_del.delete(0, tk.END)
    lead_time_del.delete(0, tk.END)
    demanda_diaria_del.delete(0, tk.END)
    min_del.delete(0, tk.END)
    punto_reorden_del.delete(0, tk.END)
    max_del.delete(0, tk.END)
    dias_del.delete(0, tk.END)
    Accion_del.delete(0, tk.END)
    Qty_to_Order_del.delete(0, tk.END)
    intran_del.delete(0, tk.END)
    comentarios_de_po_del.delete(0, tk.END)
    notas_del.delete(0, tk.END)
    no_proveedor_del.delete(0, tk.END)
    proveedor_del.delete(0, tk.END)
    contacto_del.delete(0, tk.END)
    sistema_del.delete(0, tk.END)
    centro_cuenta_del.delete(0, tk.END)
    ubicacion_del.delete(0, tk.END)
    centro_del.delete(0, tk.END)
    cuenta_del.delete(0, tk.END)
    Orden_ubicacion_one_del.delete(0, tk.END)
    Orden_ubicacion_two_del.delete(0, tk.END)
    category_del.delete(0, tk.END)
    po_or_req_del.delete(0, tk.END) 

    
def cargar_datos_en_ventana_del(fila_del_producto):
    limpiar_campos_del() 

    no_parte_interno_del.insert(0, str(fila_del_producto.No_parte_interno))
    nombre_producto_del.insert(0, str(fila_del_producto.Nombre_del_producto))
    no_parte_del.insert(0, str(fila_del_producto.No_Parte))
    presentancion_del.insert(0, str(fila_del_producto.Presentacion))
    stock_del.insert(0, str(fila_del_producto.stock))
    precio_unitario_del.insert(0, str(fila_del_producto.precio_unitario))
    moneda_del.insert(0, str(fila_del_producto.Moneda))
    lead_time_del.insert(0, str(fila_del_producto.Lead_Time))
    demanda_diaria_del.insert(0, str(fila_del_producto.Demanda_diaria))
    min_del.insert(0, str(fila_del_producto.Min))
    punto_reorden_del.insert(0, str(fila_del_producto.Punto_Reorden))
    max_del.insert(0, str(fila_del_producto.Max))
    dias_del.insert(0, str(fila_del_producto.Dias))
    Accion_del.insert(0, str(fila_del_producto.Accion))
    Qty_to_Order_del.insert(0, str(fila_del_producto.Qty_to_Order))
    intran_del.insert(0, str(fila_del_producto.intran))
    comentarios_de_po_del.insert(0, str(fila_del_producto.Comentarios_de_PO))
    notas_del.insert(0, str(fila_del_producto.Notas))
    no_proveedor_del.insert(0, str(fila_del_producto.No_Proveedor))
    proveedor_del.insert(0, str(fila_del_producto.Proveedor))
    contacto_del.insert(0, str(fila_del_producto.Contacto))
    sistema_del.insert(0, str(fila_del_producto.Sistema))
    centro_cuenta_del.insert(0, str(fila_del_producto.Centro_cuenta))
    ubicacion_del.insert(0, str(fila_del_producto.Ubicacion))
    centro_del.insert(0, str(fila_del_producto.Centro))
    cuenta_del.insert(0, str(fila_del_producto.Cuenta))
    Orden_ubicacion_one_del.insert(0, str(fila_del_producto.Orden_ubicacion_1))
    Orden_ubicacion_two_del.insert(0, str(fila_del_producto.Orden_ubicacion_2))
    category_del.insert(0, str(fila_del_producto.Category))
    po_or_req_del.insert(0, str(fila_del_producto.PO_or_REQ))
    
def eliminar_matrial_inventario():
     nombre_producto =  nombre_producto_del.get()
     
     if nombre_producto:
         respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este producto?")
         if respuesta:
            try:
                connection = pyodbc.connect(
                  'DRIVER={SQL Server};'
                   f'SERVER={Server};'
                   f'DATABASE={Database};'
                   f'UID={user};'
                   f'PWD={password}'
                   )
                
                cursor = connection.cursor()
                cursor.execute("DELETE FROM dbo.Inventarios WHERE Nombre_del_producto = ?", nombre_producto)
                connection.commit()
                cursor.close()
                
             
                limpiar_campos_del()
                messagebox.showinfo("Éxito", "Producto eliminado exitosamente")    
            except Exception as e:
                 messagebox.showerror("Error", f"Ocurrió un error al eliminar el producto: {e}")
         else:
            messagebox.showinfo("Cancelado", "La eliminación del producto fue cancelada")
     else:
         messagebox.showwarning("Advertencia", "Primero selecciona un producto")
           
#Funciones completas para dar de alta un nuevo material <----
def insertar_nuevo_material(datos):
    try:
        insert_material = "INSERT INTO dbo.Inventarios (No_parte_interno, Nombre_del_producto, No_Parte, Presentacion, stock, precio_unitario, Moneda,Lead_Time, Demanda_diaria, Min, Punto_Reorden, Max, Dias,Accion, Qty_to_Order,intran, Comentarios_de_PO, Notas,No_Proveedor,Proveedor,Contacto,Sistema,Centro_cuenta, Ubicacion, Centro, Cuenta, Orden_ubicacion_1, Orden_ubicacion_2,Category,PO_or_REQ )VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            
        cursor.execute(insert_material, tuple(datos.values()))
        connection.commit()
        
        messagebox.showinfo("Exito", "Datos agregados correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error al insertar los datos")


def guardar_datos_alta():
    datos = {
        'No_parte_interno': no_parte_interno_add.get(),
        'Nombre_del_producto': nombre_producto_add.get(),
        'No_Parte': no_parte_add.get(),
        'Presentacion': presentancion_add.get(),
        'stock': stock_add.get(),
        'precio_unitario': precio_unitario_add.get(),
        'Moneda': moneda_add.get(),
        'Lead_Time': lead_time_add.get(),
        'Demanda_diaria': demanda_diaria_add.get(),
        'Min': min_add.get(),
        'Punto_Reorden': punto_reorden_add.get(),
        'Max': max_add.get(),
        'Dias': dias_add.get(),
        'Accion': Accion_add.get(),
        'Qty_to_Order': Qty_to_Order_add.get(),
        'intran': intran_add.get(),
        'Comentarios_de_PO': comentarios_de_po_add.get(),
        'Notas': notas_add.get(),
        'No_Proveedor': no_proveedor_add.get(),
        'Proveedor': proveedor_add.get(),
        'Contacto': contacto_add.get(),
        'Sistema': sistema_add.get(),
        'Centro_cuenta': centro_cuenta_add.get(),
        'Ubicacion': ubicacion_add.get(),
        'Centro': centro_add.get(),
        'Cuenta': cuenta_add.get(),
        'Orden_ubicacion_1': Orden_ubicacion_one_add.get(),
        'Orden_ubicacion_2': Orden_ubicacion_two_add.get(),
        'Category': category_add.get(),
        'PO_or_REQ': po_or_req_add.get()
    }

    insertar_nuevo_material(datos)

def alta_materiales():
    clear_window()

    no_parte_interno_add.place(x=250, y=60)
    material_label = tk.Label(ventana_princ, text="Numero de parte interno")
    material_label.place(x=50, y=60)
    material_label.config(bg="white",
                         font=("Arial Black",10))

    nombre_producto_add.place(x=580, y=60)
    material_label_1 = tk.Label(ventana_princ, text="Nombre del producto")
    material_label_1.place(x=400, y=60)
    material_label_1.config(bg="white",
                         font=("Arial Black",10))
    
    no_parte_add.place(x=900, y=60)
    material_label_2 = tk.Label(ventana_princ, text="Numero de parte")
    material_label_2.place(x=730, y=60)
    material_label_2.config(bg="white",
                         font=("Arial Black",10))

    presentancion_add.place(x=170, y=120)
    material_label_3 = tk.Label(ventana_princ, text="Presentacion")
    material_label_3.place(x=50, y=120)
    material_label_3.config(bg="white",
                         font=("Arial Black",10))

    stock_add.place(x=390, y=120)
    material_label_4 = tk.Label(ventana_princ, text="Stock")
    material_label_4.place(x=320, y=120)
    material_label_4.config(bg="white",
                         font=("Arial Black",10))

    precio_unitario_add.place(x=675, y=120)
    material_label_5 = tk.Label(ventana_princ, text="Precio unitario")
    material_label_5.place(x=540, y=120)
    material_label_5.config(bg="white",
                         font=("Arial Black",10))

    moneda_add.place(x=130, y=180)
    material_label_6 = tk.Label(ventana_princ, text="Moneda")
    material_label_6.place(x=50, y=180)
    material_label_6.config(bg="white",
                         font=("Arial Black",10))

    lead_time_add.place(x=370, y=180)
    material_label_7 = tk.Label(ventana_princ, text="Lead time")
    material_label_7.place(x=270, y=180)
    material_label_7.config(bg="white",
                         font=("Arial Black",10))

    demanda_diaria_add.place(x=650, y=180)
    material_label_8 = tk.Label(ventana_princ, text="Demanda diaria")
    material_label_8.place(x=510, y=180)
    material_label_8.config(bg="white",
                         font=("Arial Black",10))

    min_add.place(x=840, y=180)
    material_label_9 = tk.Label(ventana_princ, text="Min")
    material_label_9.place(x=790, y=180)
    material_label_9.config(bg="white",
                         font=("Arial Black",10))

    punto_reorden_add.place(x=950, y=120)
    material_label_10 = tk.Label(ventana_princ, text="Punto Reorden")
    material_label_10.place(x=820, y=120)
    material_label_10.config(bg="white",
                         font=("Arial Black",10))

    max_add.place(x=100, y=240)
    material_label_11 = tk.Label(ventana_princ, text="Max")
    material_label_11.place(x=50, y=240)
    material_label_11.config(bg="white",
                         font=("Arial Black",10))
    
    dias_add.place(x=305, y=240)
    material_label_12 = tk.Label(ventana_princ, text="Dias")
    material_label_12.place(x=250, y=240)
    material_label_12.config(bg="white",
                         font=("Arial Black",10))

    Accion_add.place(x=530, y=240)
    material_label_13 = tk.Label(ventana_princ, text="Accion")
    material_label_13.place(x=450, y=240)
    material_label_13.config(bg="white",
                         font=("Arial Black",10))

    Qty_to_Order_add.place(x=730, y=240)
    material_label_14 = tk.Label(ventana_princ, text="Qty")
    material_label_14.place(x=680, y=240)
    material_label_14.config(bg="white",
                         font=("Arial Black",10))

    intran_add.place(x=950, y=240)
    material_label_15 = tk.Label(ventana_princ, text="Intran")
    material_label_15.place(x=880, y=240)
    material_label_15.config(bg="white",
                         font=("Arial Black",10))

    comentarios_de_po_add.place(x=210, y=300)
    material_label_16 = tk.Label(ventana_princ, text="Comentarios de po")
    material_label_16.place(x=50, y=300)
    material_label_16.config(bg="white",
                         font=("Arial Black",10))

    notas_add.place(x=430, y=300)
    material_label_17 = tk.Label(ventana_princ, text="Notas")
    material_label_17.place(x=360, y=300)
    material_label_17.config(bg="white",
                         font=("Arial Black",10))

    no_proveedor_add.place(x=730, y=300)
    material_label_18 = tk.Label(ventana_princ, text="No. de Proveedor")
    material_label_18.place(x=580, y=300)
    material_label_18.config(bg="white",
                         font=("Arial Black",10))

    proveedor_add.place(x=980, y=300)
    material_label_19 = tk.Label(ventana_princ, text="Proveedor")
    material_label_19.place(x=880, y=300)
    material_label_19.config(bg="white",
                         font=("Arial Black",10))

    contacto_add.place(x=140, y=360)
    material_label_20 = tk.Label(ventana_princ, text="Contacto")
    material_label_20.place(x=50, y=360)
    material_label_20.config(bg="white",
                         font=("Arial Black",10))

    sistema_add.place(x=360, y=360)
    material_label_21 = tk.Label(ventana_princ, text="Sistema")
    material_label_21.place(x=280, y=360)
    material_label_21.config(bg="white",
                         font=("Arial Black",10))

    centro_cuenta_add.place(x=650, y=360)
    material_label_22 = tk.Label(ventana_princ, text="Centro de cuenta")
    material_label_22.place(x=500, y=360)
    material_label_22.config(bg="white",
                         font=("Arial Black",10))

    ubicacion_add.place(x=890, y=360)
    material_label_23 = tk.Label(ventana_princ, text="Ubicacion")
    material_label_23.place(x=790, y=360)
    material_label_23.config(bg="white",
                         font=("Arial Black",10))

    centro_add.place(x=120, y=420)
    material_label_24 = tk.Label(ventana_princ, text="Centro")
    material_label_24.place(x=50, y=420)
    material_label_24.config(bg="white",
                         font=("Arial Black",10))

    cuenta_add.place(x=345, y=420)
    material_label_25 = tk.Label(ventana_princ, text="Cuenta")
    material_label_25.place(x=270, y=420)
    material_label_25.config(bg="white",
                         font=("Arial Black",10))

    Orden_ubicacion_one_add.place(x=650, y=420)
    material_label_26 = tk.Label(ventana_princ, text="Orden Ubicacion 1")
    material_label_26.place(x=490, y=420)
    material_label_26.config(bg="white",
                         font=("Arial Black",10))

    Orden_ubicacion_two_add.place(x=960, y=420)
    material_label_27 = tk.Label(ventana_princ, text="Orden Ubicacion 2")
    material_label_27.place(x=800, y=420)
    material_label_27.config(bg="white",
                         font=("Arial Black",10))

    category_add.place(x=140, y=480)
    material_label_29 = tk.Label(ventana_princ, text="Categoria")
    material_label_29.place(x=50, y=480)
    material_label_29.config(bg="white",
                         font=("Arial Black",10))

    po_or_req_add.place(x=400, y=480)
    material_label_30 = tk.Label(ventana_princ, text="po or req")
    material_label_30.place(x=300, y=480)
    material_label_30.config(bg="white",
                         font=("Arial Black",10))

    boton_volver_menu_abc.place(x=1000, y=540)
    boton_guardar_alta_material.place(x=900, y=540)
    


def update_materiales():
    clear_window()

    no_parte_interno_upd.place(x=250, y=60)
    material_label = tk.Label(ventana_princ, text="Numero de parte interno")
    material_label.place(x=50, y=60)
    material_label.config(bg="white",
                         font=("Arial Black",10))

    nombre_producto_upd.place(x=580, y=60)
    material_label_1 = tk.Label(ventana_princ, text="Nombre del producto")
    material_label_1.place(x=400, y=60)
    material_label_1.config(bg="white",
                         font=("Arial Black",10))
    
    no_parte_upd.place(x=900, y=60)
    material_label_2 = tk.Label(ventana_princ, text="Numero de parte")
    material_label_2.place(x=730, y=60)
    material_label_2.config(bg="white",
                         font=("Arial Black",10))

    presentancion_upd.place(x=170, y=120)
    material_label_3 = tk.Label(ventana_princ, text="Presentacion")
    material_label_3.place(x=50, y=120)
    material_label_3.config(bg="white",
                         font=("Arial Black",10))

    stock_upd.place(x=390, y=120)
    material_label_4 = tk.Label(ventana_princ, text="Stock")
    material_label_4.place(x=320, y=120)
    material_label_4.config(bg="white",
                         font=("Arial Black",10))

    precio_unitario_upd.place(x=675, y=120)
    material_label_5 = tk.Label(ventana_princ, text="Precio unitario")
    material_label_5.place(x=540, y=120)
    material_label_5.config(bg="white",
                         font=("Arial Black",10))

    moneda_upd.place(x=130, y=180)
    material_label_6 = tk.Label(ventana_princ, text="Moneda")
    material_label_6.place(x=50, y=180)
    material_label_6.config(bg="white",
                         font=("Arial Black",10))

    lead_time_upd.place(x=370, y=180)
    material_label_7 = tk.Label(ventana_princ, text="Lead time")
    material_label_7.place(x=270, y=180)
    material_label_7.config(bg="white",
                         font=("Arial Black",10))

    demanda_diaria_upd.place(x=650, y=180)
    material_label_8 = tk.Label(ventana_princ, text="Demanda diaria")
    material_label_8.place(x=510, y=180)
    material_label_8.config(bg="white",
                         font=("Arial Black",10))

    min_upd.place(x=840, y=180)
    material_label_9 = tk.Label(ventana_princ, text="Min")
    material_label_9.place(x=790, y=180)
    material_label_9.config(bg="white",
                         font=("Arial Black",10))

    punto_reorden_upd.place(x=950, y=120)
    material_label_10 = tk.Label(ventana_princ, text="Punto Reorden")
    material_label_10.place(x=820, y=120)
    material_label_10.config(bg="white",
                         font=("Arial Black",10))

    max_upd.place(x=100, y=240)
    material_label_11 = tk.Label(ventana_princ, text="Max")
    material_label_11.place(x=50, y=240)
    material_label_11.config(bg="white",
                         font=("Arial Black",10))
    
    dias_upd.place(x=305, y=240)
    material_label_12 = tk.Label(ventana_princ, text="Dias")
    material_label_12.place(x=250, y=240)
    material_label_12.config(bg="white",
                         font=("Arial Black",10))

    Accion_upd.place(x=530, y=240)
    material_label_13 = tk.Label(ventana_princ, text="Accion")
    material_label_13.place(x=450, y=240)
    material_label_13.config(bg="white",
                         font=("Arial Black",10))

    Qty_to_Order_upd.place(x=730, y=240)
    material_label_14 = tk.Label(ventana_princ, text="Qty")
    material_label_14.place(x=680, y=240)
    material_label_14.config(bg="white",
                         font=("Arial Black",10))

    intran_upd.place(x=950, y=240)
    material_label_15 = tk.Label(ventana_princ, text="Intran")
    material_label_15.place(x=880, y=240)
    material_label_15.config(bg="white",
                         font=("Arial Black",10))

    comentarios_de_po_upd.place(x=210, y=300)
    material_label_16 = tk.Label(ventana_princ, text="Comentarios de po")
    material_label_16.place(x=50, y=300)
    material_label_16.config(bg="white",
                         font=("Arial Black",10))

    notas_upd.place(x=430, y=300)
    material_label_17 = tk.Label(ventana_princ, text="Notas")
    material_label_17.place(x=360, y=300)
    material_label_17.config(bg="white",
                         font=("Arial Black",10))

    no_proveedor_upd.place(x=730, y=300)
    material_label_18 = tk.Label(ventana_princ, text="No. de Proveedor")
    material_label_18.place(x=580, y=300)
    material_label_18.config(bg="white",
                         font=("Arial Black",10))

    proveedor_upd.place(x=980, y=300)
    material_label_19 = tk.Label(ventana_princ, text="Proveedor")
    material_label_19.place(x=880, y=300)
    material_label_19.config(bg="white",
                         font=("Arial Black",10))

    contacto_upd.place(x=140, y=360)
    material_label_20 = tk.Label(ventana_princ, text="Contacto")
    material_label_20.place(x=50, y=360)
    material_label_20.config(bg="white",
                         font=("Arial Black",10))

    sistema_upd.place(x=360, y=360)
    material_label_21 = tk.Label(ventana_princ, text="Sistema")
    material_label_21.place(x=280, y=360)
    material_label_21.config(bg="white",
                         font=("Arial Black",10))

    centro_cuenta_upd.place(x=650, y=360)
    material_label_22 = tk.Label(ventana_princ, text="Centro de cuenta")
    material_label_22.place(x=500, y=360)
    material_label_22.config(bg="white",
                         font=("Arial Black",10))

    ubicacion_upd.place(x=890, y=360)
    material_label_23 = tk.Label(ventana_princ, text="Ubicacion")
    material_label_23.place(x=790, y=360)
    material_label_23.config(bg="white",
                         font=("Arial Black",10))

    centro_upd.place(x=120, y=420)
    material_label_24 = tk.Label(ventana_princ, text="Centro")
    material_label_24.place(x=50, y=420)
    material_label_24.config(bg="white",
                         font=("Arial Black",10))

    cuenta_upd.place(x=345, y=420)
    material_label_25 = tk.Label(ventana_princ, text="Cuenta")
    material_label_25.place(x=270, y=420)
    material_label_25.config(bg="white",
                         font=("Arial Black",10))

    Orden_ubicacion_one_upd.place(x=650, y=420)
    material_label_26 = tk.Label(ventana_princ, text="Orden Ubicacion 1")
    material_label_26.place(x=490, y=420)
    material_label_26.config(bg="white",
                         font=("Arial Black",10))

    Orden_ubicacion_two_upd.place(x=960, y=420)
    material_label_27 = tk.Label(ventana_princ, text="Orden Ubicacion 2")
    material_label_27.place(x=800, y=420)
    material_label_27.config(bg="white",
                         font=("Arial Black",10))

    category_upd.place(x=140, y=480)
    material_label_28 = tk.Label(ventana_princ, text="Categoria")
    material_label_28.place(x=50, y=480)
    material_label_28.config(bg="white",
                         font=("Arial Black",10))

    po_or_req_upd.place(x=400, y=480)
    material_label_29 = tk.Label(ventana_princ, text="po or req")
    material_label_29.place(x=300, y=480)
    material_label_29.config(bg="white",
                         font=("Arial Black",10))

    boton_volver_menu_abc.place(x=1000, y=540)
    
    boton_para_escoger_produto_upd = tk.Button(ventana_princ, text="Lista de productos", command=ventana_lista_de_productos_upd)
    boton_para_escoger_produto_upd.place(x=100, y=540)
    
    boton_actualizar = tk.Button(ventana_princ, text="Actualizar", command=update_material)
    boton_actualizar.place(x=600, y=540)
    
def ventana_lista_de_productos_upd():
    def aceptar_upd():
        producto_seleccionado = combobox_productos_upd.get()
        fila_producto = cargar_fila_producto(producto_seleccionado)
        
        if fila_producto:
            cargar_datos_en_ventana_upd(fila_producto)
            ventana_princ.deiconify()
            ventana_prod_upd.destroy()

    ventana_princ.withdraw()

    ventana_prod_upd = tk.Toplevel(ventana_princ)
    ventana_prod_upd.title("Producto-Materiales")
    ventana_prod_upd.geometry("500x200")
    ventana_prod_upd.resizable(width=False, height=False)
    ventana_prod_upd.config(bg="white")
    ventana_prod_upd.iconbitmap("avion.ico")

    combobox_productos_upd = ttk.Combobox(ventana_prod_upd)
    combobox_productos_upd.place(x=250, y=50)
    combobox_productos_upd.config(font=("Arial Black", 10))

    try:
        cursor.execute("SELECT [Nombre_del_producto] FROM dbo.Inventarios")
        datos = [fila.Nombre_del_producto for fila in cursor.fetchall()]
        combobox_productos_upd['values'] = tuple(datos)
    except Exception as e:
        print(f"Error al cargar productos: {e}")

    subtitulo = tk.Label(ventana_prod_upd, text="Seleccione el producto")
    subtitulo.place(x=50, y=50)
    subtitulo.config(bg="white", font=("Arial Black", 10))

    boton_aceptar = tk.Button(ventana_prod_upd, text="Aceptar", command=aceptar_upd)
    boton_aceptar.place(x=200, y=100)
    
def limpiar_campos_upd():
    campos = [
        no_parte_interno_upd, nombre_producto_upd, no_parte_upd, presentancion_upd, stock_upd,
        precio_unitario_upd, moneda_upd, lead_time_upd, demanda_diaria_upd, min_upd,
        punto_reorden_upd, max_upd, dias_upd, Accion_upd, Qty_to_Order_upd,
        intran_upd, comentarios_de_po_upd, notas_upd, no_proveedor_upd,
        proveedor_upd, contacto_upd, sistema_upd, centro_cuenta_upd,
        ubicacion_upd, centro_upd, cuenta_upd, Orden_ubicacion_one_upd,
        Orden_ubicacion_two_upd, category_upd, po_or_req_upd
    ]
    
    for campo in campos:
        campo.delete(0, tk.END)
    
def cargar_datos_en_ventana_upd(fila_del_producto):
    limpiar_campos_upd() 

    no_parte_interno_upd.insert(0, str(fila_del_producto.No_parte_interno))
    nombre_producto_upd.insert(0, str(fila_del_producto.Nombre_del_producto))
    no_parte_upd.insert(0, str(fila_del_producto.No_Parte))
    presentancion_upd.insert(0, str(fila_del_producto.Presentacion))
    stock_upd.config(state='normal')
    stock_upd.insert(0, str(fila_del_producto.stock))
    stock_upd.config(state='readonly')
    precio_unitario_upd.insert(0, str(fila_del_producto.precio_unitario))
    moneda_upd.insert(0, str(fila_del_producto.Moneda))
    lead_time_upd.insert(0, str(fila_del_producto.Lead_Time))
    demanda_diaria_upd.insert(0, str(fila_del_producto.Demanda_diaria))
    min_upd.insert(0, str(fila_del_producto.Min))
    punto_reorden_upd.insert(0, str(fila_del_producto.Punto_Reorden))
    max_upd.insert(0, str(fila_del_producto.Max))
    dias_upd.insert(0, str(fila_del_producto.Dias))
    Accion_upd.insert(0, str(fila_del_producto.Accion))
    Qty_to_Order_upd.insert(0, str(fila_del_producto.Qty_to_Order))
    intran_upd.insert(0, str(fila_del_producto.intran))
    comentarios_de_po_upd.insert(0, str(fila_del_producto.Comentarios_de_PO))
    notas_upd.insert(0, str(fila_del_producto.Notas))
    no_proveedor_upd.insert(0, str(fila_del_producto.No_Proveedor))
    proveedor_upd.insert(0, str(fila_del_producto.Proveedor))
    contacto_upd.insert(0, str(fila_del_producto.Contacto))
    sistema_upd.insert(0, str(fila_del_producto.Sistema))
    centro_cuenta_upd.insert(0, str(fila_del_producto.Centro_cuenta))
    ubicacion_upd.insert(0, str(fila_del_producto.Ubicacion))
    centro_upd.insert(0, str(fila_del_producto.Centro))
    cuenta_upd.insert(0, str(fila_del_producto.Cuenta))
    Orden_ubicacion_one_upd.insert(0, str(fila_del_producto.Orden_ubicacion_1))
    Orden_ubicacion_two_upd.insert(0, str(fila_del_producto.Orden_ubicacion_2))
    category_upd.insert(0, str(fila_del_producto.Category))
    po_or_req_upd.insert(0, str(fila_del_producto.PO_or_REQ))

def update_material():
    try:
        cursor = connection.cursor()

        valores = (
            no_parte_interno_upd.get(), 
            nombre_producto_upd.get(), 
            no_parte_upd.get(), 
            presentancion_upd.get(),
            float(stock_upd.get()), 
            float(precio_unitario_upd.get()), 
            moneda_upd.get(), 
            float(lead_time_upd.get()), 
            float(demanda_diaria_upd.get()),
            float(min_upd.get()), 
            float(punto_reorden_upd.get()),  
            float(max_upd.get()), 
            float(dias_upd.get()), 
            Accion_upd.get(), 
            float(Qty_to_Order_upd.get()),  
            intran_upd.get(),
            comentarios_de_po_upd.get(), 
            notas_upd.get(), 
            no_proveedor_upd.get(), 
            proveedor_upd.get(),
            contacto_upd.get(), 
            sistema_upd.get(), 
            centro_cuenta_upd.get(), 
            ubicacion_upd.get(),
            centro_upd.get(), 
            cuenta_upd.get(), 
            Orden_ubicacion_one_upd.get(), 
            Orden_ubicacion_two_upd.get(),
            category_upd.get(), 
            po_or_req_upd.get(), 
            nombre_producto_upd.get()
        )

        query = """
            UPDATE dbo.Inventarios
            SET No_parte_interno = ?, Nombre_del_producto = ?, No_Parte = ?, Presentacion = ?, stock = ?, precio_unitario = ?, Moneda = ?, Lead_Time = ?, Demanda_diaria = ?, Min = ?, Punto_Reorden = ?, Max = ?, Dias = ?, Accion = ?, Qty_to_Order = ?, intran = ?, Comentarios_de_PO = ?, Notas = ?, No_Proveedor = ?, Proveedor = ?, Contacto = ?, Sistema = ?, Centro_cuenta = ?, Ubicacion = ?, Centro = ?, Cuenta = ?, Orden_ubicacion_1 = ?, Orden_ubicacion_2 = ?, Category = ?, PO_or_REQ = ?
            WHERE Nombre_del_producto = ?
        """

        cursor.execute(query, valores)
        connection.commit()
        messagebox.showinfo("Éxito", "Producto actualizado correctamente")

    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar el producto: {e}")
        print(f"Error al actualizar el producto: {e}")

    finally:
        cursor.close()


#funcion para guardar stock entrada
def guardar_entrada():
    nombre_del_producto = combo.get()
    cantidad = entry.get()

    if nombre_del_producto and cantidad:
        try:
            cantidad = int(cantidad)
            cursor.execute("UPDATE dbo.Inventarios SET stock = stock + ? WHERE Nombre_del_producto = ?", (cantidad, nombre_del_producto))
            cursor.execute("SELECT stock, Punto_Reorden FROM dbo.Inventarios WHERE Nombre_del_producto = ?", (nombre_del_producto,))
            resultado_ent = cursor.fetchone()
            
            if resultado_ent:
                stock_actual, punto_de_reorden = resultado_ent
                cursor.execute("INSERT INTO dbo.Entradas (nombre_del_producto, stock_actual, entrada, fecha) VALUES (?, ?, ?, GETDATE())",
                               (nombre_del_producto, stock_actual, cantidad))
                if stock_actual > punto_de_reorden:
                    cursor.execute("UPDATE dbo.Inventarios SET Accion = 'Cantidad Suficiente' WHERE Nombre_del_producto = ?", (nombre_del_producto,))
                connection.commit()
                messagebox.showinfo("Éxito", "Entrada guardada correctamente")
            else:
                messagebox.showerror("Error", "Producto no encontrado en el inventario")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    else:
        messagebox.showerror("Error", "Por favor, selecciona un producto e ingresa una cantidad.")

#funcion para guardar stock Salida
def guardar_salida():
    nombre_del_producto_sal = combo.get()
    cantidad_sal = entry.get()

    if nombre_del_producto_sal and cantidad_sal:
        try:
            cantidad_sal = int(cantidad_sal)
            cursor.execute("UPDATE dbo.Inventarios SET stock = stock - ? WHERE Nombre_del_producto = ?", (cantidad_sal, nombre_del_producto_sal))
            cursor.execute("SELECT stock, Punto_Reorden FROM dbo.Inventarios WHERE Nombre_del_producto = ?", (nombre_del_producto_sal,))
            resultado = cursor.fetchone()

            if resultado:
                stock_actual, punto_de_reorden = resultado
                cursor.execute("INSERT INTO dbo.Salidas (nombre_del_producto, stock_actual, salida, fecha) VALUES (?, ?, ?, GETDATE())",
                               (nombre_del_producto_sal, stock_actual, cantidad_sal))
                if stock_actual < punto_de_reorden:
                    cursor.execute("UPDATE dbo.Inventarios SET Accion = 'Comprar' WHERE Nombre_del_producto = ?", (nombre_del_producto_sal,))
                connection.commit()
                messagebox.showinfo("Éxito", "Salida guardada correctamente")
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

"""
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
"""
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

    if resultado is not None:
        intransit = resultado[0] if resultado[0] is not None else 0
        stock_int.delete(0, tk.END)
        stock_int.insert(0, intransit)
    else:
        messagebox.showerror("Error", f"Producto no encontrado")


def export_excel_inventario():
    fecha_actual_inv = datetime.datetime.now().strftime("%Y-%m-%d")
    name_file_inv = "Registros_Inventario_" + fecha_actual_inv
    try:
        query_inventario = "select * from dbo.inventarios"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_inventario, cursor)
             file_path_inv = filedialog.asksaveasfilename(initialfile = name_file_inv, defaultextension='xlsx',
                                                          filetypes=[("Excel files", "*.xlsx")])
             if file_path_inv == "":
                messagebox.showinfo("Informacion", "Informacion Cancelada sin guardar!")
                return

             df_i.to_excel(file_path_inv, index=False)
             messagebox.showinfo("Exito!", "Informacion guardada correctamente")

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion del inventario a excel: {str(e)}")

def export_excel_entradas():
    fecha_actual_ent = datetime.datetime.now().strftime("%Y-%m-%d")
    name_file_ent = "Registro_Entadas_" + fecha_actual_ent
    try:
        query_entradas = "select * from dbo.entradas;"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_entradas, cursor)
             file_path_ent = filedialog.asksaveasfilename(initialfile = name_file_ent, defaultextension='xlsx',
                                                          filetypes=[("Excel files", "*.xlsx")])
             if  file_path_ent == "":
                 messagebox.showinfo("Informacion", "Informacion Cancelada sin guardar!")
                 return

             df_i.to_excel(file_path_ent, index=False)
             messagebox.showinfo("Exito", "Informacion exportada a Excel correctamente!")

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion de las entradas a excel: {str(e)}")

def export_excel_salidas():
    fecha_actual_sal = datetime.datetime.now().strftime("%Y-%m-%d")
    name_file_sal = "Registro_Salidas_" + fecha_actual_sal 
    try:
        query_salidas = "select * from dbo.salidas"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_salidas, cursor)
             file_path_sal = filedialog.asksaveasfilename(initialfile = name_file_sal, defaultextension='xlsx',
                                                          filetypes=[("Ecel files", "*.xlsx")])
             if file_path_sal == "":
                 messagebox.showinfo("Informacion", "Informacion cancelada sin guadar!")
                 return

             df_i.to_excel(file_path_sal, index=False)
             messagebox.showinfo("Exito", "Informacion exportada correctamente!")

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion de las salidas a excel: {str(e)}")

def export_excel_intransit():
    fecha_actual_int = datetime.datetime.now().strftime("%Y-%m-%d")
    name_file_intr = "Registro_Intransit" + fecha_actual_int
    try:
        query_intransit="select * from dbo.intransit"
        with engine.begin() as cursor:
             df_i = pd.read_sql(query_intransit, cursor)
             file_path_intransit = filedialog.asksaveasfilename(initialfile=name_file_intr, defaultextension='xlsx',
                                                           filetypes=[("Excel files", "*.xlsx")])
             if file_path_intransit =="":
                 messagebox.showinfo("Informacion", "Informacion cancelada sin guardar!")
                 return

             df_i.to_excel(file_path_intransit, index=False)
             messagebox.showinfo("Exito", "Informacion guardada correctamente!")

    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar la informacion a excel: {str(e)}")


def limpiar_campos():
    combo.set("")
    stock_textbox.delete(0, "end")
    accion_textbox.delete(0, "end")
    stock_int.delete(0, "end")

def limpiar_campos_entradas_salidas():
    combo.set("")
    entry.delete(0, "end")
  
def Salir_app():
    ventana_princ.destroy()


#Interfaz principal y funciones 
ventana_princ = tk.Tk()
ventana_princ.title("Inventario Miscelaneos SFX MTY")
ventana_princ.geometry("500x200")
ventana_princ.resizable(width=False, height=False)


img = ImageTk.PhotoImage(file="stratoflex-logo.jpg")
Label(ventana_princ, image=img, anchor="nw").pack()
ventana_princ.iconbitmap("avion.ico")

#Botones de interfaz principal
boton_entradas = tk.Button(ventana_princ, text="Entradas", command=show_entradas)
boton_salidas = tk.Button(ventana_princ, text="Salidas", command=show_salidas)
boton_registros = tk.Button(ventana_princ, text="Registros", command=show_registros)
boton_salir = tk.Button(ventana_princ, text="Salir", command=Salir_app)
boton_consulta = tk.Button(ventana_princ, text="Consulta", command=show_consultas)
boton_intransit = tk.Button(ventana_princ, text="Intransit", command=show_intransit_interfaz)
boton_materiales = tk.Button(ventana_princ, text="Materiales", command=materiales_alta_baja_delete)

#Botones, combobox titulos y mas
titulo_entradas = tk.Label(ventana_princ, text="Entradas")
boton_cargar = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
entry = tk.Entry(ventana_princ)
boton_guardar = tk.Button(ventana_princ, text="Guardar", command=guardar_entrada)
boton_volver = tk.Button(ventana_princ, text="Volver", command=lambda: (limpiar_campos_entradas_salidas(), show_main()))


titulo_salidas = tk.Label(ventana_princ, text="Salidas")
boton_cargar_sal = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
boton_guardar_sal = tk.Button(ventana_princ, text="Guardar", command=guardar_salida)

boton_agregar_int = tk.Button(ventana_princ, text="Agregar a intransit", command=show_agregar_instransit)
boton_registo_int = tk.Button(ventana_princ, text="Registros", command=export_excel_intransit)
#boton_recibo_material = tk.Button(ventana_princ, text="Recibo de material")
#boton_guardar_recibo_material = tk.Button(ventana_princ, text="guardar")

boton_selec_prod_in_int = tk.Button(ventana_princ, text="Cargar informacion", command=cargar_productos)
boton_consultar_in_intransit = tk.Button(ventana_princ, text="Consultar", command=actualizacion_intransit_consulta)

boton_guardar_ints =tk.Button(ventana_princ, text="Guardar", command=guardar_intransit)
boton_volver_main_int =tk.Button(ventana_princ, text="volver", command=show_intransit_interfaz)

titulo_consultas = tk.Label(ventana_princ, text="Consultas")
boton_consultas = tk.Button(ventana_princ, text="Consulta de stock", command=show_consulta_accion)
boton_consuta_int = tk.Button(ventana_princ, text="Consulta de Intrasit", command=show_consulta_de_intransit)
boton_selec_prod_accion = tk.Button(ventana_princ, text="consultar producto", command=cargar_productos)
boton_consultar_produc_accion = tk.Button(ventana_princ, text="Consultar", command=actualizacion_stock_consulta)
boton_volver_consultas = tk.Button(ventana_princ, text="volver", command=lambda: (limpiar_campos(), show_consultas()))
accion = tk.Entry(ventana_princ)

boton_reg_entradas = tk.Button(ventana_princ, text="Registro de entradas", command=export_excel_entradas)
boton_reg_salidas = tk.Button(ventana_princ, text="Registro de Salidas", command=export_excel_salidas)
boton_inventario = tk.Button(ventana_princ, text="Inventario", command=export_excel_inventario)

boton_alta_producto = tk.Button(ventana_princ, text="Agregar", command=lambda: (tamano_ventana_uno(), alta_materiales()))
boton_baja_producto = tk.Button(ventana_princ, text="Eliminar", command=lambda: (tamano_ventana_uno(), baja_materiales()))
boton_actualizar_producto = tk.Button(ventana_princ, text="Actualizar", command=lambda: (tamano_ventana_uno(), update_materiales()))

boton_volver_menu_abc = tk.Button(ventana_princ, text="volver", command=lambda: (tamano_ventana_dos(), materiales_alta_baja_delete()))

boton_guardar_alta_material = tk.Button(ventana_princ, text="Guardar", command=guardar_datos_alta)
boton_para_escoger_produto_del = tk.Button(ventana_princ, text="Lista de productos", command=ventana_lista_de_productos_del)


#Campos de texto y etiquetas para modulo de eliminar productos
no_parte_interno_del = tk.Entry(ventana_princ)
nombre_producto_del = tk.Entry(ventana_princ)
no_parte_del = tk.Entry(ventana_princ)
presentancion_del = tk.Entry(ventana_princ)
stock_del = tk.Entry(ventana_princ)
precio_unitario_del = tk.Entry(ventana_princ)
moneda_del = tk.Entry(ventana_princ)
lead_time_del = tk.Entry(ventana_princ)
demanda_diaria_del = tk.Entry(ventana_princ)
min_del = tk.Entry(ventana_princ)
punto_reorden_del = tk.Entry(ventana_princ)
max_del = tk.Entry(ventana_princ)
dias_del = tk.Entry(ventana_princ)
Accion_del = tk.Entry(ventana_princ)
Qty_to_Order_del = tk.Entry(ventana_princ)
intran_del = tk.Entry(ventana_princ)
comentarios_de_po_del = tk.Entry(ventana_princ)
notas_del = tk.Entry(ventana_princ)
no_proveedor_del = tk.Entry(ventana_princ)
proveedor_del = tk.Entry(ventana_princ)
contacto_del = tk.Entry(ventana_princ)
sistema_del = tk.Entry(ventana_princ)
centro_cuenta_del = tk.Entry(ventana_princ)
ubicacion_del = tk.Entry(ventana_princ)
centro_del = tk.Entry(ventana_princ)
cuenta_del = tk.Entry(ventana_princ)
Orden_ubicacion_one_del = tk.Entry(ventana_princ)
Orden_ubicacion_two_del = tk.Entry(ventana_princ)
category_del = tk.Entry(ventana_princ)
po_or_req_del = tk.Entry(ventana_princ)
#------------------------------------------------------------------------------

#Campos de texto y etiquetas para modulo de agregar productos
no_parte_interno_add = tk.Entry(ventana_princ)
nombre_producto_add = tk.Entry(ventana_princ)
no_parte_add = tk.Entry(ventana_princ)
presentancion_add = tk.Entry(ventana_princ)
stock_add = tk.Entry(ventana_princ)
precio_unitario_add = tk.Entry(ventana_princ)
moneda_add = tk.Entry(ventana_princ)
lead_time_add = tk.Entry(ventana_princ)
demanda_diaria_add = tk.Entry(ventana_princ)
min_add = tk.Entry(ventana_princ)
punto_reorden_add = tk.Entry(ventana_princ)
max_add = tk.Entry(ventana_princ)
dias_add = tk.Entry(ventana_princ)
Accion_add = tk.Entry(ventana_princ)
Qty_to_Order_add = tk.Entry(ventana_princ)
intran_add = tk.Entry(ventana_princ)
comentarios_de_po_add = tk.Entry(ventana_princ)
notas_add = tk.Entry(ventana_princ)
no_proveedor_add = tk.Entry(ventana_princ)
proveedor_add = tk.Entry(ventana_princ)
contacto_add = tk.Entry(ventana_princ)
sistema_add = tk.Entry(ventana_princ)
centro_cuenta_add = tk.Entry(ventana_princ)
ubicacion_add = tk.Entry(ventana_princ)
centro_add = tk.Entry(ventana_princ)
cuenta_add = tk.Entry(ventana_princ)
Orden_ubicacion_one_add = tk.Entry(ventana_princ)
Orden_ubicacion_two_add = tk.Entry(ventana_princ)
category_add = tk.Entry(ventana_princ)
po_or_req_add = tk.Entry(ventana_princ)
#------------------------------------------------------------

#Campos de texto y etiquetas para modulo de actualizar productos
no_parte_interno_upd = tk.Entry(ventana_princ)
nombre_producto_upd = tk.Entry(ventana_princ)
no_parte_upd = tk.Entry(ventana_princ)
presentancion_upd = tk.Entry(ventana_princ)
stock_upd = tk.Entry(ventana_princ)
precio_unitario_upd = tk.Entry(ventana_princ)
moneda_upd = tk.Entry(ventana_princ)
lead_time_upd = tk.Entry(ventana_princ)
demanda_diaria_upd = tk.Entry(ventana_princ)
min_upd = tk.Entry(ventana_princ)
punto_reorden_upd = tk.Entry(ventana_princ)
max_upd = tk.Entry(ventana_princ)
dias_upd = tk.Entry(ventana_princ)
Accion_upd = tk.Entry(ventana_princ)
Qty_to_Order_upd = tk.Entry(ventana_princ)
intran_upd = tk.Entry(ventana_princ)
comentarios_de_po_upd = tk.Entry(ventana_princ)
notas_upd = tk.Entry(ventana_princ)
no_proveedor_upd = tk.Entry(ventana_princ)
proveedor_upd = tk.Entry(ventana_princ)
contacto_upd = tk.Entry(ventana_princ)
sistema_upd = tk.Entry(ventana_princ)
centro_cuenta_upd = tk.Entry(ventana_princ)
ubicacion_upd = tk.Entry(ventana_princ)
centro_upd = tk.Entry(ventana_princ)
cuenta_upd = tk.Entry(ventana_princ)
Orden_ubicacion_one_upd = tk.Entry(ventana_princ)
Orden_ubicacion_two_upd = tk.Entry(ventana_princ)
category_upd = tk.Entry(ventana_princ)
po_or_req_upd = tk.Entry(ventana_princ)
#------------------------------------------------------------


stock_textbox = tk.Entry(ventana_princ)
accion_textbox = tk.Entry(ventana_princ)

stock_int = tk.Entry(ventana_princ)

combo = ttk.Combobox(ventana_princ, state="readonly", font=Font(size=15))
combobox_productos_del = ttk.Combobox(ventana_princ, state="readonly", font=Font(size=15))

show_main()


ventana_princ.mainloop()
