# Projeto desenvolvido recorrente ao desafio solicitado pela 4i
Este projeto será deletado em alguns dias :)


## Instalações

Este projeto possuí dependências de ferramentas utilizadas para desenvolvimento de aplicações Python.

Python - https://python.org.br/instalacao-linux/
```sh
sudo apt-get install python3
```

Poetry - https://python-poetry.org/docs/#installation
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

## Guia utilização

Após a instalação das dependências, execute o seguinte comando no terminal:

Linux:
```sh
export FLASK_APP=app 
```

Windows (Powershell):
```sh
$env:FLASK_APP = "app"    
```

Com o projeto instalado, acesse o diretório através do terminal ./**src** e execute o comando abaixo

```sh
poetry run flask run   
```

O projeto se inicializará com as dependências necessárias.
