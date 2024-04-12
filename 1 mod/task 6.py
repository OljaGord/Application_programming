from flask import Flask
app = Flask(__name__)
import random

@app.route('/cats')
def cats():
    cats = ['Корниш-рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мейн-кун', 'манчкин']
    random_cat = random.choice(cats)
    return random_cat

if __name__ == '__main__':
    app.run(debug=True, port=4000)  # поменяли порт на 4000