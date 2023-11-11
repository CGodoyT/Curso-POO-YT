#Clase madre (la que otorga atributos y metodos)
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    #Funcion por defecto
    def hablar(self):
        print("Hola, estoy hablando un poco")


#Clase hija (la que hereda los atributos y metodos de la clase madre)
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        #Funcion super() con los atributos que se quieren heredar
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    #Funcion reescribrida para Empleado
    def hablar(self):
        print("No, estoy ocupado")


persona1 = Empleado("Roberto", 41, "argentino", "programador", 5000000000)

persona1.hablar()