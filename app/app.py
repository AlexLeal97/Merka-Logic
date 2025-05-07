from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('inicio-de-sesion.html')

@app.route('/index.html')
def indexhtml():
    return render_template('index.html')

@app.route('/usuarios.html')
def usuarios():
    return render_template('usuarios.html')

@app.route('/facturacion.html')
def facturacion():
    return render_template('facturacion.html')





@app.route('/inventarios.html')
def inventarios():
    return render_template('inventarios.html',titulo='Ver productos')

@app.route('/buscarfactura')
def buscarfactura():
   return render_template('buscarfactura.html',titulo='Ver productos')

@app.route('/clientes.html')
def clientes():
   return render_template('clientes.html',titulo='Ver productos')

@app.route('/crearusuario')
def crear_usuario():
   return render_template('crearnuevousuario.html',titulo='Ver productos')

if __name__ == '__main__':
  app.run(debug=True)

