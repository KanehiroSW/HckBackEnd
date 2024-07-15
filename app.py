from flask import Flask
from config import Config
from models import db
from controllers.usuario_controller import usuario_bp
from controllers.detalle_diagnostico_controller import detalle_diag_bp
from controllers.diagnostico_controller import diagnostico_bp
#from controllers.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(usuario_bp)
app.register_blueprint(detalle_diag_bp)
app.register_blueprint(diagnostico_bp)
#app.register_blueprint(auth_bp)

@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)