from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add productivity
class AddProductivityViability(Resource):
    def post(self):
        try:
            farmer = ProductivityViabilityTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmerproductivity = ProductivityViabilityTable(bvn=request.json['bvn'],
        cropscultivated=request.json['cropscultivated'],growscrops=request.json['growscrops'],
        oilpalmfertilizers=request.json['oilpalmfertilizers'],cocoafertilizers=request.json['cocoafertilizers'],
        fertilizerfrequency=request.json['fertilizerfrequency'],pestfungherbicides=request.json['pestfungherbicides'],
        stagechemicalapplied=request.json['stagechemicalapplied'],noofoildrums=request.json['noofoildrums'],
        noofbagssesame=request.json['noofbagssesame'],noofbagssoyabeans=request.json['noofbagssoyabeans'],
        noofbagsmaize=request.json['noofbagsmaize'],noofbagssorghum=request.json['noofbagssorghum'],
        noofbagscocoabeans=request.json['noofbagscocoabeans'],croptrainedon=request.json['croptrainedon'],
        wherewhenwhotrained=request.json['wherewhenwhotrained'],nooftraining=request.json['nooftraining'],
        pruningfrequency=request.json['pruningfrequency'],cropbasedproblems=request.json['cropbasedproblems'],
        tooyoungcrops=request.json['tooyoungcrops'],youngcropsandstage=request.json['youngcropsandstage'],
        cultivationstartdate=request.json['cultivationstartdate'],isintensivefarmingpractised=request.json['isintensivefarmingpractised'],
        economicactivities=request.json['economicactivities'])
                db.session.add(farmerproductivity)
                db.session.commit()
                return {"error":False,"message":f'productivity{added}',"data":farmerproductivity.json()}
        except KeyError:
            return {"error":True,"message":missingentry}

# get productivity with bvn
class Productivitybvn(Resource):
    def get(self, bvn):
        farmer = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'productivity{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'productivity{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
  
# get all productivity
class AllProductivity(Resource):
    def get(self):
        all_farmers = ProductivityViabilityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'productivity{retrieved}','data': all_farmers})

# with pagination
class ListProductivity(Resource):
    def get(self, limit):
        all_farmers = ProductivityViabilityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))