# ✅ Definition
# The Adapter Pattern is a structural design pattern that allows incompatible
# interfaces to work together by converting the interface of one class into another
# that the client expects.

# 🧠 Real-World Analogy
# 🪫 Think of a charging adapter:

# Your laptop has a USB-C port.

# You have a device with a Micro-USB cable.

# An adapter converts Micro-USB to USB-C so it can connect.


# | Component   | Role                                                                    |
# | ----------- | ----------------------------------------------------------------------- |
# | **Client**  | Expects a specific interface                                            |
# | **Adaptee** | Existing class with a different/incompatible interface                  |
# | **Adapter** | Wraps the Adaptee and converts its interface to what the Client expects |



# | Use Case                      | Description                                                              |
# | ----------------------------- | ------------------------------------------------------------------------ |
# | **Legacy system integration** | Wrap old classes to work with new code                                   |
# | **Third-party API**           | Wrap APIs so they fit your app’s expected interface                      |
# | **Database abstraction**      | Adapt different DB drivers (MySQL, Postgres, etc.) to a common interface |
# | **Testing/mocking**           | Replace real services with adapters for testing                          |
# | **GUI frameworks**            | Adapting between toolkit widgets (e.g., PyQt ↔ Tkinter)                  |



from dataclasses import dataclass


# 3rd party functionality (have to send data in definate format)
@dataclass
class DisplatDataTypes:
    index: float
    data: str


class DisplayData:
    def __init__(self, display_data: DisplatDataTypes):
        self.display_data = display_data

    def show_data(self):
        print(f"3rd party functionality: {self.display_data.index} - {self.display_data.data}")


# our side code


@dataclass
class DatabaseDataType:
    position: int
    amount: int


class StoreDatabaseData:
    def __init__(self, database_data: DatabaseDataType):
        self.database_data = database_data

    def store_data(self):
        print(f"Database Data store: {self.database_data.position} - {self.database_data.amount}")


class DisplayDataAdapter(StoreDatabaseData, DisplayData):
    def __init__(self, data):
        self.data = data

    def store_data(self):
        print("call out code but use 3rd party code")
        for item in self.data:
            ddt = DisplatDataTypes(float(item.position), str(item.amount))
            # chnage the data call from super class
            self.display_data = ddt
            self.show_data()





def generate_data():
    data = list()
    data.append(DatabaseDataType(2, 3))
    data.append(DatabaseDataType(4, 7))

    return data


if __name__ == "__main__":
    data = generate_data()

    adapter = DisplayDataAdapter(data)
    adapter.store_data()





#  Adapter Pattern in Python Standard Library
# Python’s standard library often uses adapter-like behavior.

# Example: open() adapts different file interfaces:

# with open("file.txt", "r") as f:
#     content = f.read()
# Under the hood, Python uses adapter classes for text vs binary I/O streams.



# | Feature              | Adapter Pattern                |
# | -------------------- | ------------------------------ |
# | Interface conversion | ✅                              |
# | Legacy integration   | ✅                              |
# | Wrapper class        | ✅                              |
# | Structural pattern   | ✅                              |
# | Real-world example   | API bridge, hardware connector |

