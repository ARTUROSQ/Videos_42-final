from tkinter import  * #Importamos todo del modulo tkinter


#Construimos la raiz de nuestra aplicacion grafica
raiz=Tk()

raiz.title("Ventana de pruebas") #Nos permite poner un titulo a la ventana

#aiz.resizable(True,False) #Metodo que nos permite redimencionar o no la ventana, admite dos parametros booleanos

#raiz.iconbitmap("@/home/coolengine/Documentos/programacion/prog_python_pildoras/Vid_42-78/vid42_Interfaz_grafica1/gato.xbm")

raiz.iconbitmap("@~/Documentos/programacion/prog_python_pildoras/Vid_42-78/vid42_Interfaz_grafica1/gato.xbm")

#raiz.geometry("650x350")

raiz.config(bg="blue")

miFrame=Frame() #Creacion de un frame

#miFrame.pack(side="right", anchor="n") #Empaquetamos nuestro frame en la raiz, le podemos decir a que lado se ancla

#miFrame.pack(fill="both", expand="True") #Nos rellena la raiz dependiendo el parametro sera horizontal vertical o ambos

miFrame.pack()

miFrame.config(bd=35) #Con bd le damos borde a nuestro frame

miFrame.config(relief="groove") #Groove es el estilo de nuestro borde otro estilo es sunken

miFrame.config(cursor="hand2") #Nos pone un puntero para el raton

miFrame.config(bg="red") #Le damos color a nuestro frame, pero primero hay que darle tamaño

miFrame.config(width="650", height="350") #Configuramos el tamaño del frame



raiz.mainloop() #La ventana se encuentra en un loop infinito con esta nstruccion
