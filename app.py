from bottle import route, run,static_file,error,template
from bottle import get, post, request


@route('/')
def hello():
    return static_file("/index.html",root='static/views')


@route('/hello/<name>')
def greet(name):
    return template('Hello {{name}}, how are you?', name=name)



@route('/img/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/img/')

@route('/css/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/css/')





@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('UserName: {{name}}\n Password: {{pwd}}', name=username,pwd=password)



@error(404)
def error404(error):
    return static_file("/404.html",root='views')

run(host='0.0.0.0', port=8080, debug=True)