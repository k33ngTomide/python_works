print('Enter two Integers, and i will tell you '
      'the relationship they satisfy')

number1 = int(input ('Enter first integer: '))
number2 = int(input ('Enter second integer: '))

if number1 == number2:
    print(number1, 'is equal to ', number2)
else:
    print(number1, 'is not equal to ', number2)

if number1 < number2:
    print(number1, 'is less than ', number2)
else:
    print(number1, 'is greater than', number2)

if number1 <= number2:
    print(number1, 'is less than or equal to ', number2)
else:
    print(number1, 'is greater equal to ', number2)
