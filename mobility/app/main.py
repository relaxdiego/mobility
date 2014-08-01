# ===========================
# BORING, INITIALIZATION BITS
# ===========================

# This uses the Flask library to
# instantiate a simple web server
# http://flask.pocoo.org/
from flask import Flask
from flask import render_template
import os
import sys

path = os.path.abspath(os.path.dirname(__file__) + '/' + '../..')
sys.path.append(path)

from mobility.framework.mse import MSE

app = Flask(__name__)


# =====================
# WRITE YOUR CODE BELOW
# =====================


@app.route('/')
def home():
    # The actual template is in mobility/app/templates/home.html
    return render_template('home.html')


@app.route('/get_maps')
def get_maps():
    # See mobility/framework/mse.py for information on
    # how the MSE class is implemented
    mse = MSE()

    # The return value of mse.get('maps') will be available
    # to the maps.html template as the variable 'maps'
    return render_template('maps.html', maps=mse.get('maps'))


# =====================
# WRITE YOUR CODE ABOVE
# =====================

if __name__ == "__main__":
    app.debug = True
    app.run()
