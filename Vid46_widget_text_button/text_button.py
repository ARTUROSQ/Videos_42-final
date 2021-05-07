
#Widgets text y button: text-sirve para introducir texto, button-sirve para aplicar botones interactivos


from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")#Al escribir la contraseña solo muestra arsteriscos

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)#Creamos nusdtra caja de texto
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)#Y nuestra barra vertical
scrollVert.grid(row=4, column=2, sticky="nsew")#Hace  que nuestra barra de desplazamiento se adapte al tamaño de nuestro widget

textoComentario.config(yscrollcommand=scrollVert.set)#Nuestra scrollbar se adapta a la cantidad de texto escrito

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0 , column=0, sticky="e", padx=10, pady=10 )

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2 , column=0, sticky="e", padx=10, pady=10 )

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3 , column=0, sticky="e", padx=10, pady=10 )

passLabel=Label(miFrame, text="Contraseña: ")
passLabel.grid(row=1 , column=0, sticky="e", padx=10, pady=10 )

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4 , column=0, sticky="e", padx=10, pady=10 )

def codigoBoton():
    
    minombre.set("Juan")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()


raiz=mainloop()


#Buscar en google entry tkinter python