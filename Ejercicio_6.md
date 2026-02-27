# Ejercicio 6


Verificador de Año Bisiesto Escribe un programa que determine si un año proporcionado por el usuario es bisiesto. Un año es bisiesto si es divisible por 4 excepto aquellos divisibles por 100, a menos que también sean divisibles por 400.


- Pseudocódigo

```
Escribir 'Escribir el año'
Leer a

Si a < 0 Entonces
  Escribir 'ERROR: Los años no pueden ser negativos'

Sino Si ((a % 4 == 0) y (a%100 != 0)) o (a % 400 == 0)Entonces
  Escribir 'El año es bisiesto'

Sino Entonces
  Escribir 'El año no es bisiesto'
FinSi
```

- Código

```python 
a = float(input('Escribe el año: '))

if a < 0 :
    print('ERROR: Los años no pueden ser negativos')

elif ((a % 4 == 0) and (a%100 != 0)) or (a % 400 == 0):
    print('El año es bisiesto')

else :
    print('El año no es bisiesto')
```
