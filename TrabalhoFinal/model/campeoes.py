from database import db

class Campeao(db.Model):
    __tablename__ = 'campeoes'

    id_campeao = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    dificuldade = db.Column( db.String(50), unique=True, nullable=False)

    id_funcao = db.Column(db.Integer, db.ForeignKey('funcoes.id_funcao'), nullable=False)
#    id_classe = db.Column(db.Integer, db.ForeignKey('classes.id_classe'), nullable=False)
    id_regiao = db.Column(db.Integer, db.ForeignKey('regioes.id_regiao'), nullable=False)
    
#    funcao = db.relationship('Funcao', back_populate='campeoes')
#    regiao = db.relationship('Regiao', back_populates='campeoes', uselist=False)
#    classe = db.relationship('Classe', back_populates='campeoes')


    def __repr__(self):
        return f"<Campeao {self.nome}>"

    def toJson(self):
        return {
            'id_campeao': self.id_campeao,
            'nome': self.nome,
            'dificuldade': self.dificuldade        }
#            'lancamento': self.lancamento,
#            'classe':self.classe,
     #       'funcao': self.funcao
            

      