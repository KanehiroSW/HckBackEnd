from . import db

class Diagnostico(db.Model):
    __tablename__ = 'diagnostico'
    idDiagno = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('Usuario.idUsuario'))
    idDetalle = db.Column(db.Integer, db.ForeignKey('detalle_diagno.idDetalle'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}