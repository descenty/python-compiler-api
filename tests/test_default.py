from tests import code
import json


def test_function_exists():
    function_name = json.load(open('tests/config.json', 'r'))['function_name']
    assert hasattr(
        code, function_name), f'Function {function_name} does not exist'
    assert callable(getattr(code, function_name)
                    ), f"{function_name} is not a function"
