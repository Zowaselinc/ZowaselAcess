from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add score analytics
class AddScoreAnalytics(Resource):	
    def post(self):
        try:
            new_data = ScoreAnalytics(bvn=request.json['bvn'],scores=request.json['scores'],
        conditions=request.json['conditions'],capital=request.json['capital'],collateral=request.json['collateral'],
        capacity=request.json['capacity'],character=request.json['character'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'scoreanalysis{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}

# get score analytics
class ScoreAnalyticsbvn(Resource):
    def get(self, bvn):
        farmer = ScoreAnalytics.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'scoreanalysis{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = ScoreAnalytics.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'scoreanalysis{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
    
# get all score analytics
class AllScoreAnalytics(Resource):
    def get(self):
        all_farmers = ScoreAnalytics.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'scoreanalysis{retrieved}','data': all_farmers})

# with pagination
class ListScoreAnalytics(Resource):
    def get(self, limit):
        all_farmers = ScoreAnalytics.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))



