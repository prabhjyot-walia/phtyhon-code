# Using a Module
import math_utils 
result = math_utils.add(5, 3) 
print(result)

# Importing Specific Functions 
from math_utils import add 
result = add(5, 3) 
print(result)

# Importing All Functions 
from math_utils import * 
result = subtract(10, 5) 
print(result)

# Aliasing Modules and Functions 
import math_utils as mu 
result = mu.add(5, 3) 
print(result)

print("THIS PROGRAM IS WRITTEN BY Divyam :- 0221BCA006")