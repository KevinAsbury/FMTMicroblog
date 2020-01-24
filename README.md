# FlaskMegaTutorial
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Install and initial setup
Make sure you have python3 and Pipenv installed.
Use pipenv to install dependencies.
If using Postgres then create the database. No need to do this if you prefer SQLite.
```
git clone https://github.com/KevinAsbury/FMTMicroblog.git
cd microblog
pipenv shell
createdb fmtmicroblog
flask db init
flask db migrate
flask db upgrade
```

## Runnng the microblog
Debug mode is optional:
Note: The app will default to SQLite if no database URI environment variable is provided
```
cd microblog
pipenv shell
export FLASK_APP=microblog.py
export SECRET_KEY='TheKeyThatMustNotBeNamed'
export SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost:5432/fmtmicroblog'
export FLASK_DEBUG=true
flask run
```
