from flask import Flask, render_template, request, redirect

app = Flask(__name__)
data = {}

@app.route('/')
def home():
    return 'Welcome to the Flask App!'


@app.route('/greet')
def greet():
    username = request.args.get('username') # passing query /greet?username="Raj"
    if username:
        return f'Hello, {username}!'
    else:
        return 'Please provide a username.'


@app.route('/farewell/<username>')      # passing params
def farewell(username):
    return f'Goodbye, {username}!'


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        return redirect('/read')
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', data=data)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in data:
            data[key] = value
            return redirect('/read')
        else:
            return 'Key does not exist.'
    return render_template('update.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return redirect('/read')
        else:
            return 'Key does not exist.'
    return render_template('delete.html')

if __name__ == '__main__':
    app.run()
