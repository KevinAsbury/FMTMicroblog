# FlaskMegaTutorial
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Environement setup
Make sure you have python3 installed.
Create a virtual environment (linux, MacOS, & WSL):
'''
cd microblog
python3 venv venv
source venv/bin/activate
pip install Flask
pip install Flask-WTF
'''

## Runnng the microblog
```
cd microblog
source venv/bin/activate
export FLASK_APP=microblog.py
export SECRET_KEY='6KeGb8GFX3ASx9H9M8DB'
flask run
```
