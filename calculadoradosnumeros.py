from tkinter import *

raiz=Tk()
raiz.title("Calculadora")
raiz.geometry("400x500")

frame=Frame(raiz, bg="#707070")
frame.pack(fill="both", expand=1)

#VARIABLES
valorA= IntVar()
valorB= IntVar()
resultado =0
reseteado=0
#valinicial =0

def reset ():
    valorA.set("0")
    valorB.set("0")
    reseteado=resultado
    etiquetaRESULTADO.config(text=resultado)

        

def Suma ():
    resultado = int( valorA.get())+ int(valorB.get())
    etiquetaRESULTADO.config(text=resultado)
    


def multiplicacion ():
    resultado = int(valorA.get())*int(valorB.get())
    print(resultado)
    etiquetaRESULTADO.config(text=resultado)

def resta():
    resultado = int(valorA.get()) - int(valorB.get())
    print(resultado)
    etiquetaRESULTADO.config(text=resultado)

def divicion():
    resultado = int(valorA.get()) / int(valorB.get())
    print(resultado)
    etiquetaRESULTADO.config(text=resultado)
"""""
def igual ():
    resultado.get()
    etiquetaRESULTADO.config(text=resultado)
 """   

#ETIQUETA TITULO
etiquetaTITULO= Label(frame, text="CALCULADORA", font=("Roboto",15,"bold"), bg="#f7f7f7", fg="#000000").place(relx=0.35, rely=0.05)


#etiqueta nombre 
etiquetaA= Label(frame, text="NUMERO A", font=("Roboto",10,"bold"), bg="#707070", fg="#f7f7f7").place(relx=0.1, rely=0.2)

etiquetaB= Label(frame, text="NUMERO B", font=("Roboto",10,"bold"), bg="#707070", fg="#f7f7f7").place(relx=0.1, rely=0.3)

etiquetares= Label(frame, text="RESULTADO", font=("Roboto",10,"bold"), bg="#707070", fg="#f7f7f7").place(relx=0.1, rely=0.4)

etiquetaRESULTADO= Label(frame, text= resultado , font=("Roboto",10,"bold"), bg="#707070", fg="#f7f7f7")
etiquetaRESULTADO.place(relx=0.55, rely=0.4)



#entri box
AEntry = Entry(frame, font=("Roboto",10,"bold"), textvariable=valorA).place(relx=0.4,rely=0.2)

BEntry =  Entry(frame, font=("Roboto",10,"bold"), textvariable=valorB).place(relx=0.4,rely=0.3)

#RESULTADOEntry = Entry(frame,textvariable= font=("Roboto",10,"bold")).place(relx=0.4,rely=0.4)


#Boton
botonSUMA= Button(frame, text="Suma", font=("Roboto",10,"bold"), width=10,height=1,command=Suma).place(relx=0.1,rely=0.7)

botonmultiplicacion= Button(frame, text="mult", font=("Roboto",10,"bold"), width=10,height=1,command=multiplicacion).place(relx=0.4,rely=0.7)

botonresta= Button(frame, text="resta", font=("Roboto",10,"bold"), width=10,height=1,command=resta).place(relx=0.1,rely=0.8)

botonRESET= Button(frame, text="C", font=("Roboto",10,"bold"), width=10,height=1,command=reset).place(relx=0.7,rely=0.7)

botondivicion = Button(frame, text="division", font=("Roboto",10,"bold"), width=10,height=1,command=divicion).place(relx=0.4,rely=0.8)

#botonigual = Button(frame, text="=", font=("Roboto",10,"bold"), width=10,height=1,command=igual).place(relx=0.7,rely=0.8)






raiz.mainloop()