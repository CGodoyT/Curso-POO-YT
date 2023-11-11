class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return {self.habilidad}

class EmpleadoArtista (Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def mostrar_habilidad(self):
        print("No tengo jajsa")

    def presentarse(self):
        #print(f'{self.mostrar_habilidad()}')
        #print(f'{super().mostrar_habilidad()}')
        print(f"Hola, soy: {self.nombre}, mi habilidad es {self.habilidad} y trabajo en {self.empresa}")

roberto = EmpleadoArtista("Roberto", 41,"argentino", "cantar", 5000000000, "Google")

roberto.presentarse()



herencia = isinstance(EmpleadoArtista, Persona)
instancia = isinstance(roberto, Artista)

print(instancia)
print(herencia)