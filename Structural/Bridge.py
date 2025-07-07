# ✅ Definition
# The Bridge Pattern is a structural design pattern that decouples an abstraction
# from its implementation, so the two can vary independently.

# 🧠 Real-World Analogy
# 🎮 Think of a game controller (abstraction) and a console (implementation).
# The controller has buttons (interface),
# But it can control Xbox, PlayStation, or PC (different implementations),
# Without changing the controller interface.



# The Bridge pattern allows you to plug new implementations (like new consoles) without changing the abstraction.
# 🔄 Why Use Bridge Pattern?
# Avoid class explosion due to multiple combinations of abstraction + implementation.

# Promote composition over inheritance.

# Makes both sides extensible independently.


# IMPORTANT:

# convert form inheritance to composition
# split into multiple interfaces/ classes

# Associate them using a "bridge" refrence

from abc import ABC, abstractmethod


class Device(ABC):
    volume = 0

    @abstractmethod
    def get_name(self) -> str:
        pass


class Radio(Device):
    def get_name(self) -> str:
        return f"Radio {self}"


class TV(Device):
    def get_name(self) -> str:
        return f"TV {self}"


class Remote(ABC):
    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass


class BasicRemote(Remote):
    def __init__(self, device: Device):
        self.device = device

    def volume_up(self):
        self.device.volume += 1
        print(f"{self.device.get_name()} Volume Up:{self.device.volume}")

    def volume_down(self):
        self.device.volume -= 1
        print(f"{self.device.get_name()} Volume Down:{self.device.volume}")


if __name__ == "__main__":
    radio = Radio()
    tv = TV()

    radio_remote = BasicRemote(radio)
    tv_remote = BasicRemote(tv)

    radio_remote.volume_up()
    radio_remote.volume_up()
    radio_remote.volume_down()

    tv_remote.volume_up()
    tv_remote.volume_up()
    tv_remote.volume_down()
