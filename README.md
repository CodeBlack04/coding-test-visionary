Framework = Django | CSS = Tailwind | Rest-Framework = djangorestframework | Datavase = sqllite3

**Setup instructions:**
1. Clone the project and enter the directory.
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

  
