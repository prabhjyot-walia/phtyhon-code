#wap to demonstrate try, except and else
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except ZeroDivisionError:
    print('Error: Cannot divide by zero.')
except ValueError:
    print('Error: Invalid input. Please enter a valid number.')
else:
    print(f'The result is {result}')
    print("THIS PROGRAM IS WRITTEN BY Divyam :- 0221BCA006")