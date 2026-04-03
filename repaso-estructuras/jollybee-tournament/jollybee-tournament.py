## Obs: Se nos pide calcular el numero de walkover matches (Los cuales son los partidos en donde solo está disponible un jugador). Para esto se nos da:
# el numero de casos a probar. Y por cada caso dos lineas:
# una en donde se recibe N y M, siendo N el numero de jugadores del torneo (2°n) y M el numero de jugadores retirados.
# Luego en otra linea, separados todos los numeros de los jugadores que se retiraron.

# Entonces, contamos con:
# Cantidad total de jugadores / y de partidos.
# Cantidad de jugadores que se rindieron.
# Numeros de cada jugador que se rindió del torneo.

# Se pueden observar los siguientes casos de partido:
# Cuando están los dos jugadores disponibles, se juega un partido normal.
# Cuando falta uno o el otro, gana el unico jugador disponible por wm.
# Cuando no está disponible NINGUNO de los dos jugadores, entonces no se juega el partido, el jugador que "pasa" en el realidad un aviso de que fue un partido no jugado, por lo cual, el jugador que "juegue" contra un partido no jugado, automaticamente gana por wm.


# El array inicial
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    if M > 0:
        withdrawedPlayers = list(map(int, input().split()))
    else:
        withdrawedPlayers = []
        input()  # consumir la línea vacía
    
    players = [1] * (2 ** N)
    for i in withdrawedPlayers:
        players[i - 1] = 0
        
    walkovers = 0

    # El loop de rondas
    for ronda in range(N):
        nueva_ronda = []

        for i in range(0, len(players), 2):
            a = players[i]
            b = players[i + 1]
            # si a != b → walkover
            if a != b:
              walkovers += 1
              
            # calcular avanza
            if a == 1:
              avanza = a
            else:
              avanza = b
            # guardarlo en nuevo array
            nueva_ronda.append(avanza)

        # reemplazar players con nuevo array
        players = nueva_ronda
        
    print(walkovers)