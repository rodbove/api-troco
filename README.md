# api-troco
API que calcula o troco correto e a menor quantidade possível de cédulas a devolver.

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

Após ter o Python instalado, baixe e instale o pip utilizando o terminal do sistema operacional que utiliza com o comando correspondente:
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
Após ter instalado todos os módulos em seu ambiente virtual e estar com o ambiente virtual ativado, vá até o diretório '/apitroco/' do projeto pelo terminal e execute o comando `python manage.py runserver`. Esse comando inicializará o servidor local em seu computador e você já poderá acessar o serviço pelo seu navegador no link http://localhost:8000/.  

## Métodos para requisições
A API pode ser utilizada com os seguintes métodos e respectivas funções:

- /criar_moeda/
- /listar_moedas/
- /atualizar_moeda/
- /deletar_moeda/
- /troco_certo/
