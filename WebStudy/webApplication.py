import bottle
application=bottle.default_app()
@bottle.route('/')
def home():
    return static_file('index.html',root='WebStudy')
@bottle.route('/echo/<thing>')
def echo(thing):
    return 'say hi to my little friend: %s' % thing