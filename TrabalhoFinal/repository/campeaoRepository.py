from DAO.campeoes import CampeaoDAO

class CampeaoRepository:
    def __init__(self) -> None:
        self.campeaoDAO = CampeaoDAO()

    def get_all_campeoes(self):
        campeoes = self.campeaoDAO.get_all_campeoes()
        if campeoes:
            mensagens = "Lista de campeões recuperada com sucesso."
            return True, mensagens, campeoes
        mensagens = "Nenhum campeão encontrado."
        return False, mensagens
    

    def get_campeao_by_id(self, id_campeao):
        return self.campeaoDAO.get_Campeao(id_campeao)

    def create_campeao(self, nome, dificuldade):
        self.campeaoDAO.add_Campeao(nome, dificuldade)


    def update_campeao(self, id_campeao, nome, dificuldade):
        return self.campeaoDAO.update_Campeao(id_campeao, nome, dificuldade)

    def delete_campeao(self, id_campeao):
        return self.campeaoDAO.delete_campeao(id_campeao)

    def validar_id(id):
        pass

    def validarNome(nome):
        pass
        
    
               