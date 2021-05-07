
from tkinter import  * #Importamos todo del modulo tkinter


#Construimos la raiz de nuestra aplicacion grafica
raiz=Tk()

raiz.title("Ventana de pruebas") #Nos permite poner un titulo a la ventana

raiz.resizable(True,False) #Metodo que nos permite redimencionar o no la ventana, admite dos parametros booleanos

#raiz.iconbitmap("@/home/coolengine/Documentos/programacion/prog_python_pildoras/Vid_42-78/vid42_Interfaz_grafica1/gato.xbm")

raiz.iconbitmap("@~/Documentos/programacion/prog_python_pildoras/Vid_42-78/vid42_Interfaz_grafica1/gato.xbm")

raiz.geometry("650x350")

raiz.config(bg="blue")

raiz.mainloop() #La ventana se encuentra en un loop infinito con esta nstruccion
