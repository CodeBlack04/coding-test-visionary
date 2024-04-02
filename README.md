# Project Name: Coding Test Visionary Tech Solutions (Completed)

## Introduction
This project utilizes Django as the web framework, Tailwind CSS for styling, Django Rest Framework for building RESTful APIs and postgreSQL for database.

## Setup Instructions (Docker)

### 1. Install Docker-desktop

### 2. Clone the Project
```bash
git clone git@github.com:CodeBlack04/coding-test-visionary.git
cd coding-test-visionary
```

### 3. Build the image
```bash
docker-compose build
```

### 4. Run the container
```
docker-compose up
```

## Setup Instructions (Without Docker)
In this case sqllite3 is used for the database.
### 1. Clone the Project
```bash
git clone git@github.com:CodeBlack04/coding-test-visionary.git
cd coding-test-visionary
```
### 2. Install virtualenv, create a virtual environment(env).
```bash
pip install virtualenv
python3 -m venv env
```
### 3. Activate the environment and install packages to the environment.
```bash  
source env/bin/activate
pip install -r requirements.txt
```

### 4. Edit system.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 5. Activate the server:
```bash
python manage.py runserver
```

## API (jsonresponse):
#### Users: http://localhost:8000/api/users/
#### Moviess: http://localhost:8000/api/movies/
#### Ratings: http://localhost:8000/api/ratings/

## Database
PostgreSQL was the recommended database, although it requires system-wide configuration of the database and user. I couldn't figure out how to set up Postgres in the virtual environment. As I wanted to preserve all essential setups and packages in the virtual environment, I utilised the default sqllite3 database.

## Here is a description to setup postgreSQL database if required:
### Deactivate the virtual environment:
```bash
deactivate
```
### Setup and configure postgreSQL:
```bash
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
sudo su postgres psql
CREATE DATABASE test;
CREATE USER test WITH PASSWORD 'test';
ALTER ROLE test SET client_encoding TO 'utf8';
ALTER ROLE test SET default_transaction_isolation TO 'read committed';
ALTER ROLE test SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE test TO test;
\q
```
### Configure postgreSQL in settings.py:
```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
```
### Initialize the database:
```bash
source env/bin/activate
pip install psycopg2
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


  
