from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    lista = ['Nome', 'Email', 'Mensagem']
    lista2 = ['Seu Nome:', 'Seu E-mail:', 'Sua Mensagem']
    return render_template('contato.html', list=lista, list2=lista2)

if __name__ == '__main__':
    app.run()
