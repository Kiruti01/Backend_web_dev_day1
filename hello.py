from flask import Flask

app = Flask(__name__)

print(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return "<h1 style='text-align: center' >status success</h1>" \
           "<p>This is a paragragh.</p>" \
           "<img src='https://media.giphy.com/media/11s7Ke7jcNxCHS/giphy.gif' width=500px>"

# creating variable paths and converting the path into data
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return "Bye"

if __name__ == '__main__':
    app.run(debug=True)
