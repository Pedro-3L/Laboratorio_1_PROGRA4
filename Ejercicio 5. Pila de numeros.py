class Numero:
    def __init__(self, numero):
        self.numero = numero


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



pila = Pila()
for i in range(6):
    print("Ingrese un numero")
    numero = int(input())

    num = Numero(numero)
    pila.push(num)

def pares(pila):
    if pila.esta_vacia():
        return 0
    num = pila.pop()
    if num.numero % 2 == 0:
        return 1+ pares(pila)
class Numero:
    def __init__(self, numero):
        self.numero = numero


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



pila = Pila()
for i in range(6):
    print("Ingrese un numero")
    numero = int(input())

    num = Numero(numero)
    pila.push(num)

def pares(pila):
    if pila.esta_vacia():
        return 0
    num = pila.pop()
    if num.numero % 2 == 0:
        return 1+ pares(pila)
    else:
        return pares(pila)

print("Cantidad de numeros pares:", pares(pila))