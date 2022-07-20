import os
import pytest


@pytest.fixture()
def base_dir():
    """Change dir to the base of the repo."""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")


@pytest.fixture()
def change_base_dir(base_dir):
    """Change dir to the base of the repo."""
    os.chdir(base_dir)
