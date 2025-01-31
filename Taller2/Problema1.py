"""Se desea realizar un programa en Python, que calcule las primeras cinco ventas diarias,
teniendo ya el calculado del promedio de la cinco venta diaria en 677.00 dólares.
Para el caso que nos corresponde ingrese los cinco valores de las ventas por teclado,
una vez teniendo los valores calcule el promedio; proceda a comparar si el mayor o menor al valor de B/.677.00."""

"""----------- Se Utilizo PyCharm -----------"""
ventas = []
for i in range(5):
    venta = float(input(f"Digite la venta {i+1}: "))
    ventas.append(venta)

promedio = sum(ventas) / len(ventas)

if promedio > 677.00:
    print("Es el mayor de las cinco ventas: ", promedio)
else:
    print("Es el menor de las cinco ventas: ", promedio)