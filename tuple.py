#TUPLES IN PYTHON

tuple1 = (12,6,-8, True)
print(tuple1[0:3])
print(type(tuple1))
print(len(tuple1))
tuple2=(45,46,55)
tuple3=(tuple1+tuple2)
print(tuple3)
print(len(tuple3))
print(max(tuple3))
list1=[1,2,3]
print(tuple(list1))

tuple4=(10)*5
print(tuple4)


# SETS IN PYTHON
# Sets are unorderd due to that also we cant do indexing also they are immutable

set1 = {1,2,3,4,5,6}
set2 = {'Aakarshan', 'Jha', 'Atul', 'Kishore', 'Akash', 'Singh'}
set3 = {1, 'Aakarshan', 2, 'Jha'}
set4 = {7,8,9,10}
print(set1)
print(set2)
print(set3)

print(set1,set4)
print(type(set1))
print(type(set2))

set1.add(99)
print(set1)
print(len(set1))

set1.remove(99)
print(set1)
print(len(set1))


#operations on set

set7 = {'aakarshan', 'atul', 'jassi'}
set8 = {'jassi', 'scotty', 'ricky'}
print(set7 | set8)
