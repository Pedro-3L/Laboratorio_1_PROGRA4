from collections import deque

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


def calcularTotal(cola):
    if not cola:
        return 0
    producto = cola.popleft()
    print("Producto:", producto.nombre, "Q", producto.precio)
    return producto.precio + calcularTotal(cola)


cola = deque()

for i in range(5):
    print(f"Ingrese el nombre del producto #{i+1}:")
    nombre = input()
    print(f"Ingrese el precio #{i+1}:")
    precio = float(input())
    pro = Producto(nombre, precio)
    cola.append(pro)

total = calcularTotal(cola)
print("Total: Q", total)