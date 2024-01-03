from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello world!'

@app.route('/bye')
def bye():
    return 'bye world!'

if __name__ == '__main__':
    app.run(debug=True)
