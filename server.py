from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='secret'
counter = 1
@app.route('/', methods=['get'])
def index():
    if session==None:
        session['counter']=counter
    session['counter']=session['counter'] +1
    print(session['counter'])
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    if request.form['button'] == 'counter':
        session['counter']=session['counter']+1
    return redirect('/')

@app.route('/reset', methods=['GET'])
def reset():
    session['counter'] = -1
    return redirect('/')
@app.route('/destroy_session')
def destroy():
    session.clear()
    return render_template('index.html', counter=0 )
if __name__=="__main__":
    app.run(debug=True)