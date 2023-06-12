""" 

Latihan membuat API dengan Flask

dan Swagger UI dengan flasgger

"""

from flask import Flask, jsonify, request

from flasgger import Swagger, swag_from, LazyString, LazyJSONEncoder

import re

 

# Initiate Flask App

app = Flask(__name__)

# Assign LazyJSONEncoder to app.json_encoder for Swagger UI

app.json_encoder = LazyJSONEncoder

# Create Swagger Config & Swagger template

# Create swagger Template & Config Object

swagger_template = dict(

    info = {

        'title': LazyString(lambda:'API Data Cleansing'),

        'version': LazyString(lambda:'1.0.0'),

        'description': LazyString(lambda:'Dokumentasi Cleansing data for Gold Challenge by Aryo')

        }, 

    host = LazyString(lambda: request.host)

)

swagger_config = {

    "headers": [],

    "specs": [

        {

            "endpoint": "docs",

            "route": "/docs.json",

        }

    ],

    "static_url_path": "/flasgger_static",

    "swagger_ui": True,

    "specs_route": "/docs/"

}

# Initialize Swagger from swagger_template & swagger_config

swagger = Swagger(app, template=swagger_template, config=swagger_config)

 

@swag_from('docs/home.yml', methods=['GET'])

@app.route('/', methods=['GET'])

def home():

    welcome_msg = {

        "version": "1.0.0",

        "message": "Welcome to Flask API",

        "author": "Benedictus Aryo"

    }

    return jsonify(welcome_msg)

 

@swag_from('docs/clean_text.yml', methods=['POST'])

@app.route('/clean_text', methods=['POST'])

def clean_text():

    text = request.form['raw_text']

    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()

    # Kata kasar / abusive words

    cleaned_text = re.sub(r'anjing', '***', cleaned_text).lower()

    cleaned_text = re.sub(r'bangsat', '***', cleaned_text).lower()

    # Kamus alay

    cleaned_text = re.sub(r'gw', 'saya', cleaned_text).lower()

    cleaned_text = re.sub(r'loe', 'kamu', cleaned_text).lower()

    return jsonify(raw_text=text, cleaned_text=cleaned_text)

 

 

if __name__ == '__main__':

    app.run()

