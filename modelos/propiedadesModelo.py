from app import db, ma, app

# defino las tablas
class Propiedad(db.Model):    
    id=db.Column(db.Integer, primary_key=True)  
    tipo_propiedad=db.Column(db.String(100))
    ubicacion=db.Column(db.String(300))
    superficie=db.Column(db.Integer)
    ambiente=db.Column(db.Integer)
    banio=db.Column(db.Integer)
    dormitorio=db.Column(db.Integer)
    cochera=db.Column(db.Integer)
    antiguedad=db.Column(db.String(200))
    tipo_anunciante=db.Column(db.String(100))
    tipo_venta=db.Column(db.String(100))
    url_imagen=db.Column(db.String(400))
    moneda=db.Column(db.String(400))
    importe=db.Column(db.Integer)
    

    def __init__(self, tipo_propiedad, ubicacion, superficie, ambiente, banio, dormitorio, cochera, antiguedad, tipo_anunciante, tipo_venta, url_imagen, moneda, importe):   #crea el  constructor de la clase
        self.tipo_propiedad=tipo_propiedad   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.ubicacion=ubicacion
        self.superficie=superficie
        self.ambiente=ambiente
        self.banio=banio
        self.dormitorio=dormitorio
        self.cochera=cochera
        self.antiguedad=antiguedad
        self.tipo_anunciante=tipo_anunciante
        self.tipo_venta=tipo_venta
        self.url_imagen=url_imagen
        self.moneda=moneda
        self.importe=importe


with app.app_context():
    db.create_all()  
class PropiedadSchema(ma.Schema):
    class Meta:
        fields=('id','tipo_propiedad', 'ubicacion', 'superficie', 'ambiente', 'banio', 'dormitorio', 'cochera', 'antiguedad', 'tipo_anunciante', 'tipo_venta', 'url_imagen', 'moneda', 'importe')


propiedad_schema=PropiedadSchema()            
propiedades_schema=PropiedadSchema(many=True)  
