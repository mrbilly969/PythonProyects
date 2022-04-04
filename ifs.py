import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    if n%2 != 0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")


#if __name__ == '__main__':
#    x = int(input("¿Qué tal está el clima?: [Frío, Templado o Caliente]"))

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    num_mayor = num1
else:
    num_mayor = num2

print("El número mayor es:", num_mayor)
