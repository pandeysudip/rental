from flask import Flask, request, render_template, redirect, jsonify
import json
import os
import model_param
from bson import json_util
from pymongo import MongoClient
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', '')
app.config['MONG_DBNAME'] = 'ca_rent'
mongo = PyMongo(app)

# Creating collection
rent = mongo.db['rent']

# Defining routes


@app.route('/')
def home():
    # Return the template
    return render_template('index.html')


@app.route('/index.html')
def index():
    # Return the template
    return render_template('index.html')


@app.route('/plots.html')
def figure():
    # Store the entire collection as a list

    # Return the template
    return render_template('plots.html')


@app.route('/model.html')
def model():
    # Store the entire collection as a list
    # Return the template
    return render_template('model.html')


@app.route('/maps.html')
def plot():
    # Store the entire collection as a list
    # Return the template
    return render_template('maps.html')


@app.route('/contact.html')
def contact():
    # Return the template
    return render_template('contact.html')


@app.route('/rent', methods=["GET", "POST"])
def predic():
    if request.method == "POST":
        Age = request.form.get('Age')
        Rent_Amount = request.form.get("Rent_Amount")
        Payment_Amount = request.form.get('Payment_Amount')
        Payment_Date = request.form.get('Payment_Date')
        variables = [Age, Rent_Amount,
                     Payment_Amount, Payment_Date]
        predict = model_param.loading_model(variables)
        return render_template("index.html", pred=variables, prediction=predict)
    else:
        return render_template("index.html")


@app.route('/data.html')
def data():
    # Return the template
    return render_template('data.html')


@ app.route("/data/all_data")
def get_data():
    all_data_list = list(rent.find())
    return json.dumps(all_data_list, default=json_util.default)


if __name__ == "__main__":
    app.run(debug=True)
