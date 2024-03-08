# Take a list say for example this one: a = [1,1,2,3,5,8,13,21,34,55,89], and write a program that prints out all the elements on the list that are less than 5

#Self: intead the elements one by one make a new list that has all the elements less than 5 from this list in it and print out this new list

#first method to get the elements less than 5

L = [1,1,2,3,5,8,13,9,4]
for i in L:
    if(i<5):
        print(i)

#output:
        1
        1
        2
        3
        4


#second method to get the elements less than 5 in a new list

a = [1, 1, 2, 3, 5, 8, 13, 9, 4]

new_list = []

for element in a:
    if element < 5:
        new_list.append(element)

print("Elements less than 5:", new_list)

#output: Elements less than 5: [1,1,2,3,4]