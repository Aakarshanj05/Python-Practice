import random

Names = input("Enter the Names of the Payers: " )

names_list=Names.split(',')
length=len(names_list)

random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]} will pay the bill")