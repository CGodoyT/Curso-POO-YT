# MRO : METHOD RESOLUTION ORDER / Orden de Resolucion de metodos
#           Explica que orden tienen los metodos heredados si comparten el mismo nombre

class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")


class C(A):
    def hablar(self):
        print("Hola desde C")


class D(B, C):
    def hablar(self):
        print("Hola desde D")


# Explica el orden de las herencias
print(D.mro())
# D > B > C > A

# El objecto d obtiene la herencia de todas las clases
d = D()
d.hablar()


# Ejecutar un objeto con metodos heredados de mas arriba en el orden
# Llamar a la clase y el metodo requerido pasandole el objeto
B.hablar(d)
