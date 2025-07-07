# Attach new/Existing behaviour to an object

# without altering existing code

# overriding behaviour

# The Decorator Pattern is a structural design pattern that allows
# you to dynamically add behavior or responsibilities to an object
# without modifying its structure. It’s useful for adhering to the Open/Closed Principle
# (open for extension, closed for modification).

from abc import ABC, abstractmethod


class CoffeMachine(ABC):
    @abstractmethod
    def make_small_coffee(self):
        pass

    @abstractmethod
    def make_large_cofee(self):
        pass


class BasicCoffeeMachine(CoffeMachine):
    def make_small_coffee(self):
        return print("Basic cofee machine making Small Coffee")

    def make_large_cofee(self):
        print("Basic coffee machine making Large Coffee")


class EnhancedCofeeMachine(CoffeMachine):
    def __init__(self, basic_machine: BasicCoffeeMachine):
        self.basic_machine = basic_machine

    def make_small_coffee(self):
        self.basic_machine.make_small_coffee()

    def make_large_cofee(self):
        print("Enhansed coffee machine: Making large coffee")

    def make_milk_coffee(self):
        print("Enhanced coffie machine: making milk coffee")
        self.basic_machine.make_small_coffee()
        print("Enhanced coffee machine : adding milk")


if __name__ == "__main__":
    basic_machine = BasicCoffeeMachine()
    enhanced_machine = EnhancedCofeeMachine(basic_machine)

    enhanced_machine.make_small_coffee()
    print()
    enhanced_machine.make_large_cofee()
    print()
    enhanced_machine.make_milk_coffee()


