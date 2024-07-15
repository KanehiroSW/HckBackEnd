from . import db

class DetalleDiag(db.Model):
    __tablename__ = 'detalle_diagno'
    idDetalle = db.Column(db.Integer, primary_key=True)
    imagen = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    precision = db.Column(db.Float, nullable=False)
    tipo_enfermedad = db.Column(db.String(50), nullable=False)
    recomend=db.Column(db.Text, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}