from flask import Flask     # Importa a biblioteca

app = Flask(__name__)   # Inicializa a aplicação,     # __name__ representa o nome do módulo

@app.route('/inicio')   # Rota da aplicação

def ola():  # Criar uma função ola() que exibe uma mensagem Olá Flask!
    return '<h1>Olá Flask!</h1>'    

app.run()   # Executa a aplicação

 ## http://127.0.0.1:5000/inicio
 ## Retorna a mensagem: 
 ## Olá Flask!