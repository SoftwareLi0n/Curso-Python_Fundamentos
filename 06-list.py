# Declarar una lista
# Agregar un producto (append)
# Editar un producto
# Eliminar un producto del, pop, pop(indice), remove
# Acceder a uno de ellos
# Ordenar lista

# Declaramos lista
productos = ['Paneton', 'Azucar']

# Agregamos items a la lista
productos.append('Leche')
productos.append('Pan')
productos.append('Pollo')
productos.append('Gato')
productos.append('Regalo sorpresa')

# Editar item
productos[3] = 'Pan integral'

# Eliminar items
del productos[5]
productos.pop()
productos.pop(1)
productos.remove('Pollo')

# Acceder
producto_caro = f'El producto más caro: {productos[0]}'
print(producto_caro)

# Ordenar
productos.sort()
print(productos)