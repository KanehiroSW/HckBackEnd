from flask import Blueprint, request,jsonify
from models import db
from models.usuario import Usuario

usuario_bp=Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuario', methods=['GET'])
def get_usuarios():
    usuarios=Usuario.query.all()
    return jsonify([usuario.as_dict() for usuario in usuarios])
@usuario_bp.route('/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario=Usuario.query.get_or_404(id)
    return jsonify(usuario.as_dict())

@usuario_bp.route('/usuario',methods=['POST'])
def add_usuario():
    data=request.json
    nuevo_usuario=Usuario(
        dni=data['dni'],
        nombre=data['nombre'],
        apell=data['apell'],
        telefono=data['telefono'],
        edad=data['edad'],
        direccion=data['direccion'],
        usuario=data['usuario'],
        email=data['email'],
        password=data['password'],
        sexo=data.get('sexo'),
        fecha_nac=data.get('fecha_nac'),
        peso=data.get('peso'),
        altura=data.get('altura'),
        rol=data['rol']
    )
    #nuevo_usuario.set_password(data['pass'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'message':'Usuario añadido correctamente'}),201