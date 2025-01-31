""" Se desea realizar un programa en Python, que calcule las primeras cinco ventas diarias,
teniendo ya el calculado del promedio de la cinco venta diaria en 677.00 dólares.
Para el caso que nos corresponde ingrese los cinco valores de las ventas por teclado, una vez teniendo los
valores calcule el promedio; proceda a comparar si el mayor o menor al valor de B/.677.00."""

"""----------- Se Utilizo PyCharm -----------"""
nombre = input('\nIngrese su Nombre: ')  # Nombre Usuario
print(f"\nBienvenido {nombre}!\n")
op = 1
while op != 5:  # Se ejecuta mientras op sea diferente de 5
    print('--- Conversor de Divisas ---\n\n1.Dolares\n2.Colones\n3.Lempiras\n4.Pesos Colombianos\n5.Salir')  # Muestra las opciones
    op = int(input('\nIngresa una opcion: '))  # Usuario ingresa opcion
    if op == 1:
        Euro_a_Dolar = float(input('Ingresa una cantidad: '))  # Usuario ingresa la cantidad de euro a convertir a Dolares
        Euro_a_Dolar = Euro_a_Dolar / 1.21
        print(f"Resultado de la Conversion: ${Euro_a_Dolar:.2f}\n")
    elif op == 2:
        Euro_a_Colones = float(input('Ingresa una cantidad: '))  # Usuario ingresa la cantidad de euro a convertir en Colones
        Euro_a_Colones = Euro_a_Colones / 738.59
        print(f"Resultado de la Conversion: ${Euro_a_Colones:.2f}\n")
    elif op == 3:
        Euro_a_Lempiras = float(input('Ingresa una cantidad: '))  # Usuario ingresa la cantidad de euro a convertir en Lempiras
        Euro_a_Lempiras = Euro_a_Lempiras / 29.16
        print(f"Resultado de la Conversion: ${Euro_a_Lempiras:.2f}\n")
    elif op == 4:
        Euro_a_Pesos_Colombianos = float(input('Ingresa una cantidad: '))  # Usuario ingresa la cantidad de euro a convertir en Pesos Colombianos
        Euro_a_Pesos_Colombianos = Euro_a_Pesos_Colombianos / 4314.00
        print(f"Resultado de la Conversion: ${Euro_a_Pesos_Colombianos:.2f}\n")
    elif op == 5:
        print(f'Chao {nombre}...\n¡Gracias por Utilizar este Convertor de Divisas!!')
    else:
        print('Ingrese una opcion valida')