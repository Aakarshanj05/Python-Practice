heights = input("Enter the heights of the candidates: ")
height_list=heights.split()
count=0
for height in height_list:
    count = count+1

for height in range(0,count):
    height_list[height]=int(height_list[height])

total=0
for person in height_list:
    total=total+person
avg = total/count
print(round(avg))



