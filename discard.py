from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '292ef1b0413859709s4570746a11e58d'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

"""
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
"""
#runs the app w/ debug (auto update)
if __name__ == '__main__':
    app.run(debug=True, port=8089)