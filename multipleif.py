size = input("Enter the size of the pizza: ")
bill = 0
if size == 'S' or size == 's':
    bill +=100
    print("Small pizza price is 100 Rs.")
elif size == 'M' or size == 'm':
    bill += 200
    print("Medium pizza price is 200 Rs.")
else:
    bill += 300
    print("Large pizza price is 300 Rs.")
add_pepperoni = input("Do you want pepperoni(Y/N? ")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill +=30
    else:
        bill +=50
extra_cheese = input("Do you want extra cheese (Y/N?")
if extra_cheese == 'Y' or extra_cheese == 'y':
    if size =='S' or size == 's' :
         bill +=20
    else:
        bill +=40
print(f"You final bill is {bill}")


