from flask import Flask

app = Flask(__name__)

app.debug = True
app.secret_key = 'development key'


from app import routes


if __name__ == '__main__':
    app.run(debug=True)