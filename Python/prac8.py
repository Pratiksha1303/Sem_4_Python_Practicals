# Write a pogram (using functions!) that asks the user for a long string function. Containing multiple words. Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string: My name is Michele Then I would see the string: Michele is naming My shown back to me.

def reverse(input_string):
    words = input_string.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

def main():
    user_input = input("Enter a sentence: ")

    reversed_string = reverse(user_input)

    print("Original String:", user_input)
    print("Reversed String:", reversed_string)

main()


#output:

# Enter a sentence: This is python program
# Original String: This is python program
# Reversed String: program python is This