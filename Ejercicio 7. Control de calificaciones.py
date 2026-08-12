class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion


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


def mostrarAprobados(pila):
    if pila.esta_vacia():
        return
    estudiante = pila.pop()

    if estudiante.calificacion >= 61:
        print("Nombre:", estudiante.nombre)
        print("Calificacion:", estudiante.calificacion)
        print()
    mostrarAprobados(pila)


pila = Pila()
for i in range(5):
    print("Ingrese el nombre del estudiante")
    nombre = input()

    print("Ingrese la calificacion")
    calificacion = float(input())

    estudiante = Estudiante(nombre, calificacion)
    pila.push(estudiante)
print()
print("Estudiantes aprobados:")
mostrarAprobados(pila)