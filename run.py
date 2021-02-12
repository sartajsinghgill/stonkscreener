import yfinance as yf
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stocks/<symbol>')
def getStock(symbol):
    stockName = yf.Ticker(symbol)
    return(stockName.info)
