from flask import Flask,request

app = Flask(__name__)

@app.route('/greet/<name>')
@app.route('/greet',defaults = {"name":"小秋哥"})
def index(name):
    return "hello," + name


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])