#add/excluir/editar/mostrar todos/mostrar por id ou nome
from database import db
class Regiao(db.Model):
    __tablename__ = 'regioes'

    id_regiao = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(255), nullable=True)
    localizacao = db.Column(db.String(255), nullable=True)

    campeoes = db.relationship('Campeao', back_populates='regiao', lazy=True)
    def __repr__(self):
        return f"<Regiao {self.nome}>"
        
    def tojson(self):
            return {
                'id_regiao': self.id_regiao,
                'nome': self.nome,
                'desc': self.desc,
                'localizacao': self.localizacao
            }
