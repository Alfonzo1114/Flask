from flask import Flask, render_template, request
from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired
import DatosGenerales
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Lalita Gupta et Rajesh Singh'

class Inicio(FlaskForm):
    fecha = wtforms.DateField(label= 'Fecha', validators = [DataRequired()])
    submit = wtforms.SubmitField(label= 'Submit')
     
@app.route('/manual', methods=['GET', 'POST']) #
def index():
    years = [x for x in range(1940, 1975)]
    return render_template('index2.html', years = years) 

@app.route('/DatosGenerales', methods=['GET', 'POST'])
def get_datos():
    if request.method == 'POST':
        date = request.form['date']
        return render_template('index2.html', edad = DatosGenerales.calcular_edad(date)) 
    return render_template('index2.html', edad = DatosGenerales.calcular_edad(date)) 
    # return render_template('DatosGenerales.html', edad = 'datos')



@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # process login here


if __name__ == '__main__':
    app.run(debug=True)