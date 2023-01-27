from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add capacity
class AddCapacity(Resource):	
    def post(self):
        try:
            farmer = CapacityTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmercapacity = CapacityTable(bvn=request.json['bvn'],
        howlongbeenfarming=request.json['howlongbeenfarming'],participatedintraining=request.json['participatedintraining'],
        farmingpractice=request.json['farmingpractice'],keepsanimals=request.json['keepsanimals'],
        hascooperative=request.json['hascooperative'],cooperativename=request.json['cooperativename'],
        educationlevel=request.json['educationlevel'])
                db.session.add(farmercapacity)
                db.session.commit()
                return {"error":False,"message":f'capacity{added}',"data":farmercapacity.json()}
        except KeyError:
            return {"error":True,"message":missingentry}

# get capacity by bvn
class Capacitybvn(Resource):
    def get(self, bvn):
        farmer = CapacityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'capacity{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = CapacityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'capacity{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all capacity
class AllCapacity(Resource):
    def get(self):
        all_farmers = CapacityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'capacity{retrieved}','data': all_farmers})

# with pagination
class ListCapacity(Resource):
    def get(self, limit):
        all_farmers = CapacityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

