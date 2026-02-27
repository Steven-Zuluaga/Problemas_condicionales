# Ejercicio 7


Simulador de Inicio de Sesión Crea un programa que tenga un nombre de usuario y una contraseña almacenados en variables. Pide al usuario que ingrese sus credenciales y muestra:

• "Acceso concedido" si ambos coinciden.

• "Contraseña incorrecta" si el usuario existe pero la clave no.

• "Usuario no encontrado" si el nombre de usuario es incorrecto.


- Pseudocódigo

```
# usuario: steven.zuluaga
# constraseña: 123456

Escribir 'Usuario'
Leer a
Escribir 'Contraseña'
Leer a

Si (a == 'steven.zuluaga' y b == 123456) Entonces
  Escribir "Acceso concedido"

elif (a == 'steven.zuluaga' y no b == 123456) Entonces
  Escribir 'Contraseña incorrecta'

elif (no a == 'steven.zuluaga' y b == 123456) Entonces
  Escribir 'Usuario no encontrado'

else:
  Escribir 'No esta en el sistema'
```

- Código

```python 
# usuario: steven.zuluaga
# constraseña: 123456

a = str(input('Usuario:  '))
b = int(input('Contraseña: '))

if (a == 'steven.zuluaga' and b == 123456) :
  print("Acceso concedido")

elif (a == 'steven.zuluaga' and not b == 123456) :
  print("Contraseña incorrecta")

elif (not a == 'steven.zuluaga' and b == 123456) :
  print("Usuario no encontrado")

else:
  print('No esta en el sistema')
```
