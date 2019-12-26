# api-troco
API que calcula o troco correto e a menor quantidade possível de cédulas a devolver. Contém endpoints implementados para total funcionalidade CRUD com dados armazenados num banco MongoDB.

## Módulos utilizados e versões
- Python 3.7.4
- dataclasses 0.6
- Django 2.2.9
- djangorestframework 3.11.0
- djongo 1.2.38
- dnspython 1.16.0
- pip 19.3.1
- pymongo 3.10.0
- pytz 2019.3
- setuptools 40.8.0
- sqlparse 0.2.4

## Instalação
Inicie baixando ou clonando o repositório em seu computador. Para iniciar o projeto garanta que Python e o módulo pip estejam já instalados, caso não estejam, instale o Python na versão 3.7.4 [clicando aqui](https://www.python.org/downloads/release/python-374/).

Após ter o Python instalado, baixe e instale o pip utilizando o terminal do sistema operacional de seu computador com o comando correspondente:  
Baixar: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`  
Windows: `python get-pip.py` ou `py get-pip.py`  
Linux: `$ sudo apt install python3-pip`  
Mac: `sudo easy_install pip`  

Para utilizar todas as funções é importante que todos os módulos listados acima estejam instalados no ambiente nas versões informadas. Recomendo a criação de um ambiente virtual para impedir colisões com versões diferentes já instaladas. Dentro da primeira pasta do diretório você encontrará o arquivo **requirements.txt** que ajudará com a instalação das versões corretas. 

Primeiro, utilizando o terminal vá até o diretório onde salvou o projeto, crie e inicie um ambiente virtual com os seguintes comandos:  
Criar: `python -m venv venv`  
Iniciar no Windows: `venv/Scripts/activate`  
Linux e Mac: `$ source venv/bin/activate`  

Para a instalação dos módulos, rode o seguinte comando no terminal, substitua com o caminho para o diretório onde salvou esse arquivo:
`pip install -r /path/requirements.txt`.

## Inicialização
Após ter instalado todos os módulos em seu ambiente virtual e estar com o ambiente virtual ativado, vá até o diretório '/apitroco/' do projeto pelo terminal e execute o comando `python manage.py runserver`. Esse comando inicializará o servidor local em seu computador e você já poderá acessar o serviço pelo seu navegador no link http://localhost:8000/. Acessar o site pelo navegador te dará uma visualização dos endpoints disponíveis para requisições, abaixo está um manual sobre o funcionamento de cada uma e exemplos de como testar requisições pelo terminal.

## Fazendo requisições
Para fazer requisições você pode utilizar o próprio navegador pois na página de cada método haverá uma interface criada automaticamente pelo módugo rest_framework. Porém, recomendo que utilize um serviço como Postman ou o próprio terminal para requisições completas. Abaixo listei todos os métodos e exemplos de como requisitar pelo terminal. Para todos será necessário manter uma janela do terminal com o servidor ativo e outra para fazer a requisição. Na janela onde fará as requisições, instale o módulo "requests" com o comando `pip install requests` e depois ative o interpretador python com o comando `python`. A API pode ser utilizada com os seguintes métodos e respectivas funções:

- /api/criar_moeda/  
Método `POST` que recebe os dados de valor, tipo('nota' ou 'moeda') e código(sigla da taxa de câmbio da moeda, ex: BRL, USD) para criar uma nova moeda na base. Crie a nota de 1 dólar na base com os seguintes comandos no interpretador python no terminal:  
```
>>> import requests
>>> url = "http://localhost:8000/api/criar_moeda/"
>>> data = {"valor": 1, "tipo": "nota", "codigo": "USD"}
>>> r = requests.post(url = url, data = data)
>>> resp = r.text
>>> resp
```
Ao digitar 'resp' e apertar enter você deverá receber uma mensagem com o valor "Nova moeda registrada com sucesso." em caso de sucesso. No método seguinte você listará todas as moedas e já poderá ver no fim da lista a que criou agora.
- /api/listar_moedas/  
Mátodo `GET` que retorna uma lista com id, valor e código da moeda de todas as moedas registradas na base. Para fazer uma requisição no terminal:
```
>>> import requests
>>> url = "http://localhost:8000/api/listar_moedas/"
>>> r = requests.get(url = url)
>>> resp = r.text
>>> resp
```
'resp' nesse caso deverá retornar a lista deverá retornar com os dados informados e observando no fim da lista poderá ver a moeda que criou no método anterior (caso tenha o executado).

- /api/atualizar_moeda/
- /api/deletar_moeda/
- /api/troco_certo/  
Para ver essa função em ação, digamos que você é o/a operador(a) de caixa de uma loja e o valor final de uma compra foi R$37,50. O cliente pagou com uma nota de R$100,00. Sem spoilers do valor correto e sem necessidade do cálculo mental, execute o código abaixo no terminal para ter o valor correto do troco e as cédulas que você deve retornar ao cliente (pensando na menor quantidade possível de cédulas e moedas):
```
>>> import requests
>>> url = "http://localhost:8000/api/troco_certo/"
>>> data = {"valor_total": 37.5, "valor_pago": 100}
>>> r = requests.post(url = url, data = data)
>>> resp = r.text
>>> resp
```  
O retorno de 'resp' retornará o troco correto e as cédulas em uma mensagem "bonita". Também seria possível alterar o código para retornar um JSON com essas informações para que elas pudessem ser lidas, interpretadas e retornadas por um possível sistema de caixa da maneira preferida pela empresa.
