from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hola():
    return "Hola mundo"

@app.route("/chau")
def goodbye():
    return "Chau"

@app.route('/saludo/<emilio>')
def saludar(emilio):
    return f'Hola {emilio}'

@app.route('/saludo/<nombre>/<apellido>')
def saludar_nombre_apellido(nombre, apellido):
    return f'Hola {nombre} {apellido}'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)

