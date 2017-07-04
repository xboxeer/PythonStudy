from bottle import route,run,static_file
@route('/')
def home():
    return static_file('index.html',root='WebStudy')
@route('/echo/<thing>')
def echo(thing):
    return 'say hi to my little friend: %s' % thing
run(home='localhost',port='8000')