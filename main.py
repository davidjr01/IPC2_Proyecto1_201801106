from Ortogonal import matrizOrtogonal
from tkinter import *

ventana=Tk()
barramenu=Menu(ventana)
ventana.config(menu=barramenu,width=300 ,height=300)
amenu=Menu(barramenu,tearoff=0)
amenu.add_command(label="Abrir partida")
amenu.add_command(label="Guardar partida")
amenu.add_command(label="Ayuda")
jugar=Menu(barramenu)
barramenu.add_cascade(label="Menu",menu=amenu)
barramenu.add_cascade(label="Jugar",menu=jugar)




mframe=Frame(ventana,width=800 ,height=400)
textbox=Entry(mframe)
textbox.place(x=10,y=30)
texto=Label(mframe,text="jugador1")
texto.place(x=10,y=5)


def codigoBoton():
    print(textbox.get())
boton=Button(mframe,text="ACEPTAR",command=codigoBoton)
boton.place(x=100,y=100)

mframe.pack()

ventana.mainloop()



 

    