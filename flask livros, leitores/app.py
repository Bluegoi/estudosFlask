from flask import Flask, render_template
from livros import Livro
from leitores import Leitores
app = Flask(__name__)

leitor1 = Leitores()
leitor1.set_id(1)
leitor1.set_nome("Joao")
leitor1.set_idade(20)
leitor1.set_foto("gettyimages-1410538853-612x612.jpg")

leitor2 = Leitores()
leitor2.set_id(2)
leitor2.set_nome("Felipe")
leitor2.set_idade(20)
leitor2.set_foto("gettyimages-1410538853-612x612.jpg")


leitor3 = Leitores()
leitor3.set_id(3)
leitor3.set_nome("Neymar")
leitor3.set_idade(20)
leitor3.set_foto("gettyimages-1410538853-612x612.jpg")

listaLeitores = [leitor1, leitor2, leitor3]

livro1 = Livro()
livro1.set_id(1)
livro1.set_nome("As crônicas de nárnia")
livro1.set_cor("Vermelho")

livro2 = Livro()
livro2.set_id(2)
livro2.set_nome("As crônicas de nárnia 2")
livro2.set_cor("azul")
listaLivro = [livro1, livro2]

@app.route('/')
def index():
    return render_template("index.html", listaLeitores = listaLeitores, listaLivro = listaLivro)

@app.route('/<int:id>')
def detalhesLivro(id):
    for i in listaLivro:
        if i.get_id() == id:
            return render_template("livro.html", livroDetalhe = i, listaLivro = listaLivro, listaLeitores = listaLeitores)
    return "erro"

@app.route('/<nome>')
def leitor(nome):
    for i in listaLeitores:
        if i.get_nome() == nome:
            return render_template("leitor.html", leitorDetalhes = i,  listaLivro = listaLivro, listaLeitores = listaLeitores)
    return "erro"