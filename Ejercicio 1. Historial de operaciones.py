class Operacion:
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


def sumar(pila):
    if pila.esta_vacia():
        return 0
    operacion = pila.pop()
    return operacion.numero + sumar(pila)


pila = Pila()
for i in range(5):
    print("Ingrese un numero")
    numero = int(input())

    operacion = Operacion(numero)
    pila.push(operacion)

print("Suma:", sumar(pila))

