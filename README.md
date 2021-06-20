
<h1 align="center">Desafio Técnico Django</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/anolivei/desafio_tecnico_django?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/anolivei/desafio_tecnico_django?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/anolivei/desafio_tecnico_django?color=56BEB8">

<img alt="Github forks" src="https://img.shields.io/github/forks/anolivei/desafio_tecnico_django?color=56BEB8">

<img alt="Github stars" src="https://img.shields.io/github/stars/anolivei/desafio_tecnico_django?color=56BEB8">
</p>

<p align="center">
  <a href="#about">About</a> &#xa0; | &#xa0; 
  <a href="#features">Features</a> &#xa0; | &#xa0;
  <a href="#technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#starting">Starting</a> &#xa0; | &#xa0;
  <a href="https://github.com/anolivei" target="_blank">Author</a>
</p>

<br>

## About ##

Describe your project...

## Features ##
...

## Technologies ##

The following tools were used in this project:

- Python
- Django
- Django rest framework


## Requirements ##

Before starting :checkered_flag:, you need to have...

## Starting ##

```shell
# Clone this project
$ git clone https://github.com/anolivei/desafio_tecnico_django

# Access
$ cd desafio_tecnico_django

# Start project
$ django-admin startproject "project_name" .

# Start app
$ django-admin startapp "app_name"

# Allow data base
$ python manage.py migrate

# To create migrations
$ python manage.py makemigrations

# running the server
$ python manage.py runserver

$ python manage.py migrate your_app zero

$ python manage.py shell
$ Person.objects.create(nome="maria da silva", cpf=11122233344, rg=123456789)
$ test = Person.objects.all()[0]
$ test.nome
'maria da silva'

# sqlite importing data
$ sudo apt install sqlite3
$ sqlite3 db.sqlite3
sqlite> .mode csv
qlite> .import people_data.csv youngers_person
# To see all the packages installed
$ pip freeze
```

&#xa0;

<a href="#top">Back to top</a>
