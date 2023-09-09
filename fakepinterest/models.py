from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)
    fotos_compartilhadas = database.relationship("FotoCompartilhada", backref="usuario_comp", lazy=True)

class Foto(database.Model): #fotos de todos os usuários juntos
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

class FotoCompartilhada(database.Model):
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_foto = database.Column(database.Integer, database.ForeignKey('foto.id'), nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) #usuário que compartilhou ou adicionou imagem
    fotos = database.relationship("Foto", backref="foto", lazy=True)