import yfinance as yf
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stonks/<symbol>')
def getStonk(symbol):
    stonkName = yf.Ticker(symbol)
    return(stonkName.info)
