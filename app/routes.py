from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kevin'} # Mock user
    # Mock html page
    return '''
        <html>
            <head>
            <body>
                <h1>Hello, ''' + user['username'] +  '''!</h1>
            </body>
            </head>
        </html>
    '''