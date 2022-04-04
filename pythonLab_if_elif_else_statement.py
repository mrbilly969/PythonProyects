# Programa para determinar si un año es bisiesto o común, conforme al Calendario Gregoriano.
# Autor: Andrés Ortega Martínez

year = int(input("Ingresa un año para evaluar: "))

# Escribe tu código aquí.
#________________________
# Supuestos:
# Si el número de año no es divisible entre 4, es un año común;
# De otra forma, si el número de año no es divisible entre 100, es año bisiesto;
# De otra forma, si el número de año no es divisible entre 400, es un año común;
# De otra forma, es año bisiesto.

comn="Es año común."
leap="Es año bisiesto."
not_greg_cal="Durante este año aun no iniciaba el Calendario Gregoriano."

if year < 1582:
    print(not_greg_cal)
elif year%4 != 0:
    print(comn)
elif year%100 != 0:
    print(leap)
elif year%400 != 0:
    print(comn)
else:
    print(leap)



#________________________

