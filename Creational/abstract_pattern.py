# 🧠 What Are Abstract Design Patterns?
# These are patterns that use abstract classes or interfaces/protocols to:
# Define contracts (what must be implemented)
# Allow interchangeable behaviors (polymorphism)
# Support dependency inversion and loose coupling

# Abstract Factory	| Creates families of related objects without
#                     specifying their concrete classes


from abc import ABC, abstractmethod

from typing import Protocol

# class Animal(Protocol):
#     def speak(self) -> None:
#         ...


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# | Use case                                      | Use                    |
# | --------------------------------------------- | ---------------------- |
# | You care about behavior (not class hierarchy) | ✅ Protocol             |
# | You want flexibility and looser contracts     | ✅ Protocol             |
# | You need strict class inheritance & control   | ✅ ABC + abstractmethod |



class Dog(Animal):
    def speak(self):
        print("bark")


class Cat(Animal):
    def speak(self):
        print("Meow")


from enum import Enum


class AnimalType(Enum):
    cat = "Cat"
    dog = "Dog"


class AnimalFactory:
    @staticmethod
    def create_animal(type1: AnimalType) -> Animal:
        print("type", type1)
        if type1 == AnimalType.cat:
            return Cat()
        else:
            return Dog()


c = AnimalFactory.create_animal(AnimalType.cat)
c.speak()
d = AnimalFactory.create_animal(AnimalType.dog)
d.speak()


# a classic example is restorurant
