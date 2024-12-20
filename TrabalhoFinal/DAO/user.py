from model import User
from database import db

class UserDAO:
    @staticmethod
    def get_user_by_id(id_user):
        return User.query.get(id_user)
    
    @staticmethod
    def get_user_by_email(email):
        return User.query.get(email)
    
    @staticmethod
    def get_all_user():
        return User.query.all()
    
    @staticmethod
    def add_user(id_user, nome, email, senha):
        try:
            user = User(id_user=id_user, nome=nome, email=email, senha=senha)
            db.session.add(user)
            db.session.commit()
            return True,user
        except Exception as e:
            db.session.rollback()
            return e 
            
    @staticmethod
    def delete_user(id_user):
        try:
            user = UserDAO.get_user(id_user)
            db.session.delete(user)
            db.session.commit()
            return True,user
        except Exception as e:
            db.session.rollback()
            return e 
        
    @staticmethod
    def update_user(id_user, nome, email, senha):
        try:
            user = UserDAO.get_user(id_user)
            user.nome = nome
            user.email = email
            user.senha = senha
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

