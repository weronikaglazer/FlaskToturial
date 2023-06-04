from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/name/<name>')
@app.route('/name')
def name(name = "World"):
    return render_template("name.html", name=name)

@app.route("/products")
def cat():
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()
    return render_template("products.html", products=products)