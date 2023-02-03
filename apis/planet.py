from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add planet
class AddPlanet(Resource):	
    def post(self):
        try:
            new_data = Planet(bvn=request.json['bvn'],mobile=request.json['mobile'],
            plantoexpand=request.json['plantoexpand'],crop=request.json['crop'],
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
        f'/list/limit={limit}', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get planet with mobile
class Planetmobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = Planet.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = Planet.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = Planet.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.plantoexpand=request.json['plantoexpand']
                farmer.crop=request.json['crop']
                farmer.variety=request.json['variety']
                farmer.raiseorbuy=request.json['raiseorbuy']
                farmer.buywhere=request.json['buywhere']
                farmer.seedlingprice=request.json['seedlingprice']
                farmer.qtybought=request.json['qtybought']
                farmer.degradedland=request.json['degradedland']
                farmer.croprotation=request.json['croprotation']
                farmer.season=request.json['season']
                farmer.disaster=request.json['disaster']
                farmer.burning=request.json['burning']
                farmer.mill=request.json['mill']
                farmer.energysource=request.json['energysource']
                farmer.replacedtree=request.json['replacedtree']
                farmer.placement=request.json['placement']
                farmer.sourceofwater=request.json['sourceofwater']
                farmer.covercrops=request.json['covercrops']
                farmer.intercrop=request.json['intercrop']
                farmer.cropintercropped=request.json['cropintercropped']
                farmer.wastemgt=request.json['wastemgt']
                farmer.wastedisposal=request.json['wastedisposal']
                farmer.recyclewaste=request.json['recyclewaste']
                farmer.suffered=request.json['suffered']
                farmer.whensuffered=request.json['whensuffered']
                farmer.greywater=request.json['greywater']
                farmer.recyclegreywater=request.json['recyclegreywater']
                farmer.pollution=request.json['pollution']
                farmer.pollutionfreq=request.json['pollutionfreq']
                farmer.measures=request.json['measures']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    def get(self, mobile):
        farmer = Planet.query.filter_by(mobile=mobile).all()
        if farmer:
            return {"error":False,"message":f'planet{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = Planet.query.filter_by(mobile=mobile).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'planet{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}