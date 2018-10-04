from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='secret'
@app.route('/')
def index():
    counter = 1
    session['counter'] += counter
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    if request.form['button'] == 'counter':
        session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    if request.form['button'] == 'reset':
        session['counter'] = 0
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)