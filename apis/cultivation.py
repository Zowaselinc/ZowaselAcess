from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add cultivation
class AddCultivation(Resource):	
    def post(self):
        try:
            farmer = CultivationTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmercultivation = CultivationTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
                type_of_labor=request.json['type_of_labor'],
        pay_for_labor=request.json['pay_for_labor'],how_many_housechildren_help=request.json['how_many_housechildren_help'],
        season_children_help=request.json['season_children_help'],labor_children_do=request.json['labor_children_do'],
        household_vs_hire_cost=request.json['household_vs_hire_cost'],labor_women_do=request.json['labor_women_do'],
        percent_female_hired=request.json['percent_female_hired'])
                db.session.add(farmercultivation)
                db.session.commit()
                return {"error":False,"message":f'cultivation{added}',"data":farmercultivation.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get cultivation with bvn
class Cultivationbvn(Resource):
    def get(self, bvn):
        farmer = CultivationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'cultivation{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = CultivationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'cultivation{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# add all cultivation
class AllCultivation(Resource):
    def get(self):
        all_farmers = CultivationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'cultivation{retrieved}','data': all_farmers})

# with pagination 
class ListCultivation(Resource):
    def get(self, limit):
        all_farmers = CultivationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))


# get cultivation with mobile
class Cultivationmobile(Resource):
    def get(self, mobile):
        farmer = CultivationTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'cultivation{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = CultivationTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'cultivation{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}