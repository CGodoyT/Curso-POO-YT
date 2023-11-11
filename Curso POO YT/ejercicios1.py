class Estudiante():
    def __init__ (self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")

nombre=input("Nombre del estudiante: ")
edad=input("Edad del estudiante: ")
grado=input("Grado del estudiante: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n
      Nombre: {estudiante.nombre}
      Edad: {estudiante.edad}
      Grado: {estudiante.grado}
      """)

while True:
    estudiar = input().lower
    if (estudiar() == "estudiar"):
        estudiante.estudiar()