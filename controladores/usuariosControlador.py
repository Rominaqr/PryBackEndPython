from app import *
from flask import jsonify ,request

from modelos.usuarioModelo import *

# crea los endpoint o rutas (json)
@app.route('/usuarios',methods=['GET'])
def get_usuarios():
    all_usuarios=Usuario.query.all()         # el metodo query.all() lo hereda de db.Model
    result=usuarios_schema.dump(all_usuarios)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla


@app.route('/usuario/<email>',methods=['GET'])
def get_emailUsuario(email):
    usuario=Usuario.query.filter_by(email=email).first()
    return usuario_schema.jsonify(usuario)   


@app.route('/usuario/<id>',methods=['GET'])
def get_usuario(id):
    usuario=Usuario.query.get(id)
    return usuario_schema.jsonify(usuario)      


@app.route('/usuario/<id>',methods=['DELETE'])
def delete_usuario(id):
    usuario=Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()                     
    return usuario_schema.jsonify(usuario) # me devuelve un json con el registro eliminado

@app.route('/usuario', methods=['POST']) # crea ruta o endpoint
def create_usuario():
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    email=request.json['email']
    password=request.json['password']
    
    new_usuario=Usuario(nombre, apellido, email, password)
    db.session.add(new_usuario)
    db.session.commit() # confirma el alta
    return usuario_schema.jsonify(new_usuario)


@app.route('/usuario/<id>' ,methods=['PUT'])
def update_usuario(id):
    usuario=Usuario.query.get(id)
 
    usuario.tipo_propiedad=request.json['nombre']
    usuario.ubicacion=request.json['apellido']
    usuario.superficie=request.json['email']
    usuario.ambiente=request.json['password']
    
    db.session.commit()    # confirma el cambio
    return usuario_schema.jsonify(usuario) 