from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '292ef1b0413859709s4570746a11e58d'

channels = [
    {
        "content" : "Test 2"
    },
    {
        "content" : "Test 1"
    }
]

classes = [
    {
        "name" : "Rocky river",
        "imgurl" : "https://www.w3schools.com/w3images/rocks.jpg"
    },
    {
        "name" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam, molestias!",
        "imgurl" : "https://www.w3schools.com/w3images/paris.jpg"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', channels=channels, classes=classes)

#runs the app w/ debug (auto update)
if __name__ == '__main__':
    app.run(debug=True, port=8089)