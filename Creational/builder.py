# 🏗️ Builder Design Pattern – Explained
# The Builder Pattern is a creational design pattern that helps you construct
# complex objects step-by-step. It allows you to build different representations
# of an object using the same construction process.

# | Term                | Description                                                     |
# | ------------------- | --------------------------------------------------------------- |
# | Builder             | A class that **defines how to build parts** of a complex object |
# | Director (optional) | Controls the **building sequence**                              |
# | Product             | The **complex object** being built                              |
# | Fluent API          | Often used for chaining steps (`.setA().setB().build()`)        |



#  Real World Analogy:
# Imagine building a network request:

# Set method: GET or POST

# Set headers

# Set authentication

# Set timeout

# Set body

# Instead of passing all of that to one big constructor, Builder lets you do it step by step.

class NetworkService:
    def __init__(self, method, url, headers=None, timeout=5, body=None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.timeout = timeout
        self.body = body

    def send(self):
        print(f"Sending {self.method} request to {self.url}")
        print(f"Headers: {self.headers}")
        print(f"Timeout: {self.timeout}")
        print(f"Body: {self.body}")


class NetworkServiceBuilder:
    def __init__(self):
        self._method = "GET"
        self._url = ""
        self._headers = {}
        self._timeout = 5
        self._body = None

    def set_method(self, method):
        self._method = method
        return self

    def set_url(self, url):
        self._url = url
        return self

    def add_header(self, key, value):
        self._headers[key] = value
        return self

    def set_timeout(self, timeout):
        self._timeout = timeout
        return self

    def set_body(self, body):
        self._body = body
        return self

    def build(self):
        return NetworkService(
            method=self._method,
            url=self._url,
            headers=self._headers,
            timeout=self._timeout,
            body=self._body
        )


builder = NetworkServiceBuilder()

service = (
    builder
    .set_method("POST")
    .set_url("https://api.example.com/data")
    .add_header("Authorization", "Bearer token")
    .set_timeout(10)
    .set_body({"name": "Hitesh"})
    .build()
)

service.send()