# Create a program that asks the user to enter their name and their ages. Print out a message addresses to them that tells them the year that they will turn 100 years old


#method-1 : without importing "date from datetime"

name = input("Enter your name: ")
age = int(input("Enter your age: "))

turning_100 = 2024 + (100 - age)

print(f"Hello, {name}! You will turn 100 years old in the year {turning_100}.")

#output:

# Enter your name: Pratiksha
# Enter your age: 21
# Hello, Pratiksha! You will turn 100 years old in the year 2103.


#method-2 : with importing "date from datetime"

from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = date.today().year
year_of_turning_100 = current_year + (100 - age)

print(f"Hello, {name}! You will turn 100 years old in the year {year_of_turning_100}.")

#output:

# Enter your name: Pratiksha
# Enter your age: 21
# Hello, Pratiksha! You will turn 100 years old in the year 2103.


