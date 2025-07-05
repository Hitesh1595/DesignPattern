
class NetworkService:
    def __init__(
        self,
        method: str = "GET",
        url: str = None,
        headers: str = None,
        timeout: int = 5,
        body: dict = None,
    ):
        self.components = {}

        if method:
            self.components["method"] = method
        if url:
            self.components["url"] = url
        if headers:
            self.components["headers"] = headers
        if timeout:
            self.components["timeout"] = timeout
        if body:
            self.components["body"] = body

    def show(self):
        print(self.components)

n = NetworkService(url="google.com")
n.show()

