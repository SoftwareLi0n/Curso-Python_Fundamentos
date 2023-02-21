def app():
    archivo = open('archivo.txt', 'w')

    for i in range(0, 10):
        archivo.write(f'Linea: {i}\n')

    archivo.close()

app()