from abc import ABC, abstractmethod

# Definir la classe abstracta Animal
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        return f"Soc un {self.especie} i tinc {self.edat} anys."

# Definir les subclasses
class Cavall(Animal):
    def xerrar(self):
        return "Hiii!"

    def mourem(self):
        return "Galopar"

class Dofí(Animal):
    def xerrar(self):
        return "Eeee-eee!"

    def mourem(self):
        return "Nedar"

class Abella(Animal):
    def xerrar(self):
        return "Bzzz!"

    def mourem(self):
        return "Volar"

    def picar(self):
        return "He picat!"

class Huma(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        return "Hola!"

    def mourem(self):
        return "Caminar"

class Fiet(Huma):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares

    def nompares(self):
        return f"Els meus pares es diuen {', '.join(self.pares)}."

class Centaure(Cavall, Huma):
    def __init__(self, especie, edat, nom):
        Cavall.__init__(self, especie, edat)
        Huma.__init__(self, especie, edat, nom)

    def xerrar(self):
        return "Parlo i hennim"

    def mourem(self):
        return "Correr"

# Definir la classe Xou
class Xou:
    def xerrar(self):
        return "Xou xerrar!"

    def mourem(self):
        return "Xou mourem!"

    def quisoc(self):
        return "Soc un Xou!"

# Crear la llista d'elements de cada tipus
elements = [
    Cavall("Cavall", 5),
    Dofí("Dofí", 8),
    Abella("Abella", 1),
    Huma("Huma", 25, "Anna"),
    Fiet("Fiet", 7, "Pere", ["Anna", "Joan"]),
    Centaure("Centaure", 15, "Hercules"),
    Xou()
]

# Cridar els mètodes iguals en un bucle
for element in elements:
    print(element.quisoc())
    print(element.xerrar())
    print(element.mourem())
    if isinstance(element, Abella):
        print(element.picar())
    if isinstance(element, Fiet):
        print(element.nompares())
