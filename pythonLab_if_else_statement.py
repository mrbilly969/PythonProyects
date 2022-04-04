income = float(input("Enter the annual income: "))

#
# Escribe el código aquí:
#________________________

if income <= 85525.00:
    tax = (income*0.18)-556.02
else:
    tax= (income-85528)*0.32 + 14839.02
#________________________

tax = round(tax, 0)
if tax > 0:
    print ("El impuesto es de:", tax, "pesos.")
else:
    print ("El impuesto es de: 0.0 pesos.")
