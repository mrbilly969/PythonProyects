#Programa para que el usuario adivine número del 1-1000
#Autor: Andrés Ortega Martínez (A petición de un mago aprendiz.)

msg_wrong= "Ha ha! You're stuck in my loop"
msg_right= "Well done, mugggle! You are free now."
secret_number= 777
entry= int(input(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""))

while entry <= secret_number:
    if entry != secret_number:
        print(msg_wrong, entry)
        entry += 1
    else: 
        print(msg_right, entry)
        exit()
