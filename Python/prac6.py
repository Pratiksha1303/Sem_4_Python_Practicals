# Ask the user for a string and print out whether this string is a palidrome or not.
#(using string reversal and for loops)

flag = 0
string = str(input("Enter a string:"))
rstring = string[::-1]

for i in range(len(string)):
    if string[i] != rstring[i]:
        flag = 1
        break

if flag == 0:
    print("Palindrome")
else:
    print("Not Palindrome")


#output-1:
#    Enter a string:hello
#    Not Palindrome     


#output-2:
#    Enter a string:noon
#    Palindrome
