from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto, FotoCompartilhada
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename
from datetime import datetime


#url_for usado dentro dos arquivos html
@app.route('/', methods=['GET', 'POST']) #esses @ são atributos da função
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data): #True se senha verdadeira
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("homepage.html", form=form_login)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit(): #se usuario clicou no botão de criar conta e se todos os campos estão válidos/preenchidos
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data) #criptografa senha
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit() #cria usuario no banco de dados
        login_user(usuario, remember=True) #faz o login automático depois do preenchimento dos dados, o remember é para o login ficar gravado se o usuario fechar a janela
        return redirect(url_for('perfil', id_usuario=usuario.id)) #a função perfil precisa da informação de usuario
    return render_template('criarconta.html', form=form_criarconta)

@app.route('/perfil/<id_usuario>', methods=["GET", "POST"]) #a tag <> indica que dentro há uma variável, a página muda com o usuário
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        #usuário dentro do próprio perfil
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], nome_seguro)
            #__file__ é o arquivo routes.py
            arquivo.save(caminho)
            foto = Foto(imagem=nome_seguro, id_usuario=id_usuario)
            database.session.add(foto)
            database.session.commit()
            fotocompart = FotoCompartilhada(id_foto=foto.id, id_usuario=id_usuario)
            database.session.add(fotocompart)
            database.session.commit()
        return render_template("perfil.html", usuario=current_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form=None) #em vermelho é a variável que está no html
#tem dois atributos: é carregada dentro do link "/" e só pode ser acessada por usuário logado

@app.route("/logout")
@login_required
def logout():
    logout_user() #ele sabe que o logout é do usuário atual
    return redirect(url_for("homepage"))

@app.route("/feed")
@login_required
def feed():
    fotos = FotoCompartilhada.query.order_by(FotoCompartilhada.id.desc()).all() #me passa todas as fotos do banco de dados, das mais novas para as mais antigas (.desc())
    return render_template("feed.html", fotos=fotos)

@app.route("/adicionar/<id_foto>")
@login_required
def adicionar(id_foto):
    fotocompart = FotoCompartilhada(id_foto=int(id_foto), id_usuario=current_user.id)
    database.session.add(fotocompart)
    database.session.commit()
    return redirect(url_for('perfil', id_usuario=current_user.id))

@app.route("/visualizar/feed/<id_foto_compart>")
@login_required
def visualizarfeed(id_foto_compart):
    foto_compart_id = FotoCompartilhada.query.get(int(id_foto_compart))
    foto_compart = FotoCompartilhada.query.filter_by(id=foto_compart_id.id).first()
    foto = Foto.query.filter_by(id=int(foto_compart.id_foto)).first()
    return render_template("visualizarfotofeed.html", foto=foto, foto_compart=foto_compart)

@app.route("/visualizar/perfil/<id_foto_compart>")
@login_required
def visualizarperfil(id_foto_compart):
    foto_compart_id = FotoCompartilhada.query.get(int(id_foto_compart))
    foto_compart = FotoCompartilhada.query.filter_by(id=foto_compart_id.id).first()
    foto = Foto.query.filter_by(id=int(foto_compart.id_foto)).first()
    return render_template("visualizarfotoperfil.html", foto=foto)

@app.route("/deletar/<id_foto_compart>")
@login_required
def deletar(id_foto_compart):
    foto_compart_id = FotoCompartilhada.query.get(int(id_foto_compart))
    foto_compart = FotoCompartilhada.query.filter_by(id=foto_compart_id.id).first()
    foto = Foto.query.filter_by(id=int(foto_compart.id_foto)).first()
    if foto.id_usuario == current_user.id: #o dono da foto apaga do banco de dados Fotos
        Foto.query.filter_by(id=foto.id).delete()
        FotoCompartilhada.query.filter_by(id_foto=foto.id).delete()
        database.session.commit()
    elif foto.id_usuario != current_user.id:
        FotoCompartilhada.query.filter_by(id=int(foto_compart.id)).delete()
        database.session.commit()
    return redirect(url_for('perfil', id_usuario=current_user.id))

@app.route("/editar/<id_foto_compart>")
@login_required
def editar(id_foto_compart):
    foto_compart_id = FotoCompartilhada.query.get(int(id_foto_compart))
    foto_compart = FotoCompartilhada.query.filter_by(id=foto_compart_id.id).first()
    foto = Foto.query.filter_by(id=foto_compart.id_foto).first()
    return render_template("editar.html", foto_compart=foto_compart, foto=foto)