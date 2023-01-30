import numpy as np
from models import *
from flask_restx import Resource
from flask import jsonify, request
# define variables
added = " added successfully"
accepted = " accepted successfully"
rejected = " rejected successfully"
removed = " removed successfully"
updated = " updated successfully"
retrieved = " retrieved successfully"
bvnexists = "bvn already exists"
emailexists = "email already exists"
loanexists = "loan type already exists"
tidexists = "tracing id already exists"
idnotfound = "id not found"
tidnotfound = "tracing id not found"
bvnnotfound = "bvn not found"
tagnotfound = "tag not found"
cropnotfound = "crop not found"
emailnotfound = "email not found"
groupnotfound = "group not found"
statusnotfound = "status not found"
loannotfound = "loan type not found"
companynotfound = "company not found"
invalidinput = "invalid input"
missingentry = "missing field"
# define functions

# paginated lists
def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        return {"error":False,"data":[]}
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj
    
# Loan amount recommender
def applyLoan(bvn):
    try:
        crop_card = Cropcard.query.filter_by(bvn=bvn).first()
        if crop_card:
            prices = [int(crop_card.fertilizer_cost),int(crop_card.mechanization_cost),int(crop_card.labour_cost),
            int(crop_card.harvest_cost),int(crop_card.other_cost),10000] 
            price = np.median(prices)
            if price >10000:
                pass
            elif price<10000:
                pass
            else:
                price=10000
        else:
            price = 10000
        return price
    except KeyError:
        return {"error":True,"message":missingentry}
    except AssertionError:
        return {"error":True,"message":invalidinput}
    except Exception as e:
        return {"error":True,"message":e.__doc__}

class Endpoint(Resource):
    def get(self, path):
        return {"error":True,"message":f'{path} page does not exist'}
    def post(self, path):
        return {"error":True,"message":f'{path} page does not exist'}
    def put(self, path):
        return {"error":True,"message":f'{path} page does not exist'}
    def delete(self, path):
        return {"error":True,"message":f'{path} page does not exist'}