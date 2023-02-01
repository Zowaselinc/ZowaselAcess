from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add all collateral tables at once
class AddCollateral5c(Resource):	
    def post(self):
        try:
            farmerland = FarmlandTable(bvn=request.json['bvn'],mobile=request.json['mobile'],nooffarmlands=request.json['nooffarmlands'],
        ownerorcaretaker=request.json['ownerorcaretaker'],farmownername=request.json['farmownername'],
        farmownerphoneno=request.json['farmownerphoneno'],relationshipwithowner=request.json['relationshipwithowner'],
        inheritedfrom=request.json['inheritedfrom'],sizeoffarm=request.json['sizeoffarm'],
        farmcoordinates=request.json['farmcoordinates'],farmaddress=request.json['farmaddress'],
        keepsanimals=request.json['keepsanimals'],animalsfeedon=request.json['animalsfeedon'])

            farmer = FarmlandTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                db.session.add(farmerland)
                db.session.commit()
                return {"error":False,"message":f'collateral{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
class Collateral5cbvn(Resource):
    def get(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":True, "message":f'collateral{retrieved}','data':farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
        else:
            print({"error":True,"message":bvnnotfound})
        return {"error":False,"message":f'collateral{removed}'}

class AllCollateral5c(Resource):
    def get(self):
        all_farmers = FarmlandTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return {'farmland':all_farmers}