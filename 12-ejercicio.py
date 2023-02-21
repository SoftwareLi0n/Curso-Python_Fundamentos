playlist = {}
playlist['canciones'] = []

def app():
    preguntarNombre = True

    while preguntarNombre:
        nombre_playlist = input('Nombre de tu playlist: ')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            preguntarNombre = False

            agregar_canciones()

def agregar_canciones():
    preguntarCancion = True

    while preguntarCancion:
        nombre_playlist = playlist['nombre']
        pregunta = f'Agregue canciones a {nombre_playlist} \n\r ("X" para salir): '

        cancion = input(pregunta)

        if cancion == 'X':
            preguntarCancion = False
            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion)


def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print('\n\r')
    print(f'PlayList: {nombre_playlist} \n\r')
    print('Canciones: ')

    for cancion in playlist['canciones']:
        print(f'- {cancion}')


app()