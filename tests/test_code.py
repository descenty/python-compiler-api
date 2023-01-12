from contextlib import redirect_stdout
from tests.code import hello_world
import io


def test_hello_world():
    f = io.StringIO()
    with redirect_stdout(f):
        hello_world()
    output = f.getvalue()
    assert output == "Hello World!\n", f'Expected "Hello World!" but got {output}'
