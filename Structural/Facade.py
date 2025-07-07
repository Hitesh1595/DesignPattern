# Provide a simple interface to a complex functionality

# remove the need for a complex object/ memory management

# Simplified client implementation

# The Facade Pattern is a structural design pattern that provides a
# simplified interface to a complex subsystem. It hides the complexities
# of the system and provides a unified interface to the client.

#  Benefits:
# Reduces dependencies between client and subsystems.

# Improves readability and ease of use.

# You can refactor or swap subsystems without affecting the client.





from dataclasses import dataclass

class ComplexSystemStore:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.cache = {}

        print(f"Reading data from file : {filepath}")

    def store(self, key: str, value: str):
        self.cache[key] = value

    def read(self, key: str):
        return self.cache[key]

    def commit(self):
        print(f"Storing cached data to file {self.filepath}")


@dataclass
class User:
    login: str


#Facade
class UserRepository:
    def __init__(self):
        self.system_preferences = ComplexSystemStore("/data/default.prefs")

    def save(self, user: User):
        self.system_preferences.store("USER_KEY", user.login)
        self.system_preferences.commit()

    def find_first(self):
        return User(self.system_preferences.read("USER_KEY"))


if __name__ == "__main__":
    user_repo = UserRepository()
    user = User("john")

    user_repo.save(user)

    retrieved_user = user_repo.find_first()
    print(retrieved_user.login)
