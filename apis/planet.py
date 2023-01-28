from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add planet
class AddPlanet(Resource):	
    def post(self):
        try:
            new_data = Planet(bvn=request.json['bvn'],plantoexpand=request.json['plantoexpand'],crop=request.json['crop'],
        variety=request.json['variety'],raiseorbuy=request.json['raiseorbuy'],buywhere=request.json['buywhere'],
        seedlingprice=request.json['seedlingprice'],qtybought=request.json['qtybought'],degradedland=request.json['degradedland'],
        croprotation=request.json['croprotation'],season=request.json['season'],disaster=request.json['disaster'],
        burning=request.json['burning'],mill=request.json['mill'],energysource=request.json['energysource'],replacedtree=request.json['replacedtree'],
        placement=request.json['placement'],sourceofwater=request.json['sourceofwater'],covercrops=request.json['covercrops'],
        intercrop=request.json['intercrop'],cropintercropped=request.json['cropintercropped'],wastemgt=request.json['wastemgt'],
        wastedisposal=request.json['wastedisposal'],recyclewaste=request.json['recyclewaste'],suffered=request.json['suffered'],
        whensuffered=request.json['whensuffered'],greywater=request.json['greywater'],recyclegreywater=request.json['recyclegreywater'],
        pollution=request.json['pollution'],pollutionfreq=request.json['pollutionfreq'],measures=request.json['measures'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'planet{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get planet with bvn
class Planetbvn(Resource):
    def get(self, bvn):
        farmer = Planet.query.filter_by(bvn=bvn).all()
        if farmer:
            return {"error":False,"message":f'planet{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = Planet.query.filter_by(bvn=bvn).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'planet{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
  
# get all planet
class AllPlanet(Resource):
    def get(self):
        all_farmers = Planet.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'planet{retrieved}','data': all_farmers})

# with pagination
class ListPlanet(Resource):
    def get(self, limit):
        all_farmers = Planet.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))