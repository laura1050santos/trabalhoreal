from DAO import *
from repository import UserRepository
from flask import request, Blueprint, render_template
user_repository = UserRepository()

userController = Blueprint("user", __name__)

@userController.route('/add_user',  methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        nome = request.form.get('register-nome')
        email = request.form.get('register-email')
        senha = request.form.get('register-senha')
        confirmar_senha = request.form.get('confirmar-senha')
        mensagem = user_repository.create_user(nome, email, senha,confirmar_senha)
        return render_template('/user/cadastro_user.html' , mensagem=mensagem)
    return render_template('/user/cadastro_user.html' )


@userController.route('/ver-todos', methods=['GET'])
def get_users():
    users = user_repository.get_all_users()
    return render_template('/user/cadastro_user.html', users=users)


@userController.route('/ver-user', methods=['GET', 'POST'])
def ver_user():
    if request.method == 'POST':
        id=request.form.get("id_usuario")
        user = user_repository.get_by_id_user(id)
        return render_template('/user/get_by_id_user.html', user=user)
    return render_template('/user/get_by_id_user.html')


@userController.route('/update_user/', methods=['POST', 'GET'])
def update_user():
    if request.method == 'POST':
        id_user = request.form.get('id_user')
        nome = request.form.get('name')
        email = request.form.get('email')
        senha = request.form.get('senha')
        updated_user = user_repository.update_user(id_user, nome, email, senha)
        if updated_user:
            return render_template('/user/get_all_user.html', mensagem='Atualizado com sucesso')
    return render_template('/user/update_user.html')


@userController.route('/delete_user', methods=['GET'])
def delete_user():
    if request.method == 'POST':
        id_user = request.get('id_user')
        deleted_user = user_repository.delete_user(id_user)
        if deleted_user:
            return render_template('/user/get_all_user.html')
    return render_template('/user/delete_user.html')

@userController.errorhandler(404) #erro de pagina não encontrada
def erro404(e):
    return render_template('404.html'), 404

@userController.errorhandler(401) #erro de pagina não autorizada
def erro404(e):
    return render_template('401.html'), 401

@userController.errorhandler(403) #acesso negado
def page_not_found(e):
    return render_template('403.html'), 403

@userController.errorhandler(500)  #erro interno no servidor
def page_not_found(e):
    return render_template('500.html'), 500
