from crypt import methods
from decimal import Decimal
from locale import currency
from symtable import Symbol
from unicodedata import decimal
from unittest import result
from flask import Flask, redirect,render_template,flash, request,session
from forex_python.converter import CurrencyRates,CurrencyCodes
from flask_debugtoolbar import DebugToolbarExtension
import requests
from currency import Currencies


app=Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def start_converter():
    """show the converter page"""
    session["Responses"] = []

    return render_template("start_converter.html")


currency_c = Currencies()

@app.route("/result")
def convert():
    """show the converted currency"""

    from_cur =  currency_c.check_valid_from(request.args.get('from'))

    to_cur = currency_c.check_valid_to(request.args.get('to'))
    symbol = currency_c.get_symbol(to_cur)


    while True:
        try:
            amount = float(request.args['amount'])
            result = currency_c.converter(from_cur,to_cur,amount)

            break
        except ValueError:
            flash("Oops!  That was no valid number.  Try again...", "error")
            return redirect('/')
        except:
            msg = "Oops!  That was no valid code. Try exp EUR"
            flash(msg,"error")
            return redirect('/')
        
    return render_template("converted.html",from_cur=from_cur, to_cur=to_cur, result=result, symbol=symbol)


@app.route('/return-home')
def return_home():
    """Return back home from result page"""

    return redirect('/')
