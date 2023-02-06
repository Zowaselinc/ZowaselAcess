from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add inputs info
class AddInputsInfo(Resource):	
    def post(self):
        try:
            new_data = InputsInfo(tracing_id=request.json['tracing_id'],fertilizers=request.json['fertilizers'],herbicides=request.json['herbicides'],
        fungicides=request.json['fungicides'],insecticides=request.json['insecticides'],seeds=request.json['seeds'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'inputs{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get inputs info id
class InputsInfoTracing(Resource):
    def put(self, tracing_id):
        try:
            # pull row from db table
            farmer = InputsInfo.query.filter_by(tracing_id=tracing_id).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":tidnotfound}
            # if found, validate new values
            if farmer:
                # validate new tracing_id
                if farmer.tracing_id != request.json['tracing_id']:
                    checkdup = InputsInfo.query.filter_by(tracing_id=request.json['tracing_id']).first()
                    if checkdup:
                        return {"error":True,"message":tidexists}
                    else:
                        farmer.tracing_id=request.json['tracing_id']
                # assign other fields
                farmer.fertilizers=request.json['fertilizers']
                farmer.herbicides=request.json['herbicides']
                farmer.fungicides=request.json['fungicides']
                farmer.insecticides=request.json['insecticides']
                farmer.seeds=request.json['seeds']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    
    def get(self, tracing_id):
        farmer = InputsInfo.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            return {"error":False,"message":f'inputs{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":tidnotfound}
    def delete(self, tracing_id):
        farmer = InputsInfo.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'inputs{removed}'}
        else:
            return {"error":True,"message":tidnotfound}

# get all inputs info
class AllInputsInfo(Resource):
    def get(self):
        all_farmers = InputsInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'inputs{retrieved}','data': all_farmers})

# with pagination
class ListInputsInfo(Resource):
    def get(self, limit):
        all_farmers = InputsInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
