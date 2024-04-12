from flask import Flask
app = Flask(__name__)
import random
import os
import re

@app.route('/get_random_word')
def get_random_word():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
    with open(BOOK_FILE, "r", encoding="utf-8") as book:
        text = book.read()
        words = re.findall(r'\b\w+\b', text)
    return random.choice(words)

if __name__ == '__main__':
    app.run(debug=True, port=4000)  # поменяли порт на 4000