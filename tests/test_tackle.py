import os
from tackle import tackle


def test_all():
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    x = os.listdir()
    print(x)

    tackle(no_input=True)
