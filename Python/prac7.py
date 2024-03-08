# Write a program (!function) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates
# Self: write two different functions to do this - one using a loop and constructing a list, and another using set

def remove_duplicates(input_list):
    result_list = []
    seen_elements = set()

    for element in input_list:
        if element not in seen_elements:
            result_list.append(element)
            seen_elements.add(element)

    return result_list

user_input = input("Enter a list: ")
original_list = [int(num) for num in user_input.split(',')]

result_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List with Duplicates Removed:", result_list)


#output:

# Enter a list: 2,4,5,2,6,4,1,5
# Original List: [2, 4, 5, 2, 6, 4, 1, 5]      
# List with Duplicates Removed: [2, 4, 5, 6, 1]