from database import db

class User(db.Model):
    __tablename__ = 'usuario'

    id_user = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, index=True) 
    email = db.Column(db.String(160), nullable=False, unique=True )
    senha = db.Column(db.String(80), nullable= False)

    def __repr__(self):
            return f"<nome {self.nome}>"
    def toJson(self):
            return {
                "id_user": self.id_user,
                "nome":self.nome,
                "email":self. email,
                "senha":self.senha,
                }