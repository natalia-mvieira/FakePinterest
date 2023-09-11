from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto, FotoCompartilhada
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        #if usuario and bcrypt.check_password_hash(usuario.senha.encode("utf-8"), form_login.senha.data):
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("homepage.html", form=form_login)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit(): #campos estão válidos/preenchidos
        #senha = bcrypt.generate_password_hash(form_criarconta.senha.data).decode("utf-8") #criptografa senha
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit() #cria usuario no banco de dados
        login_user(usuario, remember=True) #login automático
        return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('criarconta.html', form=form_criarconta)

@app.route('/perfil/<id_usuario>', methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        #se usuário dentro do próprio perfil
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)
            foto = Foto(imagem=nome_seguro, id_usuario=id_usuario)
            database.session.add(foto)
            database.session.commit()
            fotocompart = FotoCompartilhada(id_foto=foto.id, id_usuario=id_usuario)
            database.session.add(fotocompart)
            database.session.commit()
        return render_template("perfil.html", usuario=current_user, form=form_foto)
    else:
        #usuário vendo outro perfil
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form=None)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/feed")
@login_required
def feed(): #mostra todas as fotos postadas e compartilhadas
    fotos = FotoCompartilhada.query.order_by(FotoCompartilhada.id.desc()).all()
    return render_template("feed.html", fotos=fotos)

@app.route("/adicionar/<id_foto>")
@login_required
def adicionar(id_foto):
    ''' Adiciona foto de outro perfil no perfil do usuário logado'''
    fotocompart = FotoCompartilhada(id_foto=int(id_foto), id_usuario=current_user.id)
    database.session.add(fotocompart)
    database.session.commit()
    return redirect(url_for('perfil', id_usuario=current_user.id))

@app.route("/visualizar/feed/<id_foto_compart>")
@login_required
def visualizarfeed(id_foto_compart):
    ''' Permite visualizar uma foto do feed, podendo depois ver o perfil
    do usuário que a postou ou adicioná-la ao próprio perfil'''
    foto_compart_id = FotoCompartilhada.query.get(int(id_foto_compart))
    foto_compart = FotoCompartilhada.query.filter_by(id=foto_compart_id.id).first()
    foto = Foto.query.filter_by(id=int(foto_compart.id_foto)).first()
    return render_template("visualizarfotofeed.html", foto=foto, foto_compart=foto_compart)

@app.route("/visualizar/perfil/<id_foto_compart>")
@login_required
def visualizarperfil(id_foto_compart):
    ''' Permite visualizar uma foto do perfil de outro usuário, podendo depois
    ver o perfil do usuário que a postou ou adicioná-la ao próprio perfil'''
    foto_compart_id = FotoCompartilhada.query.get(int(id_foto_compart))
    foto_compart = FotoCompartilhada.query.filter_by(id=foto_compart_id.id).first()
    foto = Foto.query.filter_by(id=int(foto_compart.id_foto)).first()
    return render_template("visualizarfotoperfil.html", foto=foto)

@app.route("/deletar/<id_foto_compart>")
@login_required
def deletar(id_foto_compart):
    ''' Permite remoção de uma imagem do perfil.
    Se usuário é o 'dono' da imagem, ela é apagada do banco de dados
    geral, removendo-a também de outros perfis que a compartilharam.
    Se o usuário apenas compartilhou, é removida só do seu perfil.'''
    foto_compart_id = FotoCompartilhada.query.get(int(id_foto_compart))
    foto_compart = FotoCompartilhada.query.filter_by(id=foto_compart_id.id).first()
    foto = Foto.query.filter_by(id=int(foto_compart.id_foto)).first()
    if foto.id_usuario == current_user.id:
        FotoCompartilhada.query.filter_by(id_foto=foto.id).delete()
        Foto.query.filter_by(id=foto.id).delete()
        database.session.commit()
    elif foto.id_usuario != current_user.id:
        FotoCompartilhada.query.filter_by(id=int(foto_compart.id)).delete()
        database.session.commit()
    return redirect(url_for('perfil', id_usuario=current_user.id))

@app.route("/editar/<id_foto_compart>")
@login_required
def editar(id_foto_compart):
    ''' Ao clicar em uma imagem dentro de seu próprio perfil, o usuário terá
    a opção de ver o perfil do usuário de onde a imagem se originou ou deletá-la de seu perfil.'''
    foto_compart_id = FotoCompartilhada.query.get(int(id_foto_compart))
    foto_compart = FotoCompartilhada.query.filter_by(id=foto_compart_id.id).first()
    foto = Foto.query.filter_by(id=foto_compart.id_foto).first()
    return render_template("editar.html", foto_compart=foto_compart, foto=foto)