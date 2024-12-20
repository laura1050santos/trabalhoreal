#add/excluir/editar/mostrar todos/mostrar por id ou nome
from flask import Flask, render_template, Blueprint, redirect, url_for,request
from database import init_app, db
from DAO import *
from repository import CampeaoRepository

campeoes_repository = CampeaoRepository()

campeoesController = Blueprint("campeao", __name__)

@campeoesController.route('/ver-campeoes', methods=['GET'])
def ver_campeoes():
    campeoes = campeoes_repository.get_all_campeoes()
    return render_template('/campeao/get_all_campeao.html', campeoes=campeoes)

@campeoesController.route('/get_id', methods=['GET'])
def ver_id():
    id_campeao = request.form.get('id_campeao')
    campeao = campeoes_repository.get_campeao_by_id(id_campeao)
    return render_template("/campeao/get_id_campeao.html", campeao=campeao)


@campeoesController.route('/add_campeao',methods=['POST', 'GET'])
def add_campeao():
    if request.method == 'POST':
        nome = request.form.get('nome')
        dificuldade = request.form.get('dificuldade')
        campeoes_repository.create_campeao(nome,dificuldade) #chama a função do repository que 
        return redirect(url_for('campeao.ver_campeoes'))
    return render_template('/campeao/add_campeao.html')

    
@campeoesController.route('/update_campeao', methods=['POST', 'GET'])
def update_campeao():
    if request.method == 'POST':
        id_campeao = request.form.get('id_campeao')
        nome = request.form.get('nome')
        dificuldade = request.form.get('dificuldade')
        campeoes_repository.update_campeao(id_campeao, nome, dificuldade)
        return redirect(url_for('campeao.ver_campeoes'))
    return render_template('/campeao/update_campeao.html')

@campeoesController.route('/delete_campeao',methods=['POST', 'GET'])
def delete_campeao():
    if request.method == 'POST':
        id_campeao = request.form.get('id_campeao')

        campeao = campeoes_repository.get_campeao_by_id(id_campeao)
        campeoes_repository.delete_campeao(campeao)
        return redirect(url_for('campeao.ver_campeoes'))
    return render_template('/campeao/delete_campeao.html')