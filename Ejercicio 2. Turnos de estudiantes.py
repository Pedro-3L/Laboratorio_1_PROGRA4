from collections import deque
class Estudiante:
    def __init__(self, nombre, carne):
        self.nombre = nombre
        self.carne = carne

def atender(cola):
    if not cola:
        return
    estudiante = cola.popleft()
    print("Nombre:", estudiante.nombre)
    print("Carne:", estudiante.carne)
    print()
    atender(cola)


cola = deque()
for i in range(5):
    print("Ingrese el nombre del estudiante")
    nombre = input()
    print("Ingrese el numero de carne")
    carne = input()
    estudiante = Estudiante(nombre, carne)
    cola.append(estudiante)
print()
print("Estudiantes pendientes:")

atender(cola)