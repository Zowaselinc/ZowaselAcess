from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add care
class AddCareTable(Resource):	
    def post(self):
        try:
            new_data = CareTable(bvn=request.json['bvn'],mobile=request.json['mobile'],healthcentloc=request.json['healthcentloc'],
        healthcentcount=request.json['healthcentcount'],healthcentdistance=request.json['healthcentdistance'],
        healthcentfunctional=request.json['healthcentfunctional'],affordable=request.json['affordable'],
        farmdistance=request.json['farmdistance'],injuryevent=request.json['injuryevent'],firstaid=request.json['firstaid'],
        lastcheck=request.json['lastcheck'],inschool=request.json['inschool'],level=request.json['level'],
        schoolcount=request.json['schoolcount'],schoolfunctional=request.json['schoolfunctional'],
        qualification=request.json['qualification'],studytime=request.json['studytime'],
        studywhere=request.json['studywhere'],altIncomesource=request.json['altIncomesource'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'care{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get care by bvn
class Carebvn(Resource):
    def get(self, bvn):
        farmer = CareTable.query.filter_by(bvn=bvn).all()
        if farmer:
            return {"error":False,"message":f'care{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = CareTable.query.filter_by(bvn=bvn).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'care{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all care
class AllCare(Resource):
    def get(self):
        all_farmers = CareTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'care{retrieved}','data': all_farmers})

# with pagination
class ListCare(Resource):
    def get(self, limit):
        all_farmers = CareTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get care by mobile
class Caremobile(Resource):
    def get(self, mobile):
        farmer = CareTable.query.filter_by(mobile=mobile).all()
        if farmer:
            return {"error":False,"message":f'care{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = CareTable.query.filter_by(mobile=mobile).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'care{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}