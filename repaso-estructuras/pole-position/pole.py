# Qué se recibe?
# se recibe el numero de autos en la carrera, las siguientes N lineas, reciben el numero del auto y el numero de posiciones que ganó o perdió durante la carrera, comparada con la salida inicial. Los numeros de los autos que se reciben están ordenados por resultado. O sea, si recibo primero: 3 0, es porque ganó el auto numero 3 y salió primero.

# Qué se espera? 
# Se espera devolver la grilla de salida inicial. Solamente mostrando el numero de los autos en orden.

# Observaciones: 
# Para calcular la salida, se puede guardar todo lo recibido en una lista de tuplas, con el numero del auto y los puestos ganados/perdidos. Primero, cheuqear que esa lista no sea vacía y que nos hayan pasado todos los autos que nos declararon con el primer n. Luego se va recorriendo esa lista, armando la otra en paralelo, haciendo el calculo de posición final - posicionesvariadas, podriamos llegar a guardar en la otra lista una tupla con el numero de cada auto junto a su posición inicial calculada, se podría ordenar en el guardado, para luego solamente devolver los primeros valores de cada tupla como lista. 


# totalCars = 3
# raceResult = [(3,2),(2,0),(1,-2)]

# raceGrid = list(0,0,0)

# for i in range(1, totalCars):
#   carResult = raceResult[i]
#   startPosition = i + carResult[1]
  
#   if startPosition <= 0 or startPosition > totalCars or raceGrid[startPosition] != 0:
#       return -1
#   else raceGrid[startPosition] = carResult[0]
  
#   print(raceGrid)
  
  
while True:
    # 1. Leemos la cantidad de autos de esta carrera
    n = int(input())
    
    # 2. Condición de corte: si n es 0, terminamos el programa
    if n == 0:
        break
        
    # 3. Preparamos nuestra grilla vacía y nuestra bandera
    grilla = * n
    es_valido = True
    
    # 4. Leemos las N líneas siguientes (los datos de cada auto)
    for i in range(n):
        # input().split() separa "1 -2" en ["1", "-2"]. map lo pasa a enteros.
        auto, variacion = map(int, input().split())
        
        # OJO: Solo procesamos si hasta ahora todo viene siendo válido.
        # Si ya falló antes, igual debemos seguir leyendo los inputs (los "input().split()")
        # para no desfasar la lectura de la siguiente carrera.
        if es_valido:
            # i es la posición de llegada (0, 1, 2...). 
            posicion_inicial = i + variacion
            
            if posicion_inicial < 0 or posicion_inicial >= n or grilla[posicion_inicial] != 0:
                es_valido = False
            else:
                grilla[posicion_inicial] = auto

    # 5. Imprimimos el resultado de esta carrera
    if not es_valido:
        print("-1")
    else:
        print(*(grilla))
  
  

