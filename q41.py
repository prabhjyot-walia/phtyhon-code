#Iterator
a = 'Tanisha Vyas'

print('Custom Iterator:')
result = ' '.join(char for char in a)
print(result)

print('\nCustom Iterator with yield:')
def char_gen(s):
    for char in s:
        yield char
for char in char_gen(a):
    print(char, end=' ')

print('\n\nBuilt-in Iterator:')
for char in iter(a):
    print(char, end=' ')
    
print("THIS PROGRAM IS WRITTEN BY Divyam :- 0221BCA006")