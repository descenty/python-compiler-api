import json
from subprocess import run, PIPE
import re

def run_tests(code: str, test_code: str, function_name: str):
    with open('tests/code.py', 'w') as f:
        f.write(code)
    with open('tests/test_code.py', 'w') as f:
      f.write(test_code)
    with open('tests/config.json', 'w') as f:
        json.dump({'function_name': function_name}, f)
    result = run(['pytest', 'tests'], stdout=PIPE, stderr=PIPE)
    match = re.search(r'AssertionError: (.+)\s', result.stdout.decode())
    return match.group(1) if match is not None else 'Все тесты пройдены'