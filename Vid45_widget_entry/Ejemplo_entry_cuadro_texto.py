
#Entry=widgets utilizados para introducir texto

#Variable Label variable.Label(contenedor, opciones), parecido al widget label el uso de entry

from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroTexto=Entry(miFrame) #Nos pone un cuadro para introducir texto.

#cuadroTexto.place(x=200, y=100)#Ponemos nuestro cuadro de texto en la posicion (100,100)

cuadroTexto.grid(row=0, column=1 ) #Nos crea columnas y filas

nombreLabel=Label(miFrame, text="Nombre: ")

nombreLabel.place(x=100, y=100)#El mombre de nuestro entry en el lugar que se indica

nombreLabel.grid(row=0, column =0)#El lugar en donde se colocara nuestro entry

raiz.mainloop()



