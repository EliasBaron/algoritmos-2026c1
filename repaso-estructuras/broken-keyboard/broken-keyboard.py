# Se recibe en cada linea entre 1 y 100000 letras, guiones bajos y dos caracteres especiales [ y ], cuando se recibe "[" se recibió un Home, por lo que el texto que le sigue a ese caracter va al inicio de la cadena final, y cuando se recibe un "]" se recibe un End, por lo que el texto se empieza a escribir al final de toda la cadena.

import sys

for line in sys.stdin:
    
    letters = line.strip()

    inicio = []
    fin = []

    for l in letters:
      if l == "[":
        fin = inicio + fin
        inicio = []
      elif l == "]":
        inicio = inicio + fin
        fin = []
      else: inicio.append(l)  
      
    print(''.join(inicio + fin))