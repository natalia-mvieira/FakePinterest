from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

    def validate_email(self, email): #a função tem que ter esse nome
        usuario = Usuario.query.filter_by(email=email.data).first() #email é o campo email.data é a informação dentro do campo
        if not usuario:
            raise ValidationError("Usuário inexistente, crie uma conta.")

    def validate_senha(self, senha): #a função tem que ter esse nome
        senha = Usuario.query.filter_by(senha=senha.data).first() #email é o campo email.data é a informação dentro do campo
        if not senha:
            raise ValidationError("Senha incorreta.")

class FormCriarConta(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    username = StringField("Nome de Usuário:", validators=[DataRequired()])
    senha = PasswordField("Senha:", validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField("Confirmação de Senha:", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email): #a função tem que ter esse nome
        usuario = Usuario.query.filter_by(email=email.data).first() #email é o campo email.data é a informação dentro do campo
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar.")

class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")

#FlaskForm: parte estrutural da classe
#wtforms: campos de preenchimento (StringField = campo de texto; PasswordField: campo de senha; SubmitField: campo de submissão)