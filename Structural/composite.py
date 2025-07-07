# Compose objects into tree structures

# Works when the core functionality can be represented as a Tree

# Manuplate many objects as a single one


# ✅ Definition
# The Composite Pattern allows you to compose objects into tree-like
# structures and treat individual objects and compositions uniformly.


class Equipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Composite:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add(self, equipment: Equipment):
        self.items.append(equipment)
        return self

    @property
    def price(self):
        return sum([item.price for item in self.items])

    # @price.setter
    # def price(self, value):
    #     self.price = value


if __name__ == '__main__':
    computer = Composite("PC")

    processor = Equipment("Processor", 1000)
    hard_drive = Equipment("Processor", 500)

    memory = Composite("Memory")
    rom = Equipment("Read only Memory", 100)
    ram = Equipment("Random Acess Memory", 200)


    mem = memory.add(rom).add(ram)
    pc = computer.add(processor).add(hard_drive).add(mem)

    print(pc.price)
