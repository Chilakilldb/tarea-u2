from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk


raiz=Tk()
services = []
idiomas = []
resproentry=StringVar()
resproentry1=StringVar()


def showInfo():
    print(f'el producto selecionado es: {resproentry.get()}')
    print(f'la SKU es: {resproentry1.get()}')
    print(f'el proveedor selecionado es: {var.get()}')
    for i in range(len(services)):
        selected = ""
        if services[i].get() >= 1:
            selected += str(i)
            if i ==1 and j ==0:
             print(f'selecciono el departamento: B')
            elif i ==2:
             print(f'selecciono el departamento: C')
            else:
             print(f'selecciono el departamento: A')

    for j in range(len(idiomas)):
        selected1 = ""

        if idiomas[j].get() >= 1:
            selected1 += str(j)
            #print(selected1)
            if j == 0:
             print("selecciono el idioma español")
            else:
                print("selected english languaje")
 
   
raiz.title("Registro de productos")
raiz.geometry("350x500")
#frame=Frame(raiz, bg="#707070")
#frame.pack(fill="both", expand=1)


# marco
marcoPrincipal = Frame(raiz, bg="#00FFFF",width=200, height=300)
marcoPrincipal.pack(fill="both",expand=1)

#imagen
imagenChida = Image.open("luffylentes.jpg")
imagenReproductor = imagenChida.resize((200, 150))
img = ImageTk.PhotoImage(imagenReproductor) 

imagenLabel = Label(marcoPrincipal, image=img)
imagenLabel.place(relx=0.22,  rely=0.01)

#etiqueta 
etiquetaproducto= Label(marcoPrincipal, text="producto:", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.15,rely=0.4)
etiquetaSKU= Label(marcoPrincipal, text="SKU:", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.25,rely=0.5)
etiquetaDepto= Label(marcoPrincipal, text="Depto:", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.2,rely=0.6)
etiquetaproducto= Label(marcoPrincipal, text="Proveedor:", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.15,rely=0.73)
etiquetaidioma= Label(marcoPrincipal, text="Idioma:", font=("Roboto",10,"bold"), bg="#000000", fg="#f7f7f7").place(relx=0.18,rely=0.8)


#entri box
productoEntry = Entry(marcoPrincipal, font=("Roboto",10,"bold"), textvariable=resproentry).place(relx=0.4,rely=0.4)
SKUEntry = Entry(marcoPrincipal, font=("Roboto",10,"bold"), textvariable=resproentry1).place(relx=0.4,rely=0.5)
#DeptoEntry = Entry(frame, font=("Roboto",10,"bold")).place(relx=0.4,rely=0.4)

for i in range (3):
    option = IntVar()
    option.set(0)
    services.append(option)

Checkbutton(marcoPrincipal, text="A", variable=services[0]).place(relx=0.1,rely=0.65)

Checkbutton(marcoPrincipal, text="B", variable=services[1]).place(relx=0.4,rely=0.65)

Checkbutton(marcoPrincipal, text="C", variable=services[2]).place(relx=0.7,rely=0.65)

Button(marcoPrincipal, text="Registrar", command=showInfo).place(relx=0.43,rely=0.92)

for j in range (2):
    option1 = IntVar()
    option1.set(0)
    idiomas.append(option1)

Checkbutton(marcoPrincipal, text="Español", variable=idiomas[0]).place(relx=0.3,rely=0.85)

Checkbutton(marcoPrincipal, text="ingles", variable=idiomas[1]).place(relx=0.6,rely=0.85)

var=tk.StringVar(marcoPrincipal)
var.set('-')
opciones=['yucart', 'disorder', 'meli_star', 'bullmaurix', 'chlakilldb', 'brisademar']
opcion=tk.OptionMenu(marcoPrincipal, var, *opciones)
opcion.config(width=20)
opcion.place(relx=0.4,rely=0.72)

raiz.mainloop()