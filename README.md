# Flask Tutorial

### CURSO FLASK PARTE 1: CRIE UMA WEBAPP COM PYTHON 3 😄

### Criando uma Aplicação Web com Flask 

Primeiro você tem que ter Python 3, pip e uma IDE da sua preferência instalada e configurada. 

### Instalando Flask

Para instalar Flask abra um terminal (linha de comando) na pasta Flask Tutorial e execute o comando abaixo:

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
 

```Fontes: ´´´  https://neps.academy
