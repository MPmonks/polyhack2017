from flask import render_template
from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/app.js')
def appjs():
	return app.send_static_file('app.js')

"""
@app.route('/name')
def name():
    user = {'nickname': 'Samsam'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
"""

@app.route('/give', methods=['POST'])
def give():
	f = open('test', 'w')
	f.write(request.get_data())
	f.close()
	return ""
