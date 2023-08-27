import random
a = random.randint(1,3)
print(a)

b=random.randrange(1,3)
print(b)

c=random.random()
print(c)

d=random.uniform(1,3)
print(d)

l=[1,2,3,4,5,6,7]
e=random.choice(l)
print(e)

l.reverse()
print(l)

print(len(l))

print(l[1:6])

print(max(l))

print(min(l))

l.extend([8,9,10])

print(l)

l.sort()

print(l)

l.remove(1)
print(l)