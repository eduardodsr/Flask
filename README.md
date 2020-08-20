# Flask Tutorial

### Criando uma webapp simples com Python 3😄

  ![](https://github.com/eduardodsr/Flask/blob/master/python/flask-python.png?raw=true)
  
 
 <p align="center">
  <img src=https://github.com/eduardodsr/Flask/blob/master/python/flask-python.png?raw=true" alt="imagem" width="1000px" />
 </p>
  
  

### Flask Microframework - Web apps rápidos e flexíveis

O Flask é um Microframework. Isso significa que ele não precisa de várias dependências para funcionar — ou seja, para colocar uma página na Web ou criar uma aplicação. 
Além disso, ele é muito bom pois tem uma forma bem minimalista de utilizar o Python, sem que seja necessário escrever muito código, e é muito bem organizado.

O Python, que é a linguagem que usaremos durante esse curso para criar aplicações com o Flask, é a linguagem que mais cresce atualmente. 

Se você já sabe Python, esses conhecimentos te ajudarão a trabalhar ainda melhor com a Web.

### Flask

O Flask é considerado um microframework, o que basicamente significa que ele não vem com muitas soluções embutidas para resolver problemas que não foram apresentados ainda. Dessa forma, o Flask é mais flexível: à medida em que os problemas vão aparecendo, nós os resolvemos com soluções que escolhemos no caminho, sem nos prendermos a soluções fixas.

Para começarmos a estudar o Flask, primeiro precisamos entender como funciona a Web. Quando digitamos um endereço no navegador, ele é enviado (a partir do HTTP) para um servidor, por meio de uma requisição (Request). Essa requisição é processada no servidor e enviada de volta ao navegador na forma de uma resposta (response), também por meio do HTTP.

Com essa resposta, o navegador irá renderizar o HTML ou até uma mensagem. O importante é sabermos que, no nosso caso, todo o processamento se dará no Flask.

### Requisitos

Primeiro você tem que ter Python 3, pip e uma IDE da sua preferência instalada e configurada. 

### Instalando Flask

Para instalar Flask abra um terminal (linha de comando) e execute o comando abaixo :

``` pip install flask ``` 


### Criando um arquivo Python e enviar uma mensagem no browser

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

### Criando uma aplicação web super rápido - Mostrando página HTML

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')

def ola():
    return render_template('lista.html')

app.run()
```


###  Mensagem no browser (localhost)

Para testarmos se nossa aplicação funciona. No navegador, acessaremos a URL http://127.0.0.1:5000/inicio. O resultado será a mensagem "Olá Flask!

``` http://127.0.0.1:5000/inicio ```

  ![](https://github.com/eduardodsr/Flask/blob/master/python/Flask.png?raw=true)
  
    
  
  ### Criando um template lista.html

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Jogoteca</title>
  </head>
  <body>
    <div class="container">
        <div class="page-header">
            <h1>Jogoteca</h1>
        </div>
        <table class="table table-striped table-responsive table-bordered">
            <thead class="thead-default">
                <tr>
                    <th>Nome</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>God of War</td>
                </tr>
                <tr>
                    <td>Pokemon Silver</td>
                </tr>
                <tr>
                    <td>Super Mario RPG</td>
                </tr>
            </tbody>
        </table>
    </div>
  </body>
</html>
```

###  Mensagem no browser (localhost)

Para testarmos se nossa aplicação funciona. No navegador, acessaremos a URL http://127.0.0.1:5000/inicio. 

O resultado será o template lista.html

``` http://127.0.0.1:5000/inicio ```

    
   ![](https://github.com/eduardodsr/Flask/blob/master/python/Flask2.png?raw=true)
 

```Fontes: ´´´  https://www.alura.com.br/conteudo/flask-rotas-templates-autenticacao
