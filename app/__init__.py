from flask import Flask

app = Flask(__name__)

from app import views

app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)