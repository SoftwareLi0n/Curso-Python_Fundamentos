from models.Contacto import Contacto
import os

CARPETA = 'contactos/'
EXTENSION = '.txt'

def app():
    crear_directorio()

    mostrar_menu()

    preguntar = True

    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            crear_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            listar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo...')

def eliminar_contacto():
    try:
        nombre = input('Ingrese el nombre del contacto que desea eliminar:\r\n')

        Contacto.eliminar_contacto(nombre)
    except Exception as ex:
        print('No se pudo eliminar el contacto')
        print('Detalle: '+str(ex))

def buscar_contacto():
    try:
        nombre = input('Ingrese el nombre del contacto que desea consultar:\r\n')

        with open(CARPETA+nombre+EXTENSION, 'r', encoding='utf-8') as archivo:
            print('\r\nInformación del contacto')
            print('*************')
            print(archivo.read().strip())
            print('*************')
    except Exception as ex:
        print('No se pudo obtener información del contacto')
        print('Detalle: '+str(ex))

def listar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA+archivo, 'r', encoding='utf-8') as archivo_contacto:
            print('*************')
            print(archivo_contacto.read().strip())
            print('*************')
            print('\r')

def editar_contacto():
    print('Vamos a editar el contacto')

    nombre_antiguo = input('Nombre del contacto a editar:\r\n')

    existe = Contacto.existe_contacto(nombre_antiguo)

    if existe:
        nombre_contacto = input('Nombre del contacto:\r\n')
        telefono_contacto = input('Teléfono del contacto:\r\n')
        categoria_contacto = input('Categoría del contacto:\r\n')

        os.rename(CARPETA+nombre_antiguo+EXTENSION, CARPETA+nombre_contacto+EXTENSION)

        contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
        contacto.guardar()
    else:
        print('El contacto a editar, no existe')

    app()

def crear_contacto():
    print('Escriba los datos del nuevo contacto')
    nombre_contacto = input('Nombre del contacto:\r\n')

    existe = Contacto.existe_contacto(nombre_contacto)

    if existe:
        print('El contacto ya se encuentra registrado')
    else:
        telefono_contacto = input('Teléfono del contacto:\r\n')
        categoria_contacto = input('Categoría del contacto:\r\n')

        contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
        contacto.guardar()
    
    app()

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