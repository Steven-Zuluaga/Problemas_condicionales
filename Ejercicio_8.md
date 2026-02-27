# Ejercicio 8


Clasificación de Triángulos Pide al usuario las longitudes de los tres lados de un triángulo. El programa debe determinar si el triángulo es:

• Equilátero (tres lados iguales).

• Isósceles (dos lados iguales).

• Escaleno (ningún lado igual).

- Pseudocódigo

```
Escribir 'Valor lado 1'
Leer a
Escribir 'Valor lado 2'
Leer b
Escribir 'Valor lado 3'
Leer c

Si a <= 0 o b <= 0 o c <= 0 Entonces
  Escribir 'ERROR: No pueden haber lados negativos ni iguales a 0'

Sino Si a == b y b == c y a == c Entonces
  Escribir 'El triangulo es Equilatero'

Sino Si a == b o b == c o a == c Entonces
  Escribir 'El triangulo es Isosceles'

Sino  Entonces
  Escribir 'El triangulo es Escaleno'
FinSi
```

- Código

```python 
a = float(input('Valor lado 1: '))
b = float(input('Valor lado 2: '))
c = float(input('Valor lado2 3: '))

if a <= 0 or b <= 0 or c <= 0 :
  print('ERROR: No pueden haber lados negativos ni iguales a 0')

elif a == b and b == c and a == c :
  print('El triangulo es Equilatero')

elif a == b or b == c or a == c :
  print('El triangulo es Isosceles')

else :
  print('El triangulo es Escaleno')
```
