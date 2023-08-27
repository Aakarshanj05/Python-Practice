'''names = input("Enter the names: ")
name_list = names.split()  # Split input into a list of names

for name in name_list:
    print(name)'''

list1 = [2, 3, 4, 5]
squares = []

for i in list1:
    square = i ** 2
    squares.append(square)

print("The list of square is: " ,squares)


#for-else

tuple1 = {2,5,3,4,7}
for i in tuple1:
    print(i)
    if i == 5:
        break
else:
    print("Loop is Successfully Completed")
print("Out of For/else")
