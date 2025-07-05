from abc import ABC, abstractmethod

# ✅ Definition:
# The Prototype Pattern is a creational design pattern that lets you clone
# existing objects instead of creating them from scratch using constructors.

# It's useful when:
# Object creation is expensive or complex
# You want to avoid rebuilding similar objects multiple times

# | Concept          | Meaning                                       |
# | ---------------- | --------------------------------------------- |
# | **Prototype**    | The original object used as a template        |
# | **Clone**        | A duplicate object created from the prototype |
# | **Shallow copy** | Copies only top-level attributes              |
# | **Deep copy**    | Recursively copies nested objects too         |



# 🧠 Real-World Analogy
# 🧬 Think of cell division:

# You don’t “create” a new cell from scratch.

# Instead, an existing one replicates (clones) itself.

# 🎨 Or a graphic design tool like Figma or Photoshop:

# You create one button, style it, and then duplicate it across the UI.


class shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Sqaure(shape):
    def __init__(self, size: int):
        self.size = size

    def draw(self):
        print(f"Draw square of size {self.size}")


class Circle(shape):
    def __init__(self, radius: int):
        self.radius = radius

    def draw(self):
        print(f"Draw Circle of size {self.radius}")


class AbstractArt:
    def __init__(self, bg_colour: str, shapes: list):
        self.bg_colour = bg_colour
        self.shapes = shapes

    def draw(self):
        print(f"Backgroud color og {self.bg_colour}")
        [x.draw() for x in self.shapes]

import copy

# Shallow copy will share the inner list reference, while deep copy will duplicate it.

if __name__ == "__main__":
    shapes = [Sqaure(4), Circle(2)]
    art1 = AbstractArt("red", shapes)


    art2 = copy.copy(art1)   # --> only ref  deepcopy whole with refrence
    art2.draw()
    art1.draw()


