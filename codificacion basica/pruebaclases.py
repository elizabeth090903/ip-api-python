# Definimos la clase
class ClaseNombre:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

    def imprimirNombre(self):  
        print("Mi nombre es:", self.nombre)

    def imprimirCiudad(self):  
        print("Yo soy de:", self.ciudad)


# Creamos instancias de la clase y usamos sus métodos
persona1 = ClaseNombre("Tomas", "Tehuacan")
persona1.imprimirNombre()
persona1.imprimirCiudad()

persona2 = ClaseNombre("Carlos", "Puebla")
persona2.imprimirNombre()
persona2.imprimirCiudad()

persona3 = ClaseNombre("Gloria", "Sonora")
persona3.imprimirNombre()
persona3.imprimirCiudad()

persona4 = ClaseNombre("Alfredo", "California")
persona4.imprimirNombre()
persona4.imprimirCiudad()

persona5 = ClaseNombre("Gonzalo", "Tamaulipas")
persona5.imprimirNombre()
persona5.imprimirCiudad()

persona6 = ClaseNombre("Alf", "Nogales")
persona6.imprimirNombre()
persona6.imprimirCiudad()

persona7 = ClaseNombre("Zalo", "Tehuacan")
persona7.imprimirNombre()
persona7.imprimirCiudad()

