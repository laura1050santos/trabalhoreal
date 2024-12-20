from flask import Blueprint, render_template, request, redirect, url_for, session, flash, abort, make_response
from database import init_app, db
from DAO.user import *
from repository.userRepository import UserRepository

userrepository= UserRepository()

loginController = Blueprint('login', __name__)

@loginController.route("/")
def inicial():
    return render_template("login.html")

@loginController.route("/cadastro_user", methods=['GET', 'POST'])
def cadastrar():
        if request.method == 'POST':
            nome = request.form.get('register-nome')
            email = request.form.get('register-email')
            senha = request.form.get('register-senha')
            confirmar_senha = request.form.get('confirmar-senha')
            mensagem = UserRepository.create_user(nome, email, senha,confirmar_senha)
            return render_template('/user/cadastro_user.html' , mensagem=mensagem)

@loginController.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') #usa o 'name' do input pra pegar a informação do formulario
        senha = request.form.get('senha')
        usuario= userrepository.get_user_by_email(email)
        if email== usuario.email and senha == usuario.senha:
            session['id_user']= usuario.id
            session['nome']=usuario.nome
            return redirect(url_for("login.cookie", usuario=usuario))
        else:
            flash("tente novamente", 'info')   
    return render_template("login.html")

rotas_publicas = ["login.login", "login.index","campeao.ver_campeoes","campeao.ver_id",]
rotas_usuario=["login.index","campeao.ver_campeoes","campeao.ver_id","campeao.update_campeao","campeao.add_campeao"]

@loginController.before_request #middleware (hooks)
def verificaLogin():
    if request.endpoint =='login.login' and 'iduser' in session:
        return redirect(url_for('login.index'))
    if request.endpoint in rotas_publicas:
        return 
    if "iduser" not in session: #verifica se o user ta na sessão
        return redirect(url_for('login.login'))
    if session['nome'] !='admin' and request.endpoint not in rotas_publicas and request.endpoint not in rotas_usuario:
        return 

@loginController.route('/dashboard')
def dashboard():
        return render_template('dash.html')  

@loginController.route('/logout')
def logout():
    response=make_response(redirect(url_for("login.login")))
    session.pop("iduser", None) 
    response.set_cookie('nome', '', expires=0)
    response.set_cookie('senha', '', expires=0)
    return response

@loginController.route("/admin")
def admin():
    if session.get("iduser") != 1:
        abort(401)
    return render_template('admin.html')

#@loginController.route("/cookie")   
#def cookies():
       # email = session['id_user']
        #senha = session['nome']
        #responde.set_cookie('email', 'Correto', max_age=60 * 60 *24)
        #response.set_cookie('senha', 'Correto', max_age=60 * 60 *24)
        #return redirect(url_for())