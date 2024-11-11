from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "snake!"
class Cat(Animal):
    def speak(self):
        return "kalesh!"
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
print("THIS PROGRAM IS WRITTEN BY Divyam :- 0221BCA006")
