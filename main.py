from Ortogonal import matrizOrtogonal
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
import tkinter as tk
import random

ventana=Tk()
barramenu=Menu(ventana)
ventana.config(menu=barramenu,width=300 ,height=300)
anchoventana=int(700)
largoventana=int(300)
x_ventana =(int( ventana.winfo_screenwidth()/2))-(int(anchoventana/2))
y_ventana = int((ventana.winfo_screenheight() -100 )/2)-(int(largoventana/2))
posicion = str(anchoventana) + "x" + str(largoventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)



amenu=Menu(barramenu,tearoff=0)
amenu.add_command(label="Abrir partida")
amenu.add_command(label="Guardar partida")
amenu.add_command(label="Ayuda")
jugar=Menu(barramenu)
barramenu.add_cascade(label="Menu",menu=amenu)
barramenu.add_cascade(label="Jugar",menu=jugar)

mframe=Frame(ventana,width=700 ,height=300)
mframe.config(bg="#ABB2B9")


nombre1=Label(mframe,text="Nombre Jugador 1")
nombre1.place(x=50,y=50)
nombre1.config(bg="#ABB2B9")
textbox1=Entry(mframe)
textbox1.place(x=180,y=50)


color1=Label(mframe,text="Color")
color1.place(x=50,y=90)
color1.config(bg="#ABB2B9")
listas1=ttk.Combobox(mframe,values=['Azul','Rojo','Amarillo','Verde'])
listas1.place(x=180,y=90,width=70,height=20)

color2=Label(mframe,text="Color")
color2.place(x=350,y=90)
color2.config(bg="#ABB2B9")
listas2=ttk.Combobox(mframe,values=['Azul','Rojo','Amarillo','Verde'])
listas2.place(x=480,y=90,width=70,height=20)




nombre2=Label(mframe,text="Nombre Jugador 2")
nombre2.place(x=350,y=50)
nombre2.config(bg="#ABB2B9")
textbox2=Entry(mframe)
textbox2.place(x=480,y=50)


lfila=Label(mframe,text="Fila")
lfila.place(x=80,y=170)
lfila.config(bg="#ABB2B9")
fila=Entry(mframe)
fila.place(x=140,y=170,width=70,height=20)

lcolumna=Label(mframe,text="Columna")
lcolumna.place(x=250,y=170)
lcolumna.config(bg="#ABB2B9")
columna=Entry(mframe)
columna.place(x=320,y=170,width=70,height=20)


ln_piezas=Label(mframe,text="Numero de Piezas")
ln_piezas.place(x=430,y=170)
ln_piezas.config(bg="#ABB2B9")
npiezas=Entry(mframe)
npiezas.place(x=550,y=170,width=70,height=20)






def cerrar_app():
    ventana.destroy()


def codigoBoton():
    if listas1.get() == listas2.get():
        print("Los colroes no pueden ser igual")

    else:
        ventana.withdraw()
        ventana2=Toplevel()
        ventana2.title("Juego")

        anchoventana2=int(950)
        largoventana2=int(650)
        x_ventana2 =(int( ventana2.winfo_screenwidth()/2))-(int(anchoventana2/2))
        y_ventana2 = int((ventana2.winfo_screenheight() -100 )/2)-(int(largoventana2/2))
        posicion2 = str(anchoventana2) + "x" + str(largoventana2) + "+" + str(x_ventana2) + "+" + str(y_ventana2)
        ventana2.geometry(posicion2)
        ventana2.protocol("WM_DELETE_WINDOW", cerrar_app)
        ventana2.config(bg="#ABB2B9")
        mframe2=Frame(ventana2,width=600 ,height=600)
        mframe2.config(bg="#ABB2B9")
        mframe2.place(x=15,y=15)
        fil=fila.get()
        col=columna.get()
        tabla=[]
        nf=1/int(fil)
        nc=1/int(col)
        for i in range(int(fil)):
            
            for j in range(int(col)):
                tabla.append([])
                tabla[i].append(Button(mframe2))
                tabla[i][j].config(bg="white",borderwidth=1,activebackground="white",relief="solid")
                tabla[i][j].place(relx=nc *j, rely=nf*i,relwidth=nc,relheight=nf)
        
        for i in range(int(col)):
            i2=i+1
            tabla[0][i].config(text=str(i2))
        
        for i in range(int(fil)):
            i2=i+1
            tabla[i][0].config(text=str(i2))
        
            

        jugador1=Label(ventana2,text="Jugador 1 :"+textbox1.get())
        jugador1.place(x=720,y=260)
        jugador1.config(bg="#ABB2B9")
        posx1=Label(ventana2,text="Pos X ")
        posx1.place(x=650,y=300)
        posx1.config(bg="#ABB2B9")
        textox1=Entry(ventana2)
        textox1.place(x=700,y=300,width=70,height=20)
          
        posy1=Label(ventana2,text="Pos Y ")
        posy1.place(x=800,y=300)
        posy1.config(bg="#ABB2B9")
        textoy1=Entry(ventana2)
        textoy1.place(x=850,y=300,width=70,height=20)

        jugador2=Label(ventana2,text="Jugador 2 :"+textbox2.get())
        jugador2.place(x=720,y=400)
        jugador2.config(bg="#ABB2B9")
        posx2=Label(ventana2,text="Pos X ")
        posx2.config(bg="#ABB2B9")
        posx2.place(x=650,y=440)
        textox2=Entry(ventana2)
        textox2.place(x=700,y=440,width=70,height=20)
          
        posy2=Label(ventana2,text="Pos Y ")
        posy2.config(bg="#ABB2B9")
        posy2.place(x=800,y=440)
        textoy2=Entry(ventana2)
        textoy2.place(x=850,y=440,width=70,height=20)

        

        mframei=Frame(ventana2,width=250 ,height=230)
        mframei.place(x=650,y=15)
        mframei.config(bg="#ABB2B9")
        ##turno=random.randint(1,6)
        turno=0
        turno2=0
        pos=[]
        pos.append("uno")
        matriz=matrizOrtogonal()
        cont1=0
        cont2=0
        
        
        

        def iniciarJuego():
            global turno
            global cont1
            global cont2
            cont1=0
            cont2=0
            
            turno=random.randint(1,6)
            imag = Image.open(str(turno)+".png")
            imag1 = ImageTk.PhotoImage(imag)
            pintarl = tk.Label(mframei, image=imag1)
            pintarl.imag1=imag1
            pintarl.place(x=0, y=0,width=250,height=250)

            textox1.config(state="normal")
            textoy1.config(state="normal")
            botonjugar.config(state="normal")
            botoniniciar.destroy()
            

        def Empezar():
            global cont1
            control1=False
            cont1=cont1+1

            


            if str(listas1.get())=="Rojo":
                cb1="red"
            elif str(listas1.get())=="Azul":
                cb1="blue"
            elif str(listas1.get())=="Amarillo":
                cb1="yellow"
            elif str(listas1.get())=="Verde":
                cb1="green"


            
            xc1=int(textox1.get())-1
            yc1=int(textoy1.get())-1
            xmatriz1=int(textox1.get())
            ymatriz1=int(textoy1.get())
           
            #piezza1____________
            global turno
            

            if turno==1:
                for i in range(4):
                    if i==3 :
                        for ad in pos:
                            if ad== str(yc1+i)+str(xc1) or ad== str(yc1+i)+str(xc1+1):
                                control1=True
                                break
                            
                    else:
                        for ad in pos:
                            if ad== str(yc1+i)+str(xc1):
                                control1=True
                                break

                if control1==True or cont1==2:
                    if cont1==2:
                        print("Perdio Turno")
                        cont1=0
                    else:
                        print("Espacio lleno ")
                    
                
                else: 
                    for i in range(4):
                        if i==3 : 
                            tabla[yc1+i][xc1].config(bg=cb1) 
                            tabla[yc1+i][xc1+1].config(bg=cb1) 
                            pos.append(str(yc1+i)+str(xc1))
                            pos.append(str(yc1+i)+str(xc1+1))
                            matriz.append(xmatriz1,ymatriz1+i,cb1)
                            matriz.append(xmatriz1+1,ymatriz1+i,cb1)
                        else:
                            tabla[yc1+i][xc1].config(bg=cb1) 
                            pos.append(str(yc1+i)+str(xc1))
                            matriz.append(xmatriz1,ymatriz1+i,cb1)
                    cont1=0

            elif turno==2:
                for i in range(4):
                    if i==3 :
                        for ad in pos:
                            if ad==str(yc1+i)+str(xc1) or ad==str(yc1+i)+str(xc1-1):
                                control1=True
                                break       
                    else:
                        for ad in pos:
                            if ad==str(yc1+i)+str(xc1):
                                control1=True
                                break
                
                if control1==True or cont1==2:
                    if cont1==2:
                        print("Perdio Turno")
                        cont1=0
                    else:
                        print("Espacio lleno ")
                
                else: 
                    for i in range(4):
                        if i==3 :
                            tabla[yc1+i][xc1].config(bg=cb1) 
                            tabla[yc1+i][xc1-1].config(bg=cb1) 
                            pos.append(str(yc1+i)+str(xc1))
                            pos.append(str(yc1+i)+str(xc1-1))

                            matriz.append(xmatriz1,ymatriz1+i,cb1)
                            matriz.append(xmatriz1-1,ymatriz1+i,cb1)

                        else:
                            tabla[yc1+i][xc1].config(bg=cb1)
                            pos.append(str(yc1+i)+str(xc1))
                            matriz.append(xmatriz1,ymatriz1+i,cb1)

                    cont1=0
                
                

            elif turno==3:
                for i in range(4):
                    for ad in pos:
                        if ad==str(yc1)+str(xc1+i):
                            control1=True
                            break
                
                if control1==True or cont1==2:
                    if cont1==2:
                        print("Perdio Turno")
                        cont1=0
                    else:
                        print("Espacio lleno ")
                
                else:
                    for i in range(4):
                        tabla[yc1][xc1+i].config(bg=cb1)  
                        pos.append(str(yc1)+str(xc1+i))
                        matriz.append(xmatriz1+i,ymatriz1,cb1)
                    cont1=0

            
            elif turno==4:

                for i in range(2):
                    for ad in pos:
                        if ad==str(yc1)+str(xc1+i) or ad==str(yc1+1)+str(xc1+i):
                            control1=True
                            break
                
                if control1==True or cont1==2:
                    if cont1==2:
                        print("Perdio Turno")
                        cont1=0
                    else:
                        print("Espacio lleno ")
                
                else:
                    for i in range(2):
                        tabla[yc1][xc1+i].config(bg=cb1) 
                        pos.append(str(yc1)+str(xc1+i))
                        matriz.append(xmatriz1+i,ymatriz1,cb1)
                        tabla[yc1+1][xc1+i].config(bg=cb1) 
                        pos.append(str(yc1+1)+str(xc1+i))
                        matriz.append(xmatriz1+i,ymatriz1+1,cb1)
                    cont1=0
            
            elif turno==5:

                for i in range(2):
                    for ad in pos:
                        if ad==str(yc1)+str(xc1+i):
                            control1=True
                            break
                     
                for i in range(4):
                    for ad in pos:
                        if ad==str(yc1+1)+str(xc1-1 +i):
                            control1=True
                            break
                
                if control1==True or cont1==2:
                    if cont1==2:
                        print("Perdio Turno")
                        cont1=0
                    else:
                        print("Espacio lleno ")
                
                else:
                    for i in range(2):
                        tabla[yc1][xc1+i].config(bg=cb1) 
                        pos.append(str(yc1)+str(xc1+i))
                        matriz.append(xmatriz1+i,ymatriz1,cb1)
                    
                    for i in range(4):
                        tabla[yc1+1][xc1-1 +i].config(bg=cb1) 
                        pos.append(str(yc1+1)+str(xc1-1 +i))
                        matriz.append(xmatriz1-1+i,ymatriz1+1,cb1)
                    cont1=0
            
            elif turno==6:
                for i in range(5):
                    for ad in pos:
                        if ad==str(yc1+i)+str(xc1):
                            control1=True
                            break
                
                if control1==True or cont1==2:
                    if cont1==2:
                        print("Perdio Turno")
                        cont1=0
                    else:
                        print("Espacio lleno ")
                
                else:
                    for i in range(5):
                        tabla[yc1+i][xc1].config(bg=cb1) 
                        pos.append(str(yc1+i)+str(xc1))
                        matriz.append(xmatriz1,ymatriz1+i,cb1)
                    cont1=0
            
            if cont1==True and cont1==1:
                asdf=0
                
            else:
                textox1.delete(0,END)
                textoy1.delete(0,END)
                textox1.config(state="disabled")
                textoy1.config(state="disabled")
                textox2.config(state="normal")
                textoy2.config(state="normal")
                botonjugar.config(state="disabled")
                botonjugar2.config(state="normal")
                global turno2
                turno2=random.randint(1,6)
        
                imag = Image.open(str(turno2)+".png")
                imag1 = ImageTk.PhotoImage(imag)
                pintarl2 = tk.Label(mframei, image=imag1)
                pintarl2.imag1=imag1
                pintarl2.place(x=0, y=0,width=250,height=250)

            




        

        def Empezar2():
            global cont2
            cont2=cont2+1
        

            control2=False
            if str(listas2.get())=="Rojo":
                cb2="red"
            elif str(listas2.get())=="Azul":
                cb2="blue"
            elif str(listas2.get())=="Amarillo":
                cb2="yellow"
            elif str(listas2.get())=="Verde":
                cb2="green"


            xc2=int(textox2.get())-1
            yc2=int(textoy2.get())-1
            xmatriz2=int(textox2.get())
            ymatriz2=int(textoy2.get())

            #piezza1____________
            global turno2
            
            

            if turno2==1:
                for i in range(4):
                    if i==3 :
                        for ad in pos:
                            if ad== str(yc2+i)+str(xc2) or ad== str(yc2+i)+str(xc2+1):
                                control2=True
                                break
                            
                    else:
                        for ad in pos:
                            if ad== str(yc2+i)+str(xc2):
                                control2=True
                                break

                if control2==True or cont2==2:
                    if cont2==2:
                        print("Perdio Turno")
                        cont2=0
                    else:
                        print("Espacio lleno ")
                
                else: 
                    for i in range(4):
                        if i==3 : 
                            tabla[yc2+i][xc2].config(bg=cb2) 
                            tabla[yc2+i][xc2+1].config(bg=cb2) 
                            pos.append(str(yc2+i)+str(xc2))
                            pos.append(str(yc2+i)+str(xc2+1))
                            matriz.append(xmatriz2,ymatriz2+i,cb2)
                            matriz.append(xmatriz2+1,ymatriz2+i,cb2)
                        else:
                            tabla[yc2+i][xc2].config(bg=cb2) 
                            pos.append(str(yc2+i)+str(xc2))
                            matriz.append(xmatriz2,ymatriz2+i,cb2)
                    cont2=0

            elif turno2==2:
                for i in range(4):
                    if i==3 :
                        for ad in pos:
                            if ad==str(yc2+i)+str(xc2) or ad==str(yc2+i)+str(xc2-1):
                                control2=True
                                break       
                    else:
                        for ad in pos:
                            if ad==str(yc2+i)+str(xc2):
                                control2=True
                                break
                
                if control2==True or cont2==2:
                    if cont2==2:
                        print("Perdio Turno")
                        cont2=0
                    else:
                        print("Espacio lleno ")
                
                else: 
                    for i in range(4):
                        if i==3 :
                            tabla[yc2+i][xc2].config(bg=cb2) 
                            tabla[yc2+i][xc2-1].config(bg=cb2) 
                            pos.append(str(yc2+i)+str(xc2))
                            pos.append(str(yc2+i)+str(xc2-1))

                            matriz.append(xmatriz2,ymatriz2+i,cb2)
                            matriz.append(xmatriz2-1,ymatriz2+i,cb2)

                        else:
                            tabla[yc2+i][xc2].config(bg=cb2)
                            pos.append(str(yc2+i)+str(xc2))
                            matriz.append(xmatriz2,ymatriz2+i,cb2)
                    cont2=0
                

            elif turno2==3:
                for i in range(4):
                    for ad in pos:
                        if ad==str(yc2)+str(xc2+i):
                            control2=True
                            break
                
                if control2==True or cont2==2:
                    if cont2==2:
                        print("Perdio Turno")
                        cont2=0
                    else:
                        print("Espacio lleno ")
                
                else:
                    for i in range(4):
                        tabla[yc2][xc2+i].config(bg=cb2)  
                        pos.append(str(yc2)+str(xc2+i))
                        matriz.append(xmatriz2+i,ymatriz2,cb2)
                    cont2=0

            
            elif turno2==4:

                for i in range(2):
                    for ad in pos:
                        if ad==str(yc2)+str(xc2+i) or ad==str(yc2+1)+str(xc2+i):
                            control2=True
                            break
                
                if control2==True or cont2==2:
                    if cont2==2:
                        print("Perdio Turno")
                        cont2=0
                    else:
                        print("Espacio lleno ")
                
                else:
                    for i in range(2):
                        tabla[yc2][xc2+i].config(bg=cb2) 
                        pos.append(str(yc2)+str(xc2+i))
                        matriz.append(xmatriz2+i,ymatriz2,cb2)
                        tabla[yc2+1][xc2+i].config(bg=cb2) 
                        pos.append(str(yc2+1)+str(xc2+i))
                        matriz.append(xmatriz2+i,ymatriz2+1,cb2)
                    cont2=0
            
            elif turno2==5:

                for i in range(2):
                    for ad in pos:
                        if ad==str(yc2)+str(xc2+i):
                            control2=True
                            break
                     
                for i in range(4):
                    for ad in pos:
                        if ad==str(yc2+1)+str(xc2-1 +i):
                            control2=True
                            break
                
                if control2==True or cont2==2:
                    if cont2==2:
                        print("Perdio Turno")
                        cont2=0
                    else:
                        print("Espacio lleno ")
                
                else:
                    for i in range(2):
                        tabla[yc2][xc2+i].config(bg=cb2) 
                        pos.append(str(yc2)+str(xc2+i))
                        matriz.append(xmatriz2+i,ymatriz2,cb2)
                    
                    for i in range(4):
                        tabla[yc2+1][xc2-1 +i].config(bg=cb2) 
                        pos.append(str(yc2+1)+str(xc2-1 +i))
                        matriz.append(xmatriz2-1+i,ymatriz2+1,cb2)
                    cont2=0
            
            elif turno2==6:
                for i in range(5):
                    for ad in pos:
                        if ad==str(yc2+i)+str(xc2):
                            control2=True
                            break
                
                if control2==True or cont2==2:
                    if cont2==2:
                        print("Perdio Turno")
                        cont2=0
                    else:
                        print("Espacio lleno ")
                
                else:
                    for i in range(5):
                        tabla[yc2+i][xc2].config(bg=cb2) 
                        pos.append(str(yc2+i)+str(xc2))
                        matriz.append(xmatriz2,ymatriz2+i,cb2) 
                    cont2=0
            if cont2==True and cont1==2:
                asdf=0
                
            else:

                textox2.delete(0,END)
                textoy2.delete(0,END)
            
                textox2.config(state="disabled")
                textoy2.config(state="disabled")

                textox1.config(state="normal")
                textoy1.config(state="normal")

                botonjugar2.config(state="disabled")
                botonjugar.config(state="normal")

                global turno
                turno=random.randint(1,6)

                imag = Image.open(str(turno)+".png")
                imag1 = ImageTk.PhotoImage(imag)
                pintarl2 = tk.Label(mframei, image=imag1)
                pintarl2.imag1=imag1
                pintarl2.place(x=0, y=0,width=250,height=250)
        
        def GraficarMatriz():
            matriz.Graficar_Nodo()
          

     
        botoniniciar=Button(ventana2,text="Empezar Juego ",command=iniciarJuego)
        botoniniciar.place(x=740,y=150)
       

        botonjugar=Button(ventana2,text="Siguiente",command=Empezar)
        botonjugar.place(x=750,y=350 )
        
        botonjugar2=Button(ventana2,text="Siguiente",command=Empezar2)
        botonjugar2.place(x=750,y=490 )

        Gmatriz=Button(ventana2,text="Graficar",command=GraficarMatriz)
        Gmatriz.place(x=750,y=530)

        botonjugar.config(state="disabled")
        textox1.config(state="disabled")
        textoy1.config(state="disabled")
       


        botonjugar2.config(state="disabled")
        textox2.config(state="disabled")
        textoy2.config(state="disabled")
       
    
       

        
     
        



    


    

   

  
    
boton=Button(mframe,text="SIGUIENTE",command=codigoBoton)
boton.place(x=310,y=230 )
mframe.pack()




ventana.mainloop()



 

    