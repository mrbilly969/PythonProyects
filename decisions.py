# Letura de tres números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

#Evaluar cuál de los números es el mayor y
# registrarlo como la variable num_mayor.

num_mayor = max(num1, num2, num3)
num_menor = min(num1, num2, num3)

#Imprimir el resultado

print("El número mayor es:", num_mayor)
print("El número menor es:", num_menor)
