from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add conditions
class AddConditions(Resource):	
    def post(self):
        try:
            farmercondition = ConditionsTable(bvn=request.json['bvn'],mobile=request.json['mobile'],duration=request.json['duration'],
        seller=request.json['seller'],seller_mou=request.json['seller_mou'],cropyieldprediction=request.json['cropyieldprediction'],
        cropexpectedmarketvalue=request.json['cropexpectedmarketvalue'],zowaselmarketplacepriceoffers=request.json['zowaselmarketplacepriceoffers'])
        
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

# get condition by bvn
class Conditionsbvn(Resource):
    def get(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'Conditions{retrieved}',"data":farmer.json()}
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
    
# get all conditions
class AllConditions(Resource):
    def get(self):
        all_farmers = ConditionsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

# with pagination
class ListConditions(Resource):
    def get(self, limit):
        all_farmers = ConditionsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get condition by mobile
class Conditionsmobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = ConditionsTable.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = ConditionsTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = ConditionsTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.duration=request.json['duration']
                farmer.seller=request.json['seller']
                farmer.seller_mou=request.json['seller_mou']
                farmer.cropyieldprediction=request.json['cropyieldprediction']
                farmer.cropexpectedmarketvalue=request.json['cropexpectedmarketvalue']
                farmer.zowaselmarketplacepriceoffers=request.json['zowaselmarketplacepriceoffers']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    
    def get(self, mobile):
        farmer = ConditionsTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'Conditions{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, mobile):
        farmer = ConditionsTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'Conditions{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}