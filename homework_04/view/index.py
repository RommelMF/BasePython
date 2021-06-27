from flask import Blueprint, request, jsonify, render_template, url_for, redirect


index_app = Blueprint('index_app', __name__, url_prefix='/')

@index_app.route("/about/", endpoint='about')
def about():
    return render_template('index/about.html')

@index_app.route("/", endpoint='home')
def home():
    return render_template('index/base.html')
