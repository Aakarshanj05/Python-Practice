import random
letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
           'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J'',K','L','Z','X','C','V','B','N','M'
           ]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','/']
print("Welcome to password generator")
n_letters=int(input("How many letters you want in your password: "))
n_numbers=int(input("How many numbers you want in your password: "))
n_symbols=int(input("How many symbols you want in your password: "))
password = []
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password += char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password += char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password += char
print(password)
random.shuffle(password)
print(password)

Stong_password = ""
for char in password:
    Stong_password += char
print(Stong_password)

