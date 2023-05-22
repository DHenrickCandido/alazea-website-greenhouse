from flask import Blueprint, render_template,request,redirect,url_for,flash,g

login = Blueprint("login", __name__, root_path="./")

email = []
usuarios = []
senhas = []

@login.route('/')
def login_index():
    return render_template('/login/login.html')

#@login.route('/teste')
#def teste():
 #   return render_template('cadastro_controller.lista_users')

@login.route('/ccadastro')
def ccadastro():
    return render_template('/login/cadastro.html')

@login.route('/login_user', methods=["POST","GET"])
def login_user():
    username = request.form.get("username", None)
    senha = request.form.get("Senha", None)

    global usuarios, senhas
    for user, password in zip(usuarios,senhas):
        if username == user and senha == password: 
            return redirect(url_for("cadastro.cadastro_index"))
    flash('Usuário e/ou senha incorretos')
    return redirect(url_for("login.login_index"))

@login.route('/cadastro', methods=["POST","GET"])
def cadastro():
    username = request.form.get("username", None)
    e_mail = request.form.get("email", None)
    senha = request.form.get("Senha", None)

    global usuarios, email, senhas
    usuarios.append(username)
    email.append(e_mail)
    senhas.append(senha)

    return redirect(url_for("login.login_index"))
