from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk

raiz = Tk()
nombre=StringVar()
contraseña1=StringVar()
contraseña2=StringVar()
services=[]
nommbreusuario="tilin"
contraseña="pejelagarto"

raiz.title("Registro de productos")
raiz.geometry("350x500")

# marco
marcoPrincipal = Frame(raiz, bg="#9657f5",width=200, height=300)
marcoPrincipal.pack(fill="both",expand=1)

def iniciosecion():
    if nommbreusuario == nombre.get() and contraseña1.get() == contraseña2.get() and contraseña == contraseña1.get() and services[i].get() == 1:
     print("Secion iniciada")
     marcoPrincipal.config(background="#008000")

    elif nommbreusuario != nombre.get():
       print("el usuario es incorrecto")
    elif services[i].get() != 1:
       print("error")
    else:
       print("la contraseña es incorrecta")

#imagen
imagenChida = Image.open("bobguapo.jpg")
imagenReproductor = imagenChida.resize((200, 150))
img = ImageTk.PhotoImage(imagenReproductor) 

imagenLabel = Label(marcoPrincipal, image=img)
imagenLabel.place(relx=0.22,  rely=0.01)

#etiquetas 
etiquetaNombre= Label(marcoPrincipal, text="Nombre:", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.25,rely=0.4)
etiquetaContraseña= Label(marcoPrincipal, text="Contraseña:", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.19,rely=0.46)
etiquetaconfcontra= Label(marcoPrincipal, text="confirmar contraseña:", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.01,rely=0.52)

#entri box
nombreEntry = Entry(marcoPrincipal, font=("Roboto",10,"bold"), textvariable=nombre).place(relx=0.5,rely=0.4)
contraseña1Entry = Entry(marcoPrincipal, font=("Roboto",10,"bold"), textvariable=contraseña1).place(relx=0.5,rely=0.46)
contraseña2Entry = Entry(marcoPrincipal, font=("Roboto",10,"bold"), textvariable=contraseña2).place(relx=0.5,rely=0.52)

#cradiobutton
sexo=Radiobutton(raiz, text= "Hombre", value=0).place(relx=0.25, rely= 0.6)
sexo1=Radiobutton(raiz, text= "Mujer", value=1).place(relx=0.5, rely= 0.6)

#checkbox
for i in range (1):
    option = IntVar()
    option.set(0)
    services.append(option)

Checkbutton(marcoPrincipal, text="Acepto terminos y condiciones", variable=services[0]).place(relx=0.2,rely=0.7)

#boton
botonSUMA= Button(marcoPrincipal, text="Iniciar sesion", font=("Roboto",20,"bold"), width=10,height=1,command=iniciosecion).place(relx=0.22,rely=0.83)


raiz.mainloop()