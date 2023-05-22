from flask import Flask,render_template, request, redirect, url_for
from controllers.login_controller import login
from controllers.base_controller import base
from controllers.iot_controller import iot
from controllers.cadastro_controller import cadastro

app = Flask(__name__, template_folder="./templates/",)



app.secret_key = '4,vuyccvfdsgfdsgfdguylutu5tu'

app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(cadastro, url_prefix='/cadastro')
app.register_blueprint(base, url_prefix='/base')
app.register_blueprint(iot, url_prefix='/iot')

@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(port="8080")

    



