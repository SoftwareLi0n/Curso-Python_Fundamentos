# CRUD
# C = Create
# R = Read
# U = Update
# D = Delete

import os

CARPETA = 'contactos/'

def app():
    crear_directorio()

    mostrar_menu()

    preguntar = True

    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            print('Agregar contacto')
            preguntar = False
        elif opcion == 2:
            print('Editar contacto')
            preguntar = False
        elif opcion == 3:
            print('Ver contactos')
            preguntar = False
        elif opcion == 4:
            print('Buscar contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar contacto')
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo...')

def mostrar_menu():
    print('Seleccione del menú lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

app()