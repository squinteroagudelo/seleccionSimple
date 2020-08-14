# Ejercicio 1
inversion = float(input('Ingrese el valor de la inversión: $ '))
interes = float(input('Ingrese el porcentaje de interés:  '))
intereses = inversion * (interes / 100)

if intereses > 7000:
    inversion += intereses
    print(f'Es viable reinvertir\nSu nuevo saldo será $ {inversion}')
else:
    print('No es viable reinvertir')


# Ejercicio 2
nota_1 = float(input('Digite la nota 1: '))
nota_2 = float(input('Digite la nota 2: '))
nota_3 = float(input('Digite la nota 3: '))
promedio = (nota_1 + nota_2 + nota_3) / 3

if promedio >= 70:
    print('El alumno ha aprobado')
else:
    print('El alumno ha reprobado')

# Ejercicio 3
compra = float(input('Ingrese el valor de la compra: $ '))

if compra > 1000:
    total = compra - compra * 0.2
else:
    total = compra

print(f'El total a pagar es $ {total}')

# Ejercicio 4
horas_sem = float(input('Digite la cantidad de horas trabajadas en la semana: '))

if horas_sem <= 40:
    salario = horas_sem * 16
else:
    salario = (horas_sem - 40) * 20 + 40 * 16

print(f'El salario semanal del trabajador es: $ {salario}')

# Ejercicio 6
num1 = float(input('Digite el primer número: '))
num2 = float(input('Digite el segundo número: '))

if num1 == num2:
    print(f'Ha digitado el mismo número: {num1}')
elif num1 < num2:
    print(f'Orden ascendente: {num1}\t{num2}')
else:
    print(f'Orden ascendente: {num2}\t{num1}')
