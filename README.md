# Flask Tutorial

### Flask parte 1: Crie uma webapp com Python 3😄

Flask Microframework - Web apps rápidos e flexíveis

O Flask é um Microframework. Isso significa que ele não precisa de várias dependências para funcionar — ou seja, para colocar uma página na Web ou criar uma aplicação. 
Além disso, ele é muito bom pois tem uma forma bem minimalista de utilizar o Python, sem que seja necessário escrever muito código, e é muito bem organizado.

O Python, que é a linguagem que usaremos durante esse curso para criar aplicações com o Flask, é a linguagem que mais cresce atualmente. 

Se você já sabe Python, esses conhecimentos te ajudarão a trabalhar ainda melhor com a Web.

### Requisitos

Primeiro você tem que ter Python 3, pip e uma IDE da sua preferência instalada e configurada. 

### Instalando Flask

Para instalar Flask abra um terminal (linha de comando) e execute o comando abaixo :

``` pip install flask ``` ou

``` pip install flask ```

### Criar um arquivo main.py e enviar uma mensagem de teste no browser

```
from flask import Flask     # Importa a biblioteca

app = Flask(__name__)   # Inicializa a aplicação,     # __name__ representa o nome do módulo

@app.route('/inicio')   # Rota da aplicação

def ola():  # Criar uma função ola() que exibe uma mensagem Olá Flask!
    return '<h1>Olá Flask!</h1>'    

app.run()   # Executa a aplicação

 ## http://127.0.0.1:5000/inicio
 ## Retorna a mensagem: 
 ## Olá Flask!
```
 

```Fontes: ´´´  https://www.alura.com.br/conteudo/flask-rotas-templates-autenticacao
