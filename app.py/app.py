from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_edad', methods=['POST'])
def calcular_edad():
    año_actual = 2024  # Asumiendo que estamos en el año 2024
    año_nacimiento = int(request.form['año_nacimiento'])
    edad = año_actual - año_nacimiento
    return jsonify({'edad': edad})

if __name__ == '__main__':
    app.run(debug=True)