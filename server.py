from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',titulo='Flask',mensaje='bienvenido a la wedside')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Bienvenido a la página de servicios de UDl-ICO')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/productos')
def productos():
    return render_template('productos.html', titulo='Productos')

if __name__ == '__main__':
    app.run(debug=True,port=5050)   