import os
from flask import Flask

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size:int, relative_path:str):
    abs_path = os.path.join(BASE_DIR, relative_path)
    with open(abs_path,'r') as file:
        result_text = file.read(size)
        result_size = len(result_text)
    return f'<b>{abs_path}</b> {result_size}<br>{result_text}'

if __name__ == '__main__':
    app.run(debug=True)