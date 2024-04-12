from flask import Flask
app = Flask(__name__)

@app.route('/cars')
def cars():
    cars = ['Chevrolet', 'Renoult', 'Ford', 'Lada']
    return f"Машины: </br> Машина1 : {cars[0]}</br> Машина2 : {cars[1]} </br> Машина3 : {cars[2]} </br> Машина4 : {cars[3]}"

if __name__ == '__main__':
    app.run(debug=True, port=4000)  # поменяли порт на 4000