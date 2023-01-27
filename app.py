# Import flask 
from flask import Flask, jsonify, request, Blueprint, current_app
from flask_cors import CORS,cross_origin
from flask_sqlalchemy import SQLAlchemy
#from flask_restplus import Resource, Api, fields
from flask_restx import Api, Resource
from flask_mysqldb import MySQL
from models import *
from apis.loans import * 
import csv
import io
from io import StringIO


import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask_migrate import Migrate
import numpy as np
import pandas as pd
import pickle
from modelExample import preprocess_df, bin_target
from apis import blueprint as api_blueprint


Migrate(app,db)
app.config['CORS_HEADERS'] = 'Content-Type'


app.register_blueprint(api_blueprint, url_prefix="/api")
# Running app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
