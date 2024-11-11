def count_characters(s):
    vowels = "aeiouAEIOU"
    v = c = b = 0
    for char in s:
        if char in vowels:
            v += 1
        elif char.isalpha():
            c += 1
        elif char == ' ':
            b += 1
    return v, c, b
v, c, b = count_characters(s)
print("Vowels:", v, "Consonants:", c, "Blanks:", b)

print("THIS PROGRAM IS WRITTEN BY Divyam :- 0221BCA006")