import sys

class Dron:
    #Constructor de la clase Dron
    def __init__(self, posicion, direccion, barrio):
        self.posicion = posicion
        self.direccion = direccion
        self.rutas = []
        self.barrio = barrio

    #Metodo para error
    def error(self, posicionX, posicionY):
        print("El dron no se puede mover en la direccion ", [posicionX,posicionY])
        sys.exit(1)

    #Metodo para añadir un reporte a la lista de reportes
    def añadirReporte(self, posicion, direccion):
        self.reporte.añadirEntrega([posicion, direccion])

    #Metodo para saber donde apunta el dron
    def apunta(self, direccion):
        self.direccion = direccion

    #Metodo para mover el dron
    def mover(self, movimiento):
        
        if ( movimiento == "A"):
            if ( self.direccion == "Norte"):

                if self.barrio.getCuadrasY() >= self.posicion[1]: 
                    self.posicion[1] += 1
                else: 
                    self.error(self.getPosicion()[0], self.getPosicion()[1] + 1)

            elif ( self.direccion == "Sur"):

                if self.posicion[1] > 0:
                    self.posicion[1] -= 1
                else:
                    self.error(self.getPosicion()[0], self.getPosicion()[1] - 1)

            elif ( self.direccion == "Este"):
                
                if self.barrio.getCuadrasX() >= self.posicion[0]:
                    self.posicion[0] += 1
                else: 
                    self.error(self.getPosicion()[0]+1, self.getPosicion()[1])

            elif ( self.direccion == "Oeste" and self.posicion[0] > 0):

                if self.posicion[0] > 0:
                    self.posicion[0] -= 1
                else:
                    self.error(self.getPosicion()[0]-1, self.getPosicion()[1])

        elif ( movimiento == "I" ):
            if ( self.direccion == "Norte" ):
                self.direccion = "Oeste"
            elif ( self.direccion == "Sur" ):
                self.direccion = "Este"
            elif ( self.direccion == "Este" ):
                self.direccion = "Norte"
            elif ( self.direccion == "Oeste" ):
                self.direccion = "Sur"

        elif ( movimiento == "D" ):
            if ( self.direccion == "Norte" ):
                self.direccion = "Este"
            elif ( self.direccion == "Sur" ):
                self.direccion = "Oeste"
            elif ( self.direccion == "Este" ):
                self.direccion = "Sur"
            elif ( self.direccion == "Oeste" ):
                self.direccion = "Norte"

    #Devuelve el reporte 
    def getReporte(self):
        return self.reporte.getEntregas()

    #Devuelve el barrio
    def getBarrio(self):
        return self.barrio

    #Devuelve la ruta actual del dron
    def getRuta(self):
        return self.rutas

    #Devuelve la posicion actual del dron
    def getPosicion(self):
        return self.posicion
    
    #Devuelve hacia donde esta mirando el dron
    def getDireccion(self):
        return "direccion" + " " + self.direccion
    
    #Setea la posicion actual del dron
    def setPosicion(self, posicion):
        self.posicion = posicion

    #Setea la direccion actual hacia donde mira el dron 
    def setDireccion(self, direccion):
        self.direccion = direccion

    #Setea las rutas del dron
    def setRutas(self, rutas):
        self.rutas = rutas

    #Setea el barrio
    def setBarrio(self, barrio):
        self.barrio = barrio