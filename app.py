from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
def welcome():  # put application's code here
    return redirect('/login')

@app.route('/home')
def home():
    return 'Login success'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if(request.form['username'] != 'admin' or request.form['password'] != 'admin'):
            error = 'Sai thond tin dang nhap'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
