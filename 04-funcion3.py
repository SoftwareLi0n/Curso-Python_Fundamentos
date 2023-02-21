# titulo: No desperdicies tu vida
# titulo: *** NO DESPERDICIES TU VIDA ***

def arreglar_titulo(nombre_libro):
    nuevo_nombre = f'*** {nombre_libro.upper()} ***'
    return nuevo_nombre

libro = arreglar_titulo('No desperdicies tu vida')
print(libro)