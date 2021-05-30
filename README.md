# Text data vizualization

This is my student project for a python programming course at SPbSTU.

It can be found [here](https://timofeyev.shinyapps.io/textviz/).

The program consists of two parts. RShiny client takes an arbitrary text from user and sends it to a server. A django server extracts the words from the text and encodes each word as a 1x26 vector. Then those codes are passed back to the client, where its' dimensionality is reduced to 1x2. Finally, the codes are plotted on a graph with the words, corresponding to those codes as label. The RShiny client of this project can be found [here](https://github.com/nineleven/text-data-visualization/).

## Installation
After cloning the repository, run
```
pip install -r requirements.txt
```
### PostgreSQL
Install PostgreSQL from https://www.postgresql.org/

Create a database and put it's credentials into environment variables as follows(use your credentials instead of 123):
```
DATABASE_NAME=123
DATABASE_USER=123
DATABASE_PASSWORD=123
DATABASE_HOST=127.0.0.1
DATABASE_PORT=123
```
Also, add
```
SECRET_KEY=your_secret_key
```
to environment variables.

Instead of using environement variables you can create file .env in [/textviz](/textviz). django-environ package will automatically detect and use it(see [django-environ](https://django-environ.readthedocs.io/en/latest/)).

### Setup django
Run
```
python server/manage.py makemigrations
```
and
```
python server/manage.py migrate
```

## Examples
### Running locally
Start a django server with
```
python server/manage.py runserver
```
