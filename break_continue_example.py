largest_number= -99999999
counter = 0
msj= "Enter a number or type -1 to end program: "

number = int(input(msj))

while number != 1:
    if number == 1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input(msj))

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
