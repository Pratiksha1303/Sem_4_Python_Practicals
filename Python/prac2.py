#develop a python program to make simple calculator using a conditional loop 

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operator = input("Enter the operation you want to perform:(+,-,*,/):")

add = int
subtract = int
multiply = int
divide = int
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2

if(operator == '+'):
    print(add)
elif(operator == '-'):
    print(subtract)
elif(operator == '*'):
    print(multiply)
elif(operator == '/'):
    if(num1 != 0):
           print(num1 / num2)
    else:
         print("Not divisible by zero")

#output: Enter the first number:10
#        Enter the second number:5
#        Enter the operation you want to perform:(+,-,*,/):/
#        2.0