# api_estudante

## Pré-requisitos do sistema
- [Git](https://git-scm.com)
- Python 3.7.1

```
Para Windows é necessário instalar antes
Visual studio >= 2014
```

## criando ambiente para a aplicação
- apt-get install python3-venv
- python3 -m venv venv 

## ativando o ambiente
- . venv/bin/activate

## instalando dependências
- pip install -r requirements.txt

## configurando a aplicação dentro da pasta estudante  
- python manage.py makemigrations
- python manage.py migrate

## criando usuario para a aplicação
- python manage.py createsuperuser

## rodando a aplicação OBS: sempre ativar o ambiente antes
- python manage.py runserver

## consumindo a API
- http://localhost:8000/