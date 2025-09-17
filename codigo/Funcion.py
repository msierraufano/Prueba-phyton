#Esto es una función
def lower_num (num1, num2):
    if num1 <= num2:
        lowest = num1
    else :
        lowest = num2
    return lowest

#Esto es una llamada a una función
first_num = int (input ("Enter the first number:"))
second_num = int (input ("Enter the second number:"))
lower_num (first_num, second_num)
print ("The lowest is" + str(lower_num(first_num, second_num)))



