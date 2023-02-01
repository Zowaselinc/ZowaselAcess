from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add harvest
class AddHarvest(Resource):	
    def post(self):
        try:
            farmer = HarvestTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmerharvest = HarvestTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
                when_is_harvest_season=request.json['when_is_harvest_season'],
        no_of_hired_workers=request.json['no_of_hired_workers'],no_of_family_workers=request.json['no_of_family_workers'],
        no_of_permanent_workers=request.json['no_of_permanent_workers'],no_hired_constantly=request.json['no_hired_constantly'])
                db.session.add(farmerharvest)
                db.session.commit()
                return {"error":False,"message":f'harvest{added}',"data":farmerharvest.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get harvest by bvn
class Harvestbvn(Resource):
    def get(self, bvn):
        farmer = HarvestTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'harvest{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = HarvestTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'harvest{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
    
# get all harvest
class AllHarvest(Resource):
    def get(self):
        all_farmers = HarvestTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'harvest{retrieved}','data': all_farmers})

# with pagination
class ListHarvest(Resource):
    def get(self, limit):
        all_farmers = HarvestTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
# get harvest by mobile
class Harvestmobile(Resource):
    def get(self, mobile):
        farmer = HarvestTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'harvest{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = HarvestTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'harvest{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}