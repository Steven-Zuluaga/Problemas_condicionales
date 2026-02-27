# Ejercicio 9


Calculadora de Índice de Masa Corporal (IMC) Solicita el peso (kg) y la altura (m) del usuario. 
Calcula el IMC (𝐼𝑀𝐶 = peso/ altura**2)

•	<18.5: Bajo peso

•	18.5 − 24.9: Normal

•	25.0 − 29.9: Sobre

•	≥30.0: Obesidad


- Pseudocódigo

```
Escribir 'Cuanto pesas'
Leer a
Escribir 'Cuanto mides'
Leer b

IMC = (a / (b ** 2))

Si a <= 0 o b <= 0 Entonces
  Escribir 'ERROR: Los valores no son correctos'

Sino Si IMC < 18.5 Entonces
  Escribir 'Bajo peso'

Sino Si IMC > 18.5 y IMC < 24.9 Entonces
  Escribir 'Normal'

Sino Si IMC > 19 y IMC < 29.9 Entonces
  Escribir 'Sobrepeso'

Sino Entonces
  Escribir 'Obesidad'
FinSi

```

- Código

```python 
a = float(input('Cuanto pesas(kg): '))
b = float(input('Cuanto mides(m): '))

IMC = (a / (b ** 2))

if a <= 0 or b <= 0 :
  print('ERROR: Los valores no son correctos')

elif IMC < 18.5 :
  print('Bajo peso')

elif IMC > 18.5 and IMC < 24.9:
  print('Normal')

elif IMC > 19 and IMC < 29.9:
  print('Sobrepeso')

else :
  print('Obesidad')

```
