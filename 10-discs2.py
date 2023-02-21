jugador = {}
print(jugador)

jugador['nombre'] = "Mateo"
jugador['puntaje'] = 0
print(jugador)

jugador['puntaje'] = 200
print(jugador)

for llave, valor in jugador.items():
    print(f'{llave}: {valor}')