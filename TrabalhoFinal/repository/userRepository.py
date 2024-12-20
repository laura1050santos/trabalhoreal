from DAO import UserDAO
from flask import session

class UserRepository:
    def __init__(self) -> None:
        self.userDAO = UserDAO()

    def get_all_user(self):
        users = self.userDAO.get_all_user()
        if users:
            mensagens = "Lista de usuários recuperada com sucesso."
            return True, mensagens, users
        mensagens = "Nenhum usuário encontrado."
        return False, mensagens, []

    def get_user_by_id(self, id_user):
        if not id_user or not str(id_user).isdigit():
            mensagens = "ID do usuário é inválido ou não fornecido."
            return False, mensagens
        user = self.userDAO.get_user(id_user)
        if user:
            mensagens = "Usuário encontrado com sucesso."
            return True, mensagens, user
        mensagens = "Usuário não encontrado."
        return False, mensagens

    def get_user_by_email(self, email):
        if not email:
            mensagens = "O e-mail é obrigatório."
            return False, mensagens
        user = self.userDAO.get_user(email)
        if user:
            mensagens = "Usuário encontrado com sucesso."
            return True, mensagens, user
        mensagens = "Usuário não encontrado."
        return False, mensagens

    def create_user(self, nome, email, senha, confirmar_senha):
        if not nome or not email or not senha or not confirmar_senha:
            mensagens = "Todos os campos são obrigatórios."
            return False, mensagens
        if senha != confirmar_senha:
            mensagens = "As senhas não coincidem."
            return False, mensagens
        if len(senha) < 6:
            mensagens = "A senha deve ter pelo menos 6 caracteres."
            return False, mensagens
        try:
            self.userDAO.add_user(nome, email, senha)
            mensagens = "Usuário criado com sucesso."
            return True, mensagens
        except Exception as e:
            mensagens = f"Erro ao criar o usuário: {str(e)}"
            return False, mensagens

    def update_user(self, id_user, nome, email, senha):
        if not id_user or not nome or not email or not senha:
            mensagens = "Todos os campos são obrigatórios."
            return False, mensagens
        if len(senha) < 6:
            mensagens = "A senha deve ter pelo menos 6 caracteres."
            return False, mensagens
        user_atualizado = self.userDAO.update_user(id_user, nome, email, senha)
        if user_atualizado:
            mensagens = "Usuário atualizado com sucesso."
            return True, mensagens
        mensagens = "Erro ao atualizar o usuário."
        return False, mensagens

    def delete_user(self, id_user):
        if not id_user or not str(id_user).isdigit():
            mensagens = "ID do usuário é inválido ou não fornecido."
            return False, mensagens
        user_deletado = self.userDAO.delete_user(id_user)
        if user_deletado:
            mensagens = "Usuário deletado com sucesso."
            return True, mensagens
        mensagens = "Erro ao deletar o usuário."
        return False, mensagens

    def login(self, email, senha):
        if not email or not senha:
            mensagens = "E-mail e senha são obrigatórios."
            return False, mensagens
        user = self.userDAO.get_user_email(email)
        if user:
            if user.senha == senha:
                session['user.id'] = user.id
                mensagens = "Login realizado com sucesso."
                return True, mensagens
            mensagens = "Senha inválida."
            return False, mensagens
        mensagens = "E-mail inválido."
        return False, mensagens