from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add safety
class AddSafety(Resource):	
    def post(self):
        try:
            new_data = Safety(bvn=request.json['bvn'],ferment=request.json['ferment'],
        fermentdays=request.json['fermentdays'],fermentreason=request.json['fermentreason'],brokenqty=request.json['brokenqty'],
        dowithbroken=request.json['dowithbroken'],unripeqty=request.json['unripeqty'],dowithunripe=request.json['dowithunripe'],
        cocoastore=request.json['cocoastore'],ffbstore=request.json['ffbstore'],herbicide=request.json['herbicide'],
        herbicidestore=request.json['herbicidestore'],agrochemsource=request.json['agrochemsource'],harvesttool=request.json['harvesttool'],
        wear=request.json['wear'],disposal=request.json['disposal'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'safety{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get safety by bvn
class Safetybvn(Resource):
    def get(self, bvn):
        farmer = Safety.query.filter_by(bvn=bvn).all()
        if farmer:
            return {"error":False,"message":f'safety{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = Safety.query.filter_by(bvn=bvn).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'safety{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all safety
class AllSafety(Resource):
    def get(self):
        all_farmers = Safety.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'safety{retrieved}','data': all_farmers})

# with pagination
class ListSafety(Resource):
    def get(self, limit):
        all_farmers = Safety.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))