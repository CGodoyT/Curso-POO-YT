class Animal:
    def comer(self):
        print("El animal está comiendo")


class Mamifero(Animal):
    def amamantar(self):
        print("El mamifero está amamantando")


class Ave(Animal):
    def volar(self):
        print("El ave está volando")


class Murcielago(Mamifero, Ave):
    pass


murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())
