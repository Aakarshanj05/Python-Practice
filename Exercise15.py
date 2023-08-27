numbers = input("Enter the Numbers: ")
number_list=numbers.split()
count = 0

for number in number_list:
    count +=1
print(f"The length of the list is : {count}")

total = 0
for i in range(2,101,2):
    total += i
print(f"Sum of even number till 100 is : {total}")

