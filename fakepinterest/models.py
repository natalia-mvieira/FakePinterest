from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

#o UserMixin diz qual a classe vai gerenciar a estrutura de login

@login_manager.user_loader
def load_usuario(id_usuario): #recebe um id e retorna quem é o usuario
    return Usuario.query.get(int(id_usuario))

#crio duas tabelas no banco de dados: Usuario e Fotos
class Usuario(database.Model, UserMixin): #classe que o banco de dados vai entender, por isso o database.Model
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True) #relaciona com a classe Foto
    fotos_compartilhadas = database.relationship("FotoCompartilhada", backref="usuario_comp", lazy=True)
    #o backref permite o caminho contrário, achar usuário a partir de uma foto
    #lazy melhora a eficiência

class Foto(database.Model): #fotos de todos os usuários juntos
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png") #é texto, pois armazeno o local da imagem no banco de dados
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow()) #horario padrão
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

class FotoCompartilhada(database.Model):
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_foto = database.Column(database.Integer, database.ForeignKey('foto.id'), nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) #usuário que compartilhou ou adicionou
    fotos = database.relationship("Foto", backref="foto", lazy=True)