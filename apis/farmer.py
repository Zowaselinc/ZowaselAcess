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
    def put(self, bvn):
        try:
            # pull row from db table
            farmer = FarmerTable.query.filter_by(bvn=bvn).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":bvnnotfound}
            # if found, validate new values
            if farmer:
                # validate new email
                if farmer.email != request.json['email']:
                    checkdup = FarmerTable.query.filter_by(email=request.json['email']).first()
                    if checkdup:
                        return {"error":True,"message":emailexists}
                    else:
                        farmer.email=request.json['email']
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = FarmerTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # assign other fields
                farmer.meansofid=request.json['meansofid']
                farmer.firstname=request.json['firstname']
                farmer.telephone=request.json['telephone']
                farmer.age=request.json['age']
                farmer.gender=request.json['gender']
                farmer.language = request.json['language']
                farmer.maritalstatus=request.json['maritalstatus']
                farmer.bankname = request.json['bankname']
                farmer.accountno = request.json['accountno']
                farmer.surname=request.json['surname']
                farmer.middlename=request.json['middlename']
                farmer.issuedate=request.json['issuedate']
                farmer.expirydate=request.json['expirydate']
                farmer.nin=request.json['nin']
                farmer.permanentaddress=request.json['permanentaddress']
                farmer.landmark=request.json['landmark']
                farmer.stateoforigin=request.json['stateoforigin']
                farmer.isinagroup = request.json['isinagroup']
                farmer.reasonnogroup = request.json['reasonnogroup']
                farmer.group=request.json['group']
                farmer.numberofmembers = request.json['numberofmembers']
                farmer.firstnamenok = request.json['firstnamenok']
                farmer.surnamenok = request.json['surnamenok']
                farmer.middlenamenok = request.json['middlenamenok']
                farmer.relationshipnok = request.json['relationshipnok']
                farmer.occupationnok     = request.json['occupationnok']
                farmer.telephonenok  = request.json['telephonenok']
                farmer.permanentaddressnok  = request.json['permanentaddressnok']
                farmer.landmarknok  = request.json['landmarknok']
                farmer.ninnok  = request.json['ninnok']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
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
    def put(self, tag):
        try:
            # pull row from db table
            farmer = FarmerTable.query.filter_by(tag=tag).first()
            # return error, if farmer not found
            if not farmer:
                return {"error":True,"message":tagnotfound}
            # if found, validate new values
            if farmer:
                # validate email
                if farmer.email != request.json['email']:
                    checkdup = FarmerTable.query.filter_by(email=request.json['email']).first()
                    if checkdup:
                        return {"error":True,"message":emailexists}
                    else:
                        farmer.email=request.json['email']
                # validate bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = FarmerTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # assign other fields
                farmer.meansofid=request.json['meansofid']
                farmer.firstname=request.json['firstname']
                farmer.surname=request.json['surname']
                farmer.middlename=request.json['middlename']
                farmer.issuedate=request.json['issuedate']
                farmer.expirydate=request.json['expirydate']
                farmer.nin=request.json['nin']
                farmer.telephone=request.json['telephone']
                farmer.age=request.json['age']
                farmer.gender=request.json['gender']
                farmer.language = request.json['language']
                farmer.maritalstatus=request.json['maritalstatus']
                farmer.bankname = request.json['bankname']
                farmer.accountno = request.json['accountno']
                farmer.permanentaddress=request.json['permanentaddress']
                farmer.landmark=request.json['landmark']
                farmer.stateoforigin=request.json['stateoforigin']
                farmer.isinagroup = request.json['isinagroup']
                farmer.reasonnogroup = request.json['reasonnogroup']
                farmer.group=request.json['group']
                farmer.numberofmembers = request.json['numberofmembers']
                farmer.firstnamenok = request.json['firstnamenok']
                farmer.surnamenok = request.json['surnamenok']
                farmer.middlenamenok = request.json['middlenamenok']
                farmer.relationshipnok = request.json['relationshipnok']
                farmer.occupationnok     = request.json['occupationnok']
                farmer.telephonenok  = request.json['telephonenok']
                farmer.permanentaddressnok  = request.json['permanentaddressnok']
                farmer.landmarknok  = request.json['landmarknok']
                farmer.ninnok  = request.json['ninnok']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
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