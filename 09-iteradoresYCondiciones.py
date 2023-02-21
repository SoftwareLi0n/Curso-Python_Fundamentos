contrasenias = ['123.', 'hola123', 'roberto', 'rodolfo', 'julia']

for password in contrasenias:
    if password == 'roberto':
        print(f'****** Contraseña encontrada: {password}')
    else:
        intento = f'Intentando acceder: {password}'
        print(intento)