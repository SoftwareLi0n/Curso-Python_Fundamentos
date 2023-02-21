def app():
    with open('archivo.txt') as archivo:
        # print(archivo.read())

        for linea in archivo:
            print(linea.rstrip())
   
app()