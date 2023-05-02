from archivo import Archivo
from dron import Dron
from localidad import Localidad

def main():
    #Se crea la localidad y el dron Y el report de entregas
    barrio = Localidad(15,15)
    robot = Dron([0,0],"Norte", barrio)

    resultados = []

    #Se abre el archivo
    archivo = Archivo("rutas.txt")

    #Se agregan las rutas al dron
    robot.setRutas(archivo.leerArchivo())

    #Se cierra el archivo
    archivo.cerrarArchivo()

    #Bucle para mover al dron
    resultados.append("== Reporte de entregas ==")

    print("== Reporte de entregas ==")

    for ruta in robot.getRuta():
        ruta = ruta.split()
        ruta = ruta[0]
        
        for direccion in ruta:
            robot.mover(direccion)

        solucion = "( " + str(robot.getPosicion()[0]) + ", " + str(robot.getPosicion()[1]) + " ) " + robot.getDireccion()
        print(solucion)
        resultados.append(solucion)

    #Se crea el archivo de salida y se escribe
    archivoSalida = Archivo("output.txt")

    archivoSalida.escribirArchivo(resultados)

    archivoSalida.cerrarArchivo()


if __name__ == '__main__':
    main()