import os

CARPETA = 'contactos/'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

    def guardar(self):
        with open(CARPETA+self.nombre+EXTENSION, 'w', encoding='utf-8') as archivo:
            archivo.write('Nombre: '+self.nombre +'\n')
            archivo.write('Teléfono: '+self.telefono +'\n')
            archivo.write('Categoría: '+self.categoria )

        print('\n Contacto agregado \n')

    def existe_contacto(nombre_contacto):
        existe = os.path.exists(CARPETA+nombre_contacto+EXTENSION)
        return existe
    
    def eliminar_contacto(nombre_contacto):
        existe = Contacto.existe_contacto(nombre_contacto)

        if existe:
            os.remove(CARPETA+nombre_contacto+EXTENSION)
            print('\r\n Contacto Eliminado')
        else:
            print('El contacto no existe')