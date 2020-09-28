from bottle import request, response, static_file
from bottle import get, route
from api.fn import parse, modify
import json
import os
import time


@route('/')
def root():
    return static_file('test.html', root='.')


@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('filename')
    # name, ext = os.path.splitext(upload.filename)

    save_path = "./tmp/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    timing = int(time.time())
    file_path = "{path}{time}_{filename}".format(path=save_path, time=timing, filename=upload.filename)
    upload.save(file_path)
    return parse.list_maker(file_path), file_path


@get('/call')
def listing_handler():
    '''Get buttons from default index.html'''

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return parse.list_maker('index.html')


@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='/path/to/static/files', download=filename)


@get('/modify', method='POST')
def modify(filename):
    '''Modify index.html with selected parameters'''

    response.headers['Content-Type'] = 'application/json'
    postdata = request.body.read()

    res = modify(postdata, filename)
    return {"success": True}, res
