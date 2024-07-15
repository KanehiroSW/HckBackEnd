#from flask import Blueprint, request, jsonify, session
#from models import db
#from models.usuario import Usuario

#auth_bp = Blueprint('auth_bp', __name__)

#@auth_bp.route('/login', methods=['POST'])
#def login():
 #   data = request.json
  #  usuario = Usuario.query.filter_by(usuario=data['usuario']).first()
   # if usuario and usuario.check_password(data['password']):
    #     session['user_id'] = usuario.idUsuario
    #   return jsonify({'message': 'Login exitoso'}), 200
    #return jsonify({'message': 'Credenciales inválidas'}), 401