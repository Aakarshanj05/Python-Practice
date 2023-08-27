
for number in range(0,10):
    if number%3==0 and number%2==0:
        print('FizzBuzz')
    elif number % 3==0:
        print('Fizz')
    elif number % 2==0:
        print('Buzz')
    else:
        print(number)
