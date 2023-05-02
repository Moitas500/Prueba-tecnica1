class Localidad:
    #Constructor de la clase locaclidad
    def __init__(self, cuadrasX, cuadrasY):
        self.cuadrasX = cuadrasX
        self.cuadrasY = cuadrasY

    #Devuelve la cantidad de cuadras en eje X
    def getCuadrasX(self):
        return self.cuadrasX
    
    #Devuelve la cantidad de cuadras en eje Y
    def getCuadrasY(self):
        return self.cuadrasY