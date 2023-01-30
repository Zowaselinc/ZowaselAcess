from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add capacity
class AddCapacity(Resource):	
    def post(self):
        try:
            farmer = CapacityTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmercapacity = CapacityTable(bvn=request.json['bvn'],
        howlongbeenfarming=request.json['howlongbeenfarming'],participatedintraining=request.json['participatedintraining'],
        farmingpractice=request.json['farmingpractice'],keepsanimals=request.json['keepsanimals'],
        hascooperative=request.json['hascooperative'],cooperativename=request.json['cooperativename'],
        educationlevel=request.json['educationlevel'])
                db.session.add(farmercapacity)
                db.session.commit()
                return {"error":False,"message":f'capacity{added}',"data":farmercapacity.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get capacity by bvn
class Capacitybvn(Resource):
    def put(self, bvn):
        try:
            # pull row from db table
            farmer = FarmerTable.query.filter_by(bvn=bvn).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":bvnnotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = FarmerTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # assign other fields
                farmer.howlongbeenfarming=request.json['howlongbeenfarming']
                farmer.participatedintraining=request.json['participatedintraining']
                farmer.farmingpractice=request.json['farmingpractice']
                farmer.keepsanimals=request.json['keepsanimals']
                farmer.hascooperative=request.json['hascooperative']
                farmer.cooperativename=request.json['cooperativename']
                farmer.educationlevel=request.json['educationlevel']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    def get(self, bvn):
        farmer = CapacityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'capacity{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = CapacityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'capacity{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all capacity
class AllCapacity(Resource):
    def get(self):
        all_farmers = CapacityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'capacity{retrieved}','data': all_farmers})

# with pagination
class ListCapacity(Resource):
    def get(self, limit):
        all_farmers = CapacityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

