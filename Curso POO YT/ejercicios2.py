class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Soy {self.nombre}, y tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Mi grado es {self.grado}")


estudiante1 = Estudiante("Cristian", 12, "octavo")
estudiante1.presentarse()
estudiante1.mostrar_grado()
