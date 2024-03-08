#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2 ?
#Self: if the number is a muliple of 4, print out a different meassage

num = int(input("Enter a number:"))
if(num % 2 == 0):
    if(num % 4 == 0):
        print("Divisible by 4")
    else:
        print("Number is even")
else:
    print("Number is odd")

#output-1: Enter a number:2
#          Number is even 
    
#output-2: Enter a number:4
#          Divisible by 4
    
#output-3: Enter a number:3
#          Number is odd