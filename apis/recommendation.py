from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add recommendation
class AddRecommendation(Resource):	
    def post(self):
        try:
            new_data = Recommendation(tracing_id=request.json['tracing_id'],rec_one=request.json['rec_one'],
        rec_two=request.json['rec_two'],rec_three=request.json['rec_three'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'recommendation{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get recommendation by id
class RecommendationTracing(Resource):
    def get(self, tracing_id):
        farmer = Recommendation.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            return {"error":False,"message":f'recommendation{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":tidnotfound}
    def delete(self, tracing_id):
        farmer = Recommendation.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'recommendation{removed}'}
        else:
            return {"error":True,"message":tidnotfound}

# get all recommendation
class AllRecommendation(Resource):
    def get(self):
        all_farmers = Recommendation.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'recommendation{retrieved}','data': all_farmers})

# with pagination
class ListRecommendation(Resource):
    def get(self, limit):
        all_farmers = Recommendation.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))