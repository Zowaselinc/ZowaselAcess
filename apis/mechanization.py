from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add mechanization
class AddMechanization(Resource):	
    def post(self):
        try:
            farmer = MechanizationTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmermechanization = MechanizationTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
        machinesused=request.json['machinesused'],machinehashelped=request.json['machinehashelped'],
        advisemachineorlabour=request.json['advisemachineorlabour'],othermachinesneeded=request.json['othermachinesneeded'],
        canacquiremorelands=request.json['canacquiremorelands'],percentcostsaved=request.json['percentcostsaved'])
                db.session.add(farmermechanization)
                db.session.commit()
                return {"error":False,"message":f'mechanization{added}',"data":farmermechanization.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get mechanization with bvn
class Mechanizationbvn(Resource):
    def get(self, bvn):
        farmer = MechanizationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'mechanization{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = MechanizationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'mechanization{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
  
# get all mechanization
class AllMechanization(Resource):
    def get(self):
        all_farmers = MechanizationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'mechanization{retrieved}','data': all_farmers})

# with pagination
class ListMechanization(Resource):
    def get(self, limit):
        all_farmers = MechanizationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get mechanization with mobile
class Mechanizationmobile(Resource):
    def get(self, mobile):
        farmer = MechanizationTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'mechanization{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = MechanizationTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'mechanization{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}