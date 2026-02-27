'''
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
FinSi
'''

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
