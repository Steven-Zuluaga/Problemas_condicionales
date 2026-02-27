# Ejercicio 5


Sistema	de	Descuentos	de	Tienda
Una	tienda	ofrece	descuentos	basados	en	el	monto	de	la	compra:

• Si	la	compra	es	mayor	a	$1000,	descuento	del	20%.

• Si	está	entre	$500  y  $1000,	descuento	del	10%.

• Si	es	menor	a	$500,	no	hay	descuento.

Calcula	el	monto	final	que	debe	pagar	el	cliente.


- Pseudocódigo

```
Escribir 'valor a pagar'
Leer a

Si a < 0 Entonces
  Escribir 'El valor a pagar no puede ser negativo'
FinSi

Si  a > 1000 Entonces
  descuento = a * 0.20
  valor_a_pagar = a - descuento
  Escribir 'El monto a pagar es ' , valor_a_pagar

Sino Si a >= 500 Entonces
  descuento = a * 0.10
  valor_a_pagar = a - descuento
  Escribir 'El monto a pagar es' , valor_a_pagar

Sino Si a > 0 Entonces
  Escribir 'No se aplica descuento'
  Escribir 'El monto a pagar es' , a
```

- Código

```python 
a = float(input('valor a pagar: '))

if a < 0 :
  print('El valor a pagar no puede ser negativo')

if a > 1000 :
  descuento = a * 0.20
  valor_a_pagar = a - descuento
  print(f'El monto a pagar es {valor_a_pagar}')

elif a >= 500 :
  descuento = a * 0.10
  valor_a_pagar = a - descuento
  print(f'El monto a pagar es {valor_a_pagar}')

elif a > 0 :
  print('No se aplic}a descuento')
  print(f'El monto a pagar es {a}')
```
