from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *


# add Kyf
class AddFarmer(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        try:
            farmer = FarmerTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                message = {"error":True,"message":bvnexists}
            farmer = FarmerTable.query.filter_by(email=request.json['email']).first()
            if farmer:
                message = {"error":True,"message":emailexists}
            else:
                farmerkyf = FarmerTable(firstname=request.json['firstname'],surname=request.json['surname'],
        middlename=request.json['middlename'],email=request.json['email'],telephone=request.json['telephone'],
        age=request.json['age'],
        gender=request.json['gender'],language = request.json['language'],maritalstatus=request.json['maritalstatus'],
        bankname = request.json['bankname'],accountno = request.json['accountno'],bvn=request.json['bvn'],
        meansofid=request.json['meansofid'],issuedate=request.json['issuedate'],expirydate=request.json['expirydate'],
        nin=request.json['nin'],permanentaddress=request.json['permanentaddress'],landmark=request.json['landmark'],
        stateoforigin=request.json['stateoforigin'],isinagroup = request.json['isinagroup'],
        reasonnogroup = request.json['reasonnogroup'],group=request.json['group'],
        numberofmembers = request.json['numberofmembers'],firstnamenok = request.json['firstnamenok'],
        surnamenok = request.json['surnamenok'],middlenamenok = request.json['middlenamenok'], 
        relationshipnok = request.json['relationshipnok'],occupationnok     = request.json['occupationnok'],
        telephonenok  = request.json['telephonenok'],permanentaddressnok  = request.json['permanentaddressnok'],
        landmarknok  = request.json['landmarknok'],ninnok  = request.json['ninnok'])
                db.session.add(farmerkyf)
                db.session.commit()
                message = {"error":False,"message":f'farmer{added}'}
            return message
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get farmer with bvn
class Farmerbvn(Resource):
    def get(self, bvn):
        farmer = FarmerTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'farmer{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = FarmerTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'farmer{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
    
# get farmer with tag
class Farmertag(Resource):
    def get(self, tag):
        farmer = FarmerTable.query.filter_by(tag=tag).first()
        if farmer:
            return {"error":False,"message":f'farmer{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":tagnotfound}
    def delete(self, tag):
        farmer = FarmerTable.query.filter_by(tag=tag).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'farmer{removed}'}
        else:
            return {"error":True,"message":tagnotfound}
# get farmer by group
class Farmergroup(Resource):
    def get(self, group):
        farmers = FarmerTable.query.filter_by(group=group).all()
        if farmers:
            all_farmers = [farmer.json() for farmer in farmers]
            return jsonify({'error': False,'message': f'farmer{retrieved}','data': all_farmers})
        else:
            return {"error":True,"message":groupnotfound}
    def delete(self, group):
        farmers = FarmerTable.query.filter_by(group=group).all()
        if farmers:
            for farmer in farmers:
                db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'farmer{removed}'}
        else:
            return {"error":True,"message":groupnotfound}
    
# get all farmers
class AllFarmers(Resource):
    def get(self):
        all_farmers = FarmerTable.query.all()        
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'farmer{retrieved}','data': all_farmers})

# with pagination
class ListFarmers(Resource):
    def get(self, limit):
        all_farmers = FarmerTable.query.all()        
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))