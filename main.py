import bottle
from api import call

app = application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host = '127.0.0.1', port = 5000)