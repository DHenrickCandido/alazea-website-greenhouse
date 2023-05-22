from flask import Blueprint, render_template,request,redirect,url_for,flash,g
from controllers.login_controller import email, usuarios

cadastro = Blueprint("cadastro", __name__, root_path="./")

@cadastro.route('/', methods =["post","get"])
def cadastro_index():
    return render_template('/login/lista_users.html', e_mail = email, users = usuarios)
