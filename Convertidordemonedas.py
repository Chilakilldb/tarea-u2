from tkinter import *
from tkinter import messagebox
import tkinter as tk

raiz=Tk()
raiz.title("Convertidor de monedas")
raiz.geometry("350x500")

valor= IntVar()
valor1= IntVar()
resconvercion = 0

def inisiosecion():

    if var1.get() == var.get():
       resconvercion= valor1.get()
       convercionentry.config(text=resconvercion)

    elif var1.get() == 'MXN' and var.get() == 'USD':
     dolarpeso= valor1.get()
     resconvercion=dolarpeso/18
     convercionentry.config(text=resconvercion)

    elif var1.get() == 'MXN' and var.get() == 'JPY':
     dolarpeso= valor1.get()
     resconvercion=dolarpeso*6.97327
     convercionentry.config(text=resconvercion)

    elif var1.get() == 'USD' and var.get() == 'MXN':
     dolarpeso= valor1.get()
     resconvercion=dolarpeso*18.9115
     convercionentry.config(text=resconvercion)

    elif var1.get() == 'USD' and var.get() == 'JPY':
     dolarpeso= valor1.get()
     resconvercion=dolarpeso*131.875
     convercionentry.config(text=resconvercion)

    elif var1.get() == 'JPY' and var.get() == 'MXN':
     dolarpeso= valor1.get()
     resconvercion=dolarpeso/6.97327
     convercionentry.config(text=resconvercion)

    elif var1.get() == 'JPY' and var.get() == 'USD':
     dolarpeso= valor1.get()
     resconvercion=dolarpeso/131.875
     convercionentry.config(text=resconvercion)

# marco
marcoPrincipal = Frame(raiz, bg="#00FFFF",width=200, height=300)
marcoPrincipal.pack(fill="both",expand=1)

#etiqueta
nombretitulo= Label(marcoPrincipal, text="Convertidor de monedas", font=("Roboto",15,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.15,rely=0.02)
numero= Label(marcoPrincipal, text="Numero A", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.15,rely=0.25)
resultadolabel= Label(marcoPrincipal, text= "resultado", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.15,rely=0.6)
convercionentry= Label(marcoPrincipal, text=resconvercion, font=("Roboto",10,"bold"), bg="#ffffff", fg="#000000")
convercionentry.place(relx=0.5,rely=0.6)

#listadesplegable
var1=tk.StringVar(marcoPrincipal)
var1.set('Moneda')
opciones1=['MXN', 'USD', 'JPY']
opcion1=tk.OptionMenu(marcoPrincipal, var1, *opciones1)
opcion1.config(width=15)
opcion1.place(relx=0.1,rely=0.42)

var=tk.StringVar(marcoPrincipal)
var.set('Moneda')
opciones=['MXN', 'USD', 'JPY']
opcion=tk.OptionMenu(marcoPrincipal, var, *opciones)
opcion.config(width=15)
opcion.place(relx=0.55,rely=0.42)

#entry
NumeroA = Entry(marcoPrincipal, font=("Roboto",10,"bold"), textvariable=valor1).place(relx=0.4,rely=0.25)

#boton
convertir_boton= Button(marcoPrincipal, text="Convertir", font=("Roboto",20,"bold"), width=10,height=1,command=inisiosecion).place(relx=0.25,rely=0.8)


raiz.mainloop()