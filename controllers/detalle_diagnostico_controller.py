from flask import Blueprint, request,jsonify
from models import db
from models.detalle_diagnostico import DetalleDiag

detalle_diag_bp=Blueprint('detalle_diag_bp',__name__)

@detalle_diag_bp.route('/detalle_diag',methods=['GET'])
def get_detalle_diag():
    detalles= DetalleDiag.query.all()
    return jsonify([detalle.as_dict()for detalle in detalles])

@detalle_diag_bp.route('/detalle_diag/<int:id>',methods=['GET'])
def get_detalle_diag_by_id(id):
    detalle=DetalleDiag.query.get_or_404(id)
    return jsonify(detalle.as_dict())
@detalle_diag_bp.route('/detalle_diag',methods=['POST'])
def add_detalle_diag():
    data=request.json
    nuevo_detalle=DetalleDiag(
        imagen=data['imagen'],
        descripcion=data['descripcion'],
        precision=data['precision'],
        tipo_enfermedad=data['tipo_enfermdad'],
        recomend=data['recomend']
    )
    db.session.add(nuevo_detalle)
    db.session.commit()
    return jsonify({'message': 'Detalle diagnostico añadido correctamente'}),201