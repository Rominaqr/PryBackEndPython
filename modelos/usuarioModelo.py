from app import db, ma, app

# defino las tablas
class Usuario(db.Model):    
    id=db.Column(db.Integer, primary_key=True)  
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    email=db.Column(db.String(100))
    password=db.Column(db.String(200))
    
    def __init__(self, nombre, apellido, email, password):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellido=apellido
        self.email=email
        self.password=password

with app.app_context():
    db.create_all()  

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','nombre', 'apellido', 'email', 'password')


usuario_schema=UsuarioSchema()            
usuarios_schema=UsuarioSchema(many=True)  