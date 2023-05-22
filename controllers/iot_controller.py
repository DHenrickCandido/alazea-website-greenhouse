from flask import Blueprint, render_template, request

iot = Blueprint("iot", __name__, template_folder = './views/', static_folder='./static/', root_path="./")

estufas = ["","1", "2", "3"]
temperatura = ["",36.5, 28.9, 38.2]
umidade = ["","80%","77%","60%"]
nivel_agua = ["","300ml","220ml","50ml"]
estufa_selecionada = 0

@iot.route("/")
def iot_index():
    estufa_selecionada = 0
    return render_template("/iot/iot_index.html", estufas = estufas, temperatura = temperatura, estufa_selecionada = estufa_selecionada, umidade = umidade, nivel_agua=nivel_agua)

@iot.route("/exibe_estufa", methods=["POST","GET"])
def iot_exibe_estufa():
    global estufa_selecionada
    estufa_selecionada = int(request.form.get("sel_estufa"))    

    if estufa_selecionada < 0:
        estufa_selecionada = 0

    return render_template("/iot/iot_index.html", estufas = estufas, temperatura = temperatura, estufa_selecionada = estufa_selecionada,umidade = umidade, nivel_agua=nivel_agua)