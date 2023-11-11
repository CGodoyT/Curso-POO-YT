#Clase
class Celular:

    #Metodo: funcion creada dentro de una clase 
    #Constructor: crea un objeto con los valores iniciales
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    
    def llamar(self):
        print(f"Estás haciendo una llamada desde un: {self.modelo}")
        
    def cortar(self):
        print(f"Cortaste la llamda desde tu: {self.modelo}")
    
#Objetos        
celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone", "96")

print(celular2.marca)

celular2.cortar()