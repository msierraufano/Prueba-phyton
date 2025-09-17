def highest_number (num1, num2, num3):
    if num1 >= num2 and num2 >= num3:
        highest = num1
    elif num2 >= num1 and num2 >= num3:
         highest = num2
    elif num3 >= num1 and num3 >= num2:
        highest = num3
    else:
        highest = num1, num2, num3
num1=int (input("Enter the first number"))
num2=int (input("Enter the second number"))
num3=int (input("Enter the thirten number"))

print("The  highest number is" + str (highest_number))
