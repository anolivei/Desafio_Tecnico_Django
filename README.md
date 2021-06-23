
<h1 align="center">Django Technical Challenge</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/anoliveisolcap/desafio_tecnico_django?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/anoliveisolcap/desafio_tecnico_django?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/anoliveisolcap/desafio_tecnico_django?color=56BEB8">

<img alt="Github forks" src="https://img.shields.io/github/forks/anoliveisolcap/desafio_tecnico_django?color=56BEB8">

<img alt="Github stars" src="https://img.shields.io/github/stars/anoliveisolcap/desafio_tecnico_django?color=56BEB8">
</p>

<p align="center">
  <a href="#about">About</a> &#xa0; | &#xa0; 
  <a href="#features">Features</a> &#xa0; | &#xa0;
  <a href="#technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#starting">Starting</a> &#xa0; | &#xa0;
  <a href="#cheatsheet">CheatSheet</a> &#xa0; | &#xa0;
  <a href="https://github.com/anoliveisolcap" target="_blank">Author</a>
</p>

<br>

## About ##

A Web Application made in Django REST framework and Python.

## Features ##
- /all: Lists the entire dataset
- /youngers/{n}: Returns a list of the n youngest people sorted ascending
- /olders/{n}: Returns a list of the oldest people sorted ascending
- /gender-distribution: Returns a Json with the percentage distribution of genders in the dataset: Ex.: {"Female" 51%, "Male": 49%}
- /people/{cpf_without_punctuation}: Returns single person data in Json format
- /blood-type/stats: returns the absolute distribution of blood groups: {"B-": 20, "O+": 10...}
- /peoples: List the names of all people in the dataset in alphabetical order
- /peoples/search?q=query: Search for people by name or by part of the name (case insensitive)

## Technologies ##

The following tools were used in this project:

- Python
- Django
- Django REST framework


## Requirements ##

Before starting, you need to have all the [requirements](https://github.com/anoliveisolcap/Desafio_Tecnico_Django/blob/main/requirements.txt) installed

## Starting ##

```shell
# Clone this project
$ git clone https://github.com/anoliveisolcap/desafio_tecnico_django

# Access the directory
$ cd desafio_tecnico_django

# to create a superuser
$ python manage.py createsuperuser --username=your_name --email=your_email@example.com

# Run the server
$ python manage.py runserver

# Test (test while your server is running xD)
$ python manage.py test
```

## CheatSheet ##

```shell
# Start project
$ django-admin startproject "project_name" .

# Start app
$ django-admin startapp "app_name"

# Allow data base
$ python manage.py migrate

# To create migrations
$ python manage.py makemigrations

# To clean all migrations
$ python manage.py migrate your_app zero

# sqlite importing data
$ sudo apt install sqlite3

# executing sqlite
$ sqlite3 db.sqlite3

# into the sqlite terminal
sqlite> .mode csv
qlite> .import people_data.csv solcap_person

# To open a django's shell terminal
$ python manage.py shell

# To add data into a model - example
$ Person.objects.create(nome="Maria da Silva", cpf="111.222.333-44", rg="11.222.333-4")
$ test = Person.objects.all()[0]
$ test.nome
'Maria da Silva'

# To see all the packages installed
$ pip freeze
```

&#xa0;

<a href="#top">Back to top</a>
