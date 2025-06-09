from flask import Flask, render_template
from livro import Livro
app = Flask(__name__)

livro1 = Livro()
livro1.set_id(1)
livro1.set_nome("As Crônicas de Nárnia ")
livro1.set_autor("C. S. Lewis")
livroLista = [livro1]

@app.route('/')
def index():
    return render_template("index.html", livroLista = livroLista)

@app.route('/<int:id>')
def detalhes(id):
    for i in livroLista:
        if i.get_id() == id:
            return render_template("detalhes.html", detalhesLivro = i)
    return "Erro"