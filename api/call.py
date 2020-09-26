from bottle import request, response, static_file
from bottle import get, route
from api.fn import parse
import os
import time


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


@route('/')
def root():
    return static_file('test.html', root='.')

@route('/upload', method='POST')
@enable_cors
def do_upload():
    upload = request.files.get('filename')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.html'):
        return "File extension not allowed."

    save_path = "./tmp/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    timing = int(time.time())
    file_path = "{path}{file}_{time}{ext}".format(path=save_path, file=upload.name,  ext=ext, time=timing)
    upload.save(file_path)
    return parse.list_maker(file_path)


@get('/call')
def listing_handler():
    '''Get buttons from default index.html'''

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return parse.list_maker('api/fn/index.html')
