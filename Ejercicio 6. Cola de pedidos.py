from collections import deque
class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente


def atender(cola):
    if not cola:
        return
    pedido = cola.popleft()
    print("Numero de pedido:", pedido.numero)
    print("Cliente:", pedido.cliente)
    print()
    atender(cola)


cola = deque()
print("Ingrese la cantidad de pedidos")
cantidad = int(input())

for i in range(cantidad):
    print("Ingrese el numero de pedido")
    numero = int(input())
    print("Ingrese el nombre del cliente")
    cliente = input()

    pedido = Pedido(numero, cliente)
    cola.append(pedido)
print()
print("Atendiendo pedidos:")
atender(cola)