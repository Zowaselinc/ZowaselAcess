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
            else:
                farmeragronomy = AgronomyServicesTable(bvn=request.json['bvn'],
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
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))