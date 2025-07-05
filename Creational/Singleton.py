# Why Use Singleton?
# Prevents multiple instantiations of objects (e.g., for configurations, database connections).

# Shared state across the application.

# Useful when you want to coordinate actions across the system using a single shared resource.


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance...")
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True

# -------------------------------------------------------------------------------

import threading


class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance


obj1 = ThreadSafeSingleton()
obj2 = ThreadSafeSingleton()

print(obj1 is obj2)


# Is Django a Singleton?
# Yes, in some contexts:

# Settings configuration in Django is singleton-like.

# The WSGI application object is created once and reused.

# The database connection pool is shared.

# Example: When Django starts, it loads settings and initializes once. All views, middleware, etc., refer to this global state.

# But: Django uses class-based and functional patterns, not strictly Singleton everywhere.





#  Real-Life Handling in Web Frameworks (Multi-threaded or ASGI):
# 🧵 Threads:
# Each request may be handled by a new thread or async task.

# If Singleton is used unsafely, race conditions can occur.

# ✅ Solution:
# Use thread-safe singletons or initialize objects before server starts (e.g., in startup event in FastAPI).

# FastAPI supports lifespan events for global initialization:


class Student:
    def __init__(self):
        pass


s1 = Student()
s2 = Student()

print('student', s1 is s2)
