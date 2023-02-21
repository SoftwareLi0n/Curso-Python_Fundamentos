configuracion = {
    'titulo': 'Mi recibo',
    'descripcion': 'Consulta tu recibo de agua y luz',
    'proveedor': 'Software Lion'
}

# Remplazar valor existente
configuracion['titulo'] = 'Mi recibo Perú'

# Agregar un nuevo valor
configuracion['modo'] = 'dark'

# Eliminar item del diccionario
del configuracion['descripcion']

# acceder a valor
titulo = configuracion['titulo']

print(f'Descarga desde la play store: {titulo}')