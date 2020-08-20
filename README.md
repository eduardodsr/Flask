# Flask Tutorial

### Criando uma Aplicação Web com Flask - Exemplo Simples - Parte 1 😄

Primeiro você tem que ter Python 3, pip e uma IDE da sua preferência instalada e configurada. 
Se você ainda não tem, você pode encontrar tutoriais sobre como instalar e configurar tudo isso no nosso curso de Python.

Primeiro vamos criar uma pasta para o nosso projeto, vamos chamar de “Flask Tutorial” e dentro dela vamos criar o arquivo main.py e uma segunda pasta, chamada templates. 
Dentro da pasta templates crie o arquivo index.html. Pronto! Temos todos os arquivos que precisamos para o nosso exemplo.

### Instalando Flask
Para instalar Flask abra um terminal (linha de comando) na pasta Flask Tutorial e execute o comando abaixo:

pip install flask
Primeiro programa em Flask
Vá no arquivo main.py e escreva o seguinte código:

from flask import Flask # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
  return 'Meu site em Flask :D'

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação
Na primeira linha nós estamos importando a biblioteca flask, depois a gente registra uma rota na nossa aplicação usando uma annotation. A annotation especifíca que a função main será executada quando um usuário fizer uma requisição no endereço “http://localhost:5000/” (root).

Caso você queira um endereço diferente, basta modificar o parâmetro do método route, por exemplo @app.route('/novo-caminho') executará a função quando o usuário acessar “http://localhost:5000/novo-caminho”.

Por fim, a gente roda a aplicação. Para executar a aplicação em Flask basta executar nosso programa usando o comando:

python main.py
Agora vá no seu navegador e use a URL http://127.0.0.1:5000/ ou http://localhost:5000/ e você verá seu site rodando 😄.

### Criando uma lógica
Para criar uma exemplo mais interessante nós vamos criar uma versão online do problema Aprovado e Reprovado. Para isso vamos receber o valor de duas notas e criar a lógica que determina se, dada as duas notas, o aluno está “Aprovado”, de “Recupação” ou “Reprovado”.

from flask import Flask, request # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Nova rota
def main():
  resultado = 'Entre as notas na URL'    

  primeira = request.args.get('primeira')
  segunda = request.args.get('segunda')

  if primeira and segunda:
        
    primeira = float(primeira)
    segunda = float(segunda)

    media = (primeira + segunda) / 2
    if media >= 7:
        resultado = 'Aprovado'
    elif media >= 4:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado'

  return resultado

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação
Nesse exemplo vamos pegar os valores passados como argumentos na URL. Para isso usamos o comando request.args.get('nome do parametro'), note que você precisa importar request da biblioteca flask.

Para testar use a URL http://localhost:5000/?primeira=6&segunda=7 (teste vários outros valores para as notas).

Template em Jinja e HTML
Já fizemos bastante coisa, mas nossa aplicação ainda não está parecendo com um site haha. Para isso vamos fazer nossa função retornar código HTML.

No seu arquivo index.html escreva o código abaixo:

´´´
<html>
    <head>
        <title>Meu primeiro site :D</title>
    </head>
    <body>
        Aprovado ou Reprovado

        <div>
            <form method="get">
                Primeira Nota:
                <input type="text" name="primeira">
                <br>
                Segunda Nota:
                <input type="text" name="segunda">
                <br>
                <input type="submit" value="Enviar">
            </form>
        </div>

        {% if resultado %}
        <div>
            {{resultado}} com média {{media}}!!!
        </div>
        {% endif %}

    </body>
</html>
´´´
Infelizmente não podemos entrar em detalhe sobre a sintaxe do HTML nesse tutorial. Mas vamos destacar algumas coisas importantes.

É importante que as tags input tenham um atributo name que vamos usar para retornar o valor submetido.
O if não faz parte da sintaxe do HTML. Nós estamos usando Jinja, que é a sintaxe de template padrão no Flask.
As últimas linhas do body podem ser lidas como: “Se a variável resultado tem um valor diferente de None, mostre a seguinte div”. Adicionamente, a linha {{resultado}} com média {{media}}!!! será pré-processada e irá mostrar os valores das variáveis resultado e media.
Na parte do servidor vamos mudar nosso código para processar os valores submetidos quando o usuário clica no botão “Enviar”.

from flask import Flask, request, render_template # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Nova rota
def main():
    resultado = None
    media = None    

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    if primeira and segunda:  
        primeira = float(primeira)
        segunda = float(segunda)

        media = (primeira + segunda) / 2
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return render_template('index.html', media=media,
                                         resultado=resultado)

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação

Primeiro precisamos importar o método render_template da biblioteca flask. Depois você deve se atentar à alguns detalhes importantes:

Note que os valores dos parâmetros tem o mesmo nome do atributo name especificado nas tags input do HTML.
Estamos usando o função render_template para pré-processar nosso arquivo index.html e estamos passando os valores media e resultado para o template.
Note que, por padrão, Flask procura seu arquivo de template dentro da pasta templates, por isso você só precisa definir qual template você quer usar e não o caminho completo até o arquivo.
Para simplificar ainda mais o nosso exemplo nós estamos passando os valores do form por requisições do tipo GET, o que não é aconselhável.
Agora basta ir no seu navegador na URL http://localhost:5000/ e digitar os valores das suas notas 😄.


