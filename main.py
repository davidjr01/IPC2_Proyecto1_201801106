from Ortogonal import matrizOrtogonal
from tkinter import *
from tkinter import ttk
from random import *

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

mframe=Frame(ventana,width=700 ,height=300)


nombre1=Label(mframe,text="Nombre Jugador 1")
nombre1.place(x=50,y=50)
nombre1.config()
textbox1=Entry(mframe)
textbox1.place(x=180,y=50)

color1=Label(mframe,text="Color")
color1.place(x=50,y=90)
listas1=ttk.Combobox(mframe,values=['Azul','Rojo','Amarillo','Verde'])
listas1.place(x=180,y=90,width=70,height=20)

color2=Label(mframe,text="Color")
color2.place(x=350,y=90)
listas2=ttk.Combobox(mframe,values=['Azul','Rojo','Amarillo','Verde'])
listas2.place(x=480,y=90,width=70,height=20)




nombre2=Label(mframe,text="Nombre Jugador 2")
nombre2.place(x=350,y=50)
textbox2=Entry(mframe)
textbox2.place(x=480,y=50)


lfila=Label(mframe,text="Fila")
lfila.place(x=190,y=170)
fila=Entry(mframe)
fila.place(x=230,y=170,width=70,height=20)

lcolumna=Label(mframe,text="Columna")
lcolumna.place(x=370,y=170)
columna=Entry(mframe)
columna.place(x=440,y=170,width=70,height=20)



def cerrar_app():
    ventana.destroy()


def codigoBoton():
    if listas1.get() == listas2.get():
        print("Los colroes no pueden ser igual")

    else:
        ventana.withdraw()
        ventana2=Toplevel()
        ventana2.title("Juego")
        ventana2.geometry('500x500')
        ventana2.protocol("WM_DELETE_WINDOW", cerrar_app)
        fil=fila.get()
        col=columna.get()
        tabla=[]
        for i in range(int(fil)):
            tabla.append([])
            for j in range(int(col)):
                tabla[i].append(Button(ventana2))
                tabla[i][j].config(bg="#F8FFA2",borderwidth=1,
                activebackground="#A2FBFF",relief="solid")
                tabla[i][j].place(relx=0.1 + 0.1*j, rely=0.1 + 0.1*i,relwidth=0.1,relheight=0.1)



    


    

   

  
    
boton=Button(mframe,text="SIGUIENTE",command=codigoBoton)
boton.place(x=310,y=230 )
mframe.pack()




ventana.mainloop()



 

    