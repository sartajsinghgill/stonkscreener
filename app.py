import yfinance as yf
import json

from flask import Flask
from flask import render_template
app = Flask(__name__)

# Default route will render index.html that is located in the templates/ folder
@app.route('/')
def index():
    return render_template("index.html")

# /stonks/symbol route will take the symbol that is passed to the route and use that as a query parameter for the yfinance API and return the stock information
@app.route('/stonks/<symbol>')
def getStonk(symbol):
    return(getStockDataFromYF(symbol).info)

@app.route('/stonks/<symbol>/history')
def getStonkHistory(symbol):
    json_data = json.loads(getStockDataFromYF(symbol).history().to_json(orient="records"))
    return json_data[0]

def getStockDataFromYF(symbol):
    stonkName = yf.Ticker(symbol)
    return stonkName