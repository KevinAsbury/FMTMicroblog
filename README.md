# FlaskMegaTutorial
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Environement setup
Make sure you have python3 and Pipenv installed.
Use pipenv to install dependencies.
'''
cd microblog
Pipenv shell
'''

## Runnng the microblog
Debug mode is optional:
```
cd microblog
pipenv shell
export FLASK_APP=microblog.py
export SECRET_KEY='TheKeyThatMustNotBeNamed'
export SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost:5432/fmtmicroblog'
export FLASK_DEBUG=true
flask run
```
