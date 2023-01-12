from flask import Flask, request
from subprocess import run, PIPE
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/execute/', methods=['POST'])
def execute():
    test_code = request.json.get('test_code')
    function_name = request.json.get('function_name')
    code = request.json.get('code')
    try:
        result = run(['python', '-c', code], stdout=PIPE, stderr=PIPE)
        return result.stderr + result.stdout
    except Exception:
        return Exception


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
