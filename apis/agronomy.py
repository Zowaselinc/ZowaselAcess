from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add agronomy
class AddAgronomyServices(Resource):	
    def post(self):
        try:
            farmer = AgronomyServicesTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            farmer = AgronomyServicesTable.query.filter_by(mobile=request.json['mobile']).first()
            if farmer:
                return {"error":True,"message":mobileexists}
            else:
                farmeragronomy = AgronomyServicesTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
        knowsagriprocessed=request.json['knowsagriprocessed'],agronomistthattrainedyou=request.json['agronomistthattrainedyou'],
        canmanageecosystem=request.json['canmanageecosystem'],howtomanageecosystem=request.json['howtomanageecosystem'],
        istrainingbeneficial=request.json['istrainingbeneficial'],fieldroutines=request.json['fieldroutines'],
        harvestingchanges=request.json['harvestingchanges'],iscropcalendarbeneficial=request.json['iscropcalendarbeneficial'],
        cropcalendarbenefits=request.json['cropcalendarbenefits'],recordkeepingbenefits=request.json['recordkeepingbenefits'])
                db.session.add(farmeragronomy)
                db.session.commit()
                return {"error":False,"message":f'agronomy{added}',"data":farmeragronomy.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get agronomy by bvn
class Agronomybvn(Resource):
    def put(self, bvn):
        try:
            # pull row from db table
            farmer = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":bvnnotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = AgronomyServicesTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = AgronomyServicesTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.knowsagriprocessed=request.json['knowsagriprocessed']
                farmer.agronomistthattrainedyou=request.json['agronomistthattrainedyou']
                farmer.canmanageecosystem=request.json['canmanageecosystem']
                farmer.howtomanageecosystem=request.json['howtomanageecosystem']
                farmer.istrainingbeneficial=request.json['istrainingbeneficial']
                farmer.fieldroutines=request.json['fieldroutines']
                farmer.harvestingchanges=request.json['harvestingchanges']
                farmer.iscropcalendarbeneficial=request.json['iscropcalendarbeneficial']
                farmer.cropcalendarbenefits=request.json['cropcalendarbenefits']
                farmer.recordkeepingbenefits=request.json['recordkeepingbenefits']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    def get(self, bvn):
        farmer = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'agronomy{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'agronomy{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all agronomy
class AllAgronomy(Resource):
    def get(self):
        all_farmers = AgronomyServicesTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'agronomy{retrieved}','data': all_farmers})
        
# with pagination
class ListAgronomy(Resource):
    def get(self, limit):
        all_farmers = AgronomyServicesTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get agronomy by mobile
class Agronomymobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = AgronomyServicesTable.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = AgronomyServicesTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = AgronomyServicesTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.knowsagriprocessed=request.json['knowsagriprocessed']
                farmer.agronomistthattrainedyou=request.json['agronomistthattrainedyou']
                farmer.canmanageecosystem=request.json['canmanageecosystem']
                farmer.howtomanageecosystem=request.json['howtomanageecosystem']
                farmer.istrainingbeneficial=request.json['istrainingbeneficial']
                farmer.fieldroutines=request.json['fieldroutines']
                farmer.harvestingchanges=request.json['harvestingchanges']
                farmer.iscropcalendarbeneficial=request.json['iscropcalendarbeneficial']
                farmer.cropcalendarbenefits=request.json['cropcalendarbenefits']
                farmer.recordkeepingbenefits=request.json['recordkeepingbenefits']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    def get(self, mobile):
        farmer = AgronomyServicesTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'agronomy{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = AgronomyServicesTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'agronomy{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}