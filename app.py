from flask import Flask,render_template,request,url_for

import os


app = Flask('__name__')
#stop cache static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Python','Flask']
    name = 'Challenge Me!'
    return render_template('home.html', techs=techs, name=name,title='Home')

@app.route('/about')
def about():
    name = 'Locj Web Flask'
    return render_template('about.html',name=name, title='About us')


@app.route('/post', methods=['GET','POST'])
def post():
    if request.method == 'GET':
        name = 'Text Analyzer'
        return render_template('post.html',name= name, title= name)
    if request.method == 'POST':
        return '<h1>This is post handler<h1>'

if(__name__ == '__main__'):
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True,host='localhost', port=port)

