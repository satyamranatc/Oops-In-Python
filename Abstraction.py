from abc import ABC,abstractmethod
class Animal(ABC):
    __Eyes = 2
    __Legs = 4

    def __init__(self, name=None):
        print("Hi By Animal", name)
        print("Eyes: ", Animal.__Eyes)
        print("Legs: ", Animal.__Legs)

    @abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    def __init__(self):
        super().__init__()  # Call the superclass's __init__ method
        print("Hi By Dog")

    def bark(self):
        print("Barking")

    def eat(self):
        print("Dog Eating")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)  # Call the superclass's __init__ method with 'name'
        print("Hi By Cat")

    def meow(self):
        print("Meowing")

    def eat(self):
        print("Cat Eating")


D1 = Dog()
D1.eat()
D1.bark()

print("--------------------------------")

C1 = Cat("Cat")
C1.eat()
C1.meow()
