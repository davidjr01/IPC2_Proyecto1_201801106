from Nodos import Nodo, nCabecera
from Cabecera import listaCabeceras
import os 

class matrizOrtogonal:
    def __init__(self):
        self.CFilas = listaCabeceras()
        self.CColumnas = listaCabeceras()

    def append(self, fila, columna, dato):
        nuevo = Nodo(fila, columna, dato)

        CFila = self.CFilas.getCabecera(fila)
        if CFila == None:
            CFila = nCabecera(fila)
            CFila.accesoNodo = nuevo
            self.CFilas.appendCabecera(CFila)
        else:
            if nuevo.columna <  CFila.accesoNodo.columna:
                nuevo.derecha = CFila.accesoNodo
                CFila.accesoNodo.izquierda = nuevo
                CFila.accesoNodo = nuevo
            else:
                actual = CFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual

        CColumna = self.CColumnas.getCabecera(columna)
        if CColumna == None:
            CColumna = nCabecera(columna)
            CColumna.accesoNodo = nuevo
            self.CColumnas.appendCabecera(CColumna)
        else:
            if nuevo.fila <  CColumna.accesoNodo.fila:
                nuevo.abajo = CColumna.accesoNodo
                CColumna.accesoNodo.arriba = nuevo
                CColumna.accesoNodo = nuevo
            else:
                actual = CColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def Graficar_Nodo(self):
        CFila = self.CFilas.primero
        agrafica=open("Grafica.dot","w")
        agrafica.write("digraph G {\n")
        agrafica.write('node[styles="filled" , shape="box"]\n')

        #______________columnas de Y ___________________________________________
        CColumna = self.CColumnas.primero
        nombrey="Y0"
        n2=nombrey+'[label="Inicio"]\n'
        agrafica.write(n2)
        while CColumna != None:
            actual = CColumna.accesoNodo
            nny="Y"+str(actual.columna) 
            label='"Y='+str(actual.columna)+'"' 
            nodoy=nny+"[label="+label+"]"
            agrafica.write(nodoy+"\n")
            agrafica.write(nombrey+"->"+nny+"\n")
            agrafica.write(nny+"->"+nombrey+"\n")

            nombrey=nny
            
            CColumna = CColumna.siguiente
        # ____________________________________________________
        
        while CFila != None:
            actual = CFila.accesoNodo
            m="X="+str(actual.fila)
            nfila=int(actual.fila)
            nombrex="X"+str(actual.fila)
            m2=nombrex+'[label="'+str(m)+'"]\n'
            agrafica.write(m2)    
            while actual != None:
                nombrenodo="nodo"+str(actual.fila)+str(actual.columna) 
                y='"'+str(actual.dato)+'"'
                nodo=nombrenodo+"[label="+y+"]"
                agrafica.write(nodo+"\n")
                agrafica.write(nombrex+"->"+nombrenodo+"\n")
                agrafica.write(nombrenodo+"->"+nombrex+"\n")

                nombrex=nombrenodo
                actual = actual.derecha
            if nfila >1:
                agrafica.write("X"+str(nfila -1)+"->" + "X"+str(nfila)+"\n")
                agrafica.write("X"+str(nfila)+"->" + "X"+str(nfila-1)+"\n")
                agrafica.write('{rank="same";'+"X"+str(nfila-1)+";"+"X"+str(nfila)+"}\n")

            elif nfila==1:
                agrafica.write("Y0"+"->" + "X1\n")
                agrafica.write("X1"+"->" + "Y0\n")
                agrafica.write('{rank="same";'+"Y0"+";"+"X1}\n")
                

            CFila = CFila.siguiente
        #_________________unidendo_nodos_en_Y_________________
        CColumna = self.CColumnas.primero
        while CColumna != None:
            actual = CColumna.accesoNodo
            ncolumna="Y"+str(actual.columna)
            rank=ncolumna+";"
            while actual != None:
                nf="nodo"+str(actual.fila)+str(actual.columna)
                agrafica.write(ncolumna+"->"+nf+"\n")
                agrafica.write(nf+"->"+ncolumna+"\n")
                rank=rank+str(nf)+";"
                ncolumna=nf
                actual = actual.abajo
            
            agrafica.write('{rank="same";'+rank+"}\n")

            CColumna = CColumna.siguiente
        #___________________________________________________
        agrafica.write("}")
        agrafica.close()
        os.system('dot -Tpdf Grafica.dot -o Grafica.pdf')
        try:
             os.startfile("Grafica.pdf")
            
        except Exception:
            print ("no se encontro")
       