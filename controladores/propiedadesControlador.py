from app import *
from flask import jsonify ,request

from modelos.propiedadesModelo import *

# crea los endpoint o rutas (json)
@app.route('/propiedades',methods=['GET'])
def get_propiedades():
    all_propiedades=Propiedad.query.all()         # el metodo query.all() lo hereda de db.Model
    result=propiedades_schema.dump(all_propiedades)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla


@app.route('/propiedades/<id>',methods=['GET'])
def get_propiedad(id):
    propiedad=Propiedad.query.get(id)
    return propiedad_schema.jsonify(propiedad)   


@app.route('/propiedades/<id>',methods=['DELETE'])
def delete_propiedad(id):
    propiedad=Propiedad.query.get(id)
    db.session.delete(propiedad)
    db.session.commit()                     # confirma el delete
    return propiedad_schema.jsonify(propiedad) # me devuelve un json con el registro eliminado


@app.route('/propiedades', methods=['POST']) # crea ruta o endpoint
def create_propiedad():
    tipo_propiedad=request.json['tipo_propiedad']
    ubicacion=request.json['ubicacion']
    superficie=request.json['superficie']
    ambiente=request.json['ambiente']
    banio=request.json['banio']
    dormitorio=request.json['dormitorio']
    cochera=request.json['cochera']
    antiguedad=request.json['antiguedad']
    tipo_anunciante=request.json['tipo_anunciante']
    tipo_venta=request.json['tipo_venta']
    url_imagen=request.json['url_imagen']
    moneda=request.json['moneda']
    importe=request.json['importe']
    new_propiedad=Propiedad(tipo_propiedad, ubicacion, superficie, ambiente, banio, dormitorio, cochera, antiguedad, tipo_anunciante, tipo_venta, url_imagen, moneda, importe)
    db.session.add(new_propiedad)
    db.session.commit() # confirma el alta
    return propiedad_schema.jsonify(new_propiedad)

@app.route('/propiedades/<id>' ,methods=['PUT'])
def update_producto(id):
    propiedad=Propiedad.query.get(id)
 
    propiedad.tipo_propiedad=request.json['tipo_propiedad']
    propiedad.ubicacion=request.json['ubicacion']
    propiedad.superficie=request.json['superficie']
    propiedad.ambiente=request.json['ambiente']
    propiedad.banio=request.json['banio']
    propiedad.dormitorio=request.json['dormitorio']
    propiedad.cochera=request.json['cochera']
    propiedad.antiguedad=request.json['antiguedad']
    propiedad.tipo_anunciante=request.json['tipo_anunciante']
    propiedad.tipo_venta=request.json['tipo_venta']
    propiedad.url_imagen=request.json['url_imagen']
    propiedad.moneda=request.json['moneda']
    propiedad.importe=request.json['importe']

    db.session.commit()    # confirma el cambio
    return propiedad_schema.jsonify(propiedad) 