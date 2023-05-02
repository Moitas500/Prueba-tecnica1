import os

class Archivo:
    #Constructor de la clase Archivo
    def __init__(self, ruta):
        if os.path.isfile(ruta):
            self.ruta = open(ruta)
        else:
            self.crearArchivo(ruta)

    #Metodo para leer el archivo linea por linea
    def leerArchivo(self):
        rutas = []

        with self.ruta as archivo:
            for linea in archivo:
                rutas.append(linea)

        return rutas

    #Metodo para cerrar el archivo
    def cerrarArchivo(self):
        self.ruta.close()

    def crearArchivo(self, nombre):
        file = open(nombre, "w")
        self.ruta = file

    def escribirArchivo(self,datos):

        for dato in datos:
            self.ruta.write( dato +os.linesep )