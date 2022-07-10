from crypt import methods
from decimal import Decimal
from symtable import Symbol
from unicodedata import decimal
from unittest import result
from flask import Flask, redirect,render_template,flash, request,session
from forex_python.converter import CurrencyRates,CurrencyCodes
from flask_debugtoolbar import DebugToolbarExtension
import requests


app=Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# c = CurrencyRates()
# c.get_rate('USD', 'ISK')
# c.convert('USD','ISK', 10)
# c.get_rates('USD')

@app.route("/")
def start_converter():
    """show the converter page"""
    session["Responses"] = []

    return render_template("start_converter.html")




@app.route("/result", methods=["POST"])
def convert():
    """show the converted currency"""
    # input = session['input']

    c = CurrencyRates()
    cs = CurrencyCodes()

    
    from_cur = (request.form.get('from')).upper()
    to_cur = (request.form.get('to')).upper()
    symbol = cs.get_symbol(to_cur)



    # str_amount = isinstance(amount, str)

    while True:
        try:
            amount = float(request.form['amount'])
            from_cur = (request.form.get('from')).upper()
            to_cur = (request.form.get('to')).upper()
            res = c.convert(from_cur,to_cur, amount)
            result = round(res,2)

            break
        except ValueError:
            flash("Oops!  That was no valid number.  Try again...", "error")
            return redirect('/')
        except:
            flash("Oops!  That was no valid code.","error")
            return redirect('/')
        
    # result = c.convert(from_cur,to_cur, amount)

    return render_template("converted.html",from_cur=from_cur, to_cur=to_cur, result=result, symbol=symbol)


@app.route('/return-home')
def return_home():
    """Return back home from result page"""

    return redirect('/')
