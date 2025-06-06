from flask import Flask, render_template  #importa Flask e função para renderizar HTML
from frutas import Fruta  #importa a classe Fruta

app = Flask(__name__)  # cria o app Flask


# cria 3 frutas com id, nome e cor
f1 = Fruta()
f1.set_id(1)
f1.set_nome("Maçã")
f1.set_cor("Vermelha")

f2 = Fruta()
f2.set_id(2)
f2.set_nome("Banana")
f2.set_cor("Amarela")

f3 = Fruta()
f3.set_id(3)
f3.set_nome("Morango")
f3.set_cor("Vermelha")

frutas = [f1, f2, f3]  #lista que vai guardar objetos Fruta


#rota principal (/) mostra todas as frutas
@app.route('/')
def index():
    return render_template("index.html", frutas=frutas)


#colocar o id na rota

#rota /<id> mostra os detalhes da fruta com aquele id
@app.route('/<int:id>')  #essa linha cria uma rota dinâmica: /1, /2, /3... 
def fruta(id):  #função fruta que recebe o id da fruta pela URL
    for fruta in frutas:  #para FRUTA em FRUTAS percorre a lista de frutas
        if fruta.get_id() == id:  #se achar uma fruta com o id igual ao da URL
            return render_template("fruta.html", fruta=fruta)  #mostra a página com os dados da fruta
    return "Fruta não encontrada", 404  #se não achar, mostra erro 404





