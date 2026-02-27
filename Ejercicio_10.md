# Ejercicio 10


Juego de Piedra, Papel o Tijera Escribe un programa donde el usuario ingrese su opción y el programa genere una opción aleatoria para la computadora (usando import random). Utiliza condicionales para determinar quién gana, quién pierde o si hay un empate.

•	<18.5: Bajo peso

•	18.5 − 24.9: Normal

•	25.0 − 29.9: Sobre

•	≥30.0: Obesidad


- Pseudocódigo

```
Algoritmo jugar() Hacer

    opciones = ['piedra', 'papel', 'tijera']

    Leer jugador

    Si jugador no en opciones Entonces
        Escribir 'ERROR: Opción no válida'
        returornar
    FinSi

    eleccion = random.choice(opciones)
    Escribir 'La computadora eligió' , eleccion

    Si jugador == eleccion Entonces
        Escribir 'Es un empate'
    Sino Si (jugador == 'piedra' y eleccion == 'tijera') o \
            (jugador == 'papel' y eleccion == 'piedra') o \
            (jugador == 'tijera' y eleccion == 'papel') Entonces
        Escribir 'Ganaste'
    Sino Entonces
        Escribir 'Perdiste'
    FinSi
FinAlgoritmo

```

- Código

```python 
import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']

    jugador = input('¿piedra, papel, tijera?: ')

    if jugador not in opciones:
        print('ERROR: Opción no válida')
        return

    eleccion = random.choice(opciones)
    print(f'La computadora eligió: {eleccion}')

    if jugador == eleccion:
        print('¡Es un empate!')
    elif (jugador == 'piedra' and eleccion == 'tijera') or \
         (jugador == 'papel' and eleccion == 'piedra') or \
         (jugador == 'tijera' and eleccion == 'papel'):
         print('Ganaste')

    else:
        print('Perdiste')

jugar()

```
