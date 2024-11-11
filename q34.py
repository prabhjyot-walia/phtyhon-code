#wap to demonstrate try and except (exceptance handling)
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except ZeroDivisionError:
    print('Error: Cannot divide by zero.')
except ValueError:
    print('Error: Invalid input. Please enter a valid number.')
print("THIS PROGRAM IS WRITTEN BY Divyam :- 0221BCA006")