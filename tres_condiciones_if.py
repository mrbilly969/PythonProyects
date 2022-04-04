

x=int(input("Introduce un número para evaluar por 3 condiciones: "))

cond1="Sí, la variable x es mayor a 5."
cond2="Sí, la variable x es también mayor a 10."
cond3="Sí, la variable x es mayor a 20."
no_cond="No superó esta condición."



print("\n¿El valor cumple con condición 1?: ", )
if x > 5: # Condición 1
    print(cond1)
else:
    print(no_cond)

print("\n¿El valor cumple con condición 2?: ", )
if x > 10: # Condición 2
    print(cond2)
else:
    print(no_cond)

print("\n¿El valor cumple con condición 3?: ", )
if x > 20: # Condición 3
    print(cond3)
else:
    print(no_cond)
