from Nodos import Nodo, nCabecera
from Cabecera import listaCabeceras


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

    