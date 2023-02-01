from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *


# add allconditions tables at once
class AddConditions5c(Resource):	
    def post(self):
        try:
            farmercondition = ConditionsTable(bvn=request.json['bvn'],mobile=request.json['mobile'],duration=request.json['duration'],
        seller=request.json['seller'],seller_mou=request.json['seller_mou'],cropyieldprediction=0,
        cropexpectedmarketvalue=0,zowaselmarketplacepriceoffers=0)
        
            farmer = ConditionsTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                db.session.add(farmercondition)
                db.session.commit()
                return {"error":False,"message":f'Conditions{added}',"data":farmercondition.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

class Conditions5cbvn(Resource):
    def get(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'Conditions{retrieved}',"data":{'conditions':farmer.json()}}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'Conditions{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
        
   
class AllConditions5c(Resource):
    def get(self):
        all_farmers = ConditionsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return {'conditions':all_farmers}