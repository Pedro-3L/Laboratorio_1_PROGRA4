class Palabra:
    def __init__(self, texto):
        self.texto = texto


class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0


def invertir(texto):
    if texto == "":
        return ""
    return invertir(texto[1:]) + texto[0]


pila = Pila()

print("Ingrese la cantidad de palabras")
cantidad = int(input())

for i in range(cantidad):
    print("Ingrese una palabra")
    texto = input()

    palabra = Palabra(texto)
    pila.push(palabra)


while not pila.esta_vacia():
    palabra = pila.pop()

    print(invertir(palabra.texto))