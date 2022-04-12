from tackle import BaseHook


class Greeter(BaseHook):
    hook_type: str = "python_greeter"
    target: str
    args: list = ["target"]

    def exec(self):
        print(f"Hello {self.target}")
