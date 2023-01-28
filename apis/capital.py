from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add capital
class AddCapital(Resource):	
    def post(self):
        try:
            farmer = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmercapital = CapitalTable(bvn=request.json['bvn'],mainincomesource=request.json['mainincomesource'],
        otherincomesource=request.json['otherincomesource'],noofincomeearners=request.json['noofincomeearners'],
        hasbankaccount=request.json['hasbankaccount'],firstfundingoption=request.json['firstfundingoption'],
        needsaloan=request.json['needsaloan'],paybackmonths=request.json['paybackmonths'],
        harvestqtychanged=request.json['harvestqtychanged'],pestexpensechanged=request.json['pestexpensechanged'])
                db.session.add(farmercapital)
                db.session.commit()
                return {"error":False,"message":f'capital{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get capital by bvn
class Capitalbvn(Resource):
    def get(self, bvn):
        farmer = CapitalTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'capital{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = CapitalTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'capital{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all capital 
class AllCapital(Resource):
    def get(self):
        all_farmers = CapitalTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'capital{retrieved}','data': all_farmers})

# with pagination
class ListCapital(Resource):
    def get(self, limit):
        all_farmers = CapitalTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))