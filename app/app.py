from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

engine = create_engine("mysql+pymysql://root@localhost/merkalogic?charset=utf8mb4")

connection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
Base.metadata.bind = engine




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
    return render_template('inventarios.html', titulo='Ver productos')

@app.route('/clientes.html')
def clientes():
    return render_template('clientes.html', titulo='Ver productos')

@app.route('/crearnuevousuario.html')
def crear_usuario():
    return render_template('crearnuevousuario.html', titulo='Ver productos')


@app.route('/modificarusuario.html')
def modificarusuario():
    return render_template('modificarusuario.html', titulo='Ver productos')

@app.route('/buscarfactura.html')
def buscarfactura():
    return render_template('buscarfactura.html', titulo='Ver productos')

@app.route('/editarcliente.html')
def editarcliente():
    return render_template('editarcliente.html', titulo='Ver productos')





@app.route('/inventarios')
def lista_productos():
    return render_template('inventarios.html',titulo='Ver productos')


@app.route('/formulario_producto.html', methods=['GET','POST'])
def formulario_producto():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        descripcion = request.form.get('descripcion')
        valor_unitario = request.form.get('valor_unitario')
        cantidad_inventario = request.form.get('cantidad_inventario')        
        unidad_medida = request.form.get('unidad_medida')
        categoria = request.form.get('categoria')
        producto = Productos(codigo,descripcion,valor_unitario,unidad_medida,cantidad_inventario,categoria)
        Productos.crear_producto(producto)
        print ("Entró por POST")
        print(codigo)    
    return render_template('formulario_producto.html',titulo='Crear un producto')



class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    codigo = Column(String(9), unique=True, nullable=False)
    descripcion = Column(String(300), unique=True, nullable=False)
    valor_unitario = Column(Float(10,8))
    unidad_medida = Column(String(3), nullable=False)
    cantidad_stock = Column(Float(10,8))
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self,codigo,descripcion,valor_unitario,unidad_medida,cantidad_stock,categoria):
        self.codigo = codigo
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantidad_stock = cantidad_stock
        self.categoria = categoria

    def crear_producto(producto):
        producto = session.add(producto)
        session.commit()
        return producto




class Categorias(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(300), unique=True, nullable=False)



Base.metadata.create_all(engine)