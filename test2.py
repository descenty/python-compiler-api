from contextlib import redirect_stdout
from flask_main import hello_world
import io


def hello_world():
    print("Hello World!")


def test_hello_world():
    f = io.StringIO()
    with redirect_stdout(f):
        hello_world()
    output = f.getValue()
    assert output == "Hello World!", f'Expected "Hello World!" but got {output}'
