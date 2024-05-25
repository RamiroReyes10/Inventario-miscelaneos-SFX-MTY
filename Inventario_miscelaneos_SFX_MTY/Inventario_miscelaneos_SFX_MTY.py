from multiprocessing import Value
from re import X
from tkinter import ANCHOR, CENTER, CURRENT, LEFT, Label, ttk
from tkinter import filedialog
from tkinter.font import Font
from turtle import window_height, window_width
import pyodbc
import tkinter as tk
import pandas as pd
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import datetime

Server = "SFX02EU8JX4HK3"
Database = "miscelaneos_db "
user = "RamiroSFXPruebas"
password = "Danganronpa11"

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

    productos_del = cargar_productos()

    no_parte_interno_del.place(x=250, y=60)
    material_label = tk.Label(ventana_princ, text="Numero de parte interno")
    material_label.place(x=50, y=60)
    material_label.config(bg="white",
                         font=("Arial Black",10))

    nombre_producto_del = ttk.Combobox(ventana_princ, values=productos_del)
    nombre_producto_del.place(x=580, y=60)
    nombre_producto_del.config(font=("Arial Black",10))
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
    material_label_28 = tk.Label(ventana_princ, text="Categoria")
    material_label_28.place(x=50, y=480)
    material_label_28.config(bg="white",
                         font=("Arial Black",10))

    po_or_req_del.place(x=400, y=480)
    material_label_28 = tk.Label(ventana_princ, text="po or req")
    material_label_28.place(x=300, y=480)
    material_label_28.config(bg="white",
                         font=("Arial Black",10))

    boton_volver_menu_abc.place(x=1000, y=540)



def alta_materiales():
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
    
    no_parte_del.place(x=900, y=60)
    material_label_2 = tk.Label(ventana_princ, text="Numero de parte")
    material_label_2.place(x=730, y=60)
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
    material_label_28 = tk.Label(ventana_princ, text="Categoria")
    material_label_28.place(x=50, y=480)
    material_label_28.config(bg="white",
                         font=("Arial Black",10))

    po_or_req_del.place(x=400, y=480)
    material_label_28 = tk.Label(ventana_princ, text="po or req")
    material_label_28.place(x=300, y=480)
    material_label_28.config(bg="white",
                         font=("Arial Black",10))

    boton_volver_menu_abc.place(x=1000, y=540)

def update_materiales():
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
    
    no_parte_del.place(x=900, y=60)
    material_label_2 = tk.Label(ventana_princ, text="Numero de parte")
    material_label_2.place(x=730, y=60)
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
    material_label_28 = tk.Label(ventana_princ, text="Categoria")
    material_label_28.place(x=50, y=480)
    material_label_28.config(bg="white",
                         font=("Arial Black",10))

    po_or_req_del.place(x=400, y=480)
    material_label_28 = tk.Label(ventana_princ, text="po or req")
    material_label_28.place(x=300, y=480)
    material_label_28.config(bg="white",
                         font=("Arial Black",10))

    boton_volver_menu_abc.place(x=1000, y=540)


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
     
            cursor.execute("UPDATE dbo.Inventarios SET stock = stock + ? WHERE Nombre_del_producto = ?", (cantidad, nombre_del_producto))
           
            cursor.execute("SELECT stock, Punto_Reorden FROM dbo.Inventarios WHERE Nombre_del_producto = ?", (nombre_del_producto,))
            resultado_ent = cursor.fetchone()
            if resultado_ent:
                stock_actual, punto_de_reorden = resultado_ent
            
                cursor.execute("INSERT INTO dbo.Entradas (nombre_del_producto, stock_actual, entrada, fecha) VALUES (?, ?, ?, GETDATE())",(nombre_del_producto, stock_actual, cantidad,))

                if stock_actual > punto_de_reorden:
                    cursor.execute("UPDATE dbo.Inventarios SET Accion = 'Cantidad Suficiente' WHERE Nombre_del_producto = ?", (nombre_del_producto,))
                    connection.commit()

                    messagebox.showinfo("Exito", "Entrada guardada correctamente")
                else:
                    messagebox.showerror("Error", "Producto no encontrado en el inventario")

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
            cursor.execute("SELECT stock, Punto_Reorden FROM dbo.Inventarios WHERE Nombre_del_producto = ?", (nombre_del_producto_sal,))
            resultado = cursor.fetchone()
            
            if resultado:
                stock_actual, punto_de_reorden = resultado
                cursor.execute("INSERT INTO dbo.Salidas (nombre_del_producto, stock_actual, salida, fecha) VALUES (?, ?, ?, GETDATE())", (nombre_del_producto_sal, stock_actual, cantidad_sal,))
                
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


stock_textbox = tk.Entry(ventana_princ)
accion_textbox = tk.Entry(ventana_princ)

stock_int = tk.Entry(ventana_princ)

combo = ttk.Combobox(ventana_princ, state="readonly", font=Font(size=15))

show_main()

#Ejecutar interfaz principal
ventana_princ.mainloop()
