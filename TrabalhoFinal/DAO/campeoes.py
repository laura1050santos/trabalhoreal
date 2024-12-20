from model import Campeao
from database import db

class CampeaoDAO:
    @staticmethod
    def get_Campeao(id):
        return Campeao.query.get(id)
    
    @staticmethod
    def get_all_campeoes():
        return Campeao.query.all()
    
    @staticmethod
    def add_Campeao(nome, dificuldade):#funcao, classe, regiao
        try:
            print('chegou no DAO')
            campeao= Campeao(nome=nome, dificuldade=dificuldade,)#, funcao=funcao,classe=classe,regiao=regiao
            db.session.add(campeao)
            db.session.commit()
            return True,campeao
        except Exception as e:
            db.session.rollback()
            return e 
            
    @staticmethod
    def delete_campeao(id):
        try:
            campeao = CampeaoDAO.get_Campeao(id)
            db.session.delete(campeao)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e 
        
    @staticmethod
    def update_Campeao(id_campeao,nome, dificuldade ):#funcao, classe, regiao
        try:
            campeao = CampeaoDAO.get_Campeao(id_campeao)
            campeao.nome = nome
            campeao.dificuldade = dificuldade

            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e