from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add farmland data
class AddFarmlandData(Resource):	
    def post(self):
        try:
            farmer = FarmlandTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmerland = FarmlandTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
                nooffarmlands=request.json['nooffarmlands'],
        ownerorcaretaker=request.json['ownerorcaretaker'],farmownername=request.json['farmownername'],
        farmownerphoneno=request.json['farmownerphoneno'],relationshipwithowner=request.json['relationshipwithowner'],
        inheritedfrom=request.json['inheritedfrom'],sizeoffarm=request.json['sizeoffarm'],
        farmcoordinates=request.json['farmcoordinates'],farmaddress=request.json['farmaddress'],
        keepsanimals=request.json['keepsanimals'],animalsfeedon=request.json['animalsfeedon'])
                db.session.add(farmerland)
                db.session.commit()
                return {"error":False,"message":f'farmland{added}',"data":farmerland.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get farmland by bvn
class Farmlandbvn(Resource):
    def get(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'farmland{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":added}
        else:
            return {"error":True,"message":bvnnotfound}
    
# get all farmland
class AllFarmland(Resource):
    def get(self):
        all_farmers = FarmlandTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'farmland{retrieved}','data': all_farmers})

# with pagination
class ListFarmland(Resource):
    def get(self, limit):
        all_farmers = FarmlandTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get farmland by mobile
class Farmlandmobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = FarmlandTable.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = FarmlandTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = FarmlandTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.nooffarmlands=request.json['nooffarmlands']
                farmer.ownerorcaretaker=request.json['ownerorcaretaker']
                farmer.farmownername=request.json['farmownername']
                farmer.farmownerphoneno=request.json['farmownerphoneno']
                farmer.relationshipwithowner=request.json['relationshipwithowner']
                farmer.inheritedfrom=request.json['inheritedfrom']
                farmer.sizeoffarm=request.json['sizeoffarm']
                farmer.farmcoordinates=request.json['farmcoordinates']
                farmer.farmaddress=request.json['farmaddress']
                farmer.keepsanimals=request.json['keepsanimals']
                farmer.animalsfeedon=request.json['animalsfeedon']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    
    
    def get(self, mobile):
        farmer = FarmlandTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'farmland{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = FarmlandTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":added}
        else:
            return {"error":True,"message":mobilenotfound}