
from tkinter import *

root = Tk() #En el video anterior la llamamos raiz

miframe = Frame(root, width=700, height=400)

miframe.pack()#Empaqueta nuestro frame 

miImagen = PhotoImage(file="mouse.gif")

#Label(miframe, text="Hola Alumnos de Python", fg="red", font=("Johanna",36)).place(x=100, y=200)#Ponemos el label a miframe

Label(miframe, image=miImagen).place(x=1, y=2)

#miLabel.pack nos pone el label pero la ventana queda pequeña para que no suceda se usa otra instruccion
#miLabel.pack()
 
root.mainloop()