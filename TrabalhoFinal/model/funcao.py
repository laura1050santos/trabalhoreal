from database import db
class Funcao(db.Model):
    __tablename__ = 'funcoes'

    id_funcao = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(255), nullable=True)

    classes = db.relationship('Classe', back_populates='funcao', lazy=True)
    
    def __repr__(self):
        return f"<Funcao {self.nome}>"

    def toJson(self):
        return {
            'id_funcao': self.id_funcao,
            'nome': self.nome,
            'desc': self.desc
        }