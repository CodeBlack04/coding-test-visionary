# Project Name: Coding Test Visionary

## Introduction
This project utilizes Django as the web framework, Tailwind CSS for styling, and Django Rest Framework for building RESTful APIs. Initially, SQLite3 was chosen as the database due to its simplicity and ease of setup within the virtual environment. However, for production, PostgreSQL is recommended, and instructions for setting up PostgreSQL are provided below.

## Setup Instructions

### Clone the Project
```bash
  git clone git@github.com:CodeBlack04/coding-test-visionary.git
  cd coding-test-visionary
2. Install virtualenv, create a virtual environment(env).
  pip install virtualenv
  python3 -m venv env
3. Activate the environment and install packages to the environment.
  source env/bin/activate
  pip install -r requirements.txt
4. Activate the server:
   python manage.py runserver

**Database**
PostgreSQL was the preferred database to go but it requires setting up the database and user system-wide. I couldn't figure out a way to setup postgres in the virtual environment. As i wanted to keep all required configurations and packages in the virtual environment, thus default sqllite database was used.

**Here is a description to setup postgreSQL database if required:**
1. Deactivate the virtual environment:
deactivate
2. Setup and configure postgreSQL:
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
sudo -u postgres psql
CREATE DATABASE test;
CREATE USER test WITH PASSWORD 'test';
ALTER ROLE test SET client_encoding TO 'utf8';
ALTER ROLE test SET default_transaction_isolation TO 'read committed';
ALTER ROLE test SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE test TO test;
\q

3. Configure postgreSQL in settings.py:
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

4. Initialize the database:
   source env/bin/activate
   pip install psycopg2
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver 


  
