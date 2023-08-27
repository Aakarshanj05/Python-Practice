height=int(input("Enter the height: "))

if height>=3:
    print("You can ride")
    age=int(input("What is your age? "))
    if age<=18:
        print("Pay 250")
    else:
        print("Pay 500")
else:
    print("Can't ride")