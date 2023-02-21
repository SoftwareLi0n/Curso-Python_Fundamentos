class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_informacion(self):
        print(f'Persona: {self.nombre} {self.apellido}, tiene {self.edad} años')

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, nivel):
        super().__init__(nombre, apellido, edad)
        self.nivel = nivel

    def mostrar_informacion(self):
        print('Hola como estas')

alumno = Alumno('Jesús', 'Nazareno', 33, 'Superior')
alumno.mostrar_informacion()
print(alumno.nivel)
