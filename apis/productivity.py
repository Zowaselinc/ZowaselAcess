from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add productivity
class AddProductivityViability(Resource):
    def post(self):
        try:
            farmer = ProductivityViabilityTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmerproductivity = ProductivityViabilityTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
        cropscultivated=request.json['cropscultivated'],growscrops=request.json['growscrops'],
        oilpalmfertilizers=request.json['oilpalmfertilizers'],cocoafertilizers=request.json['cocoafertilizers'],
        fertilizerfrequency=request.json['fertilizerfrequency'],pestfungherbicides=request.json['pestfungherbicides'],
        stagechemicalapplied=request.json['stagechemicalapplied'],noofoildrums=request.json['noofoildrums'],
        noofbagssesame=request.json['noofbagssesame'],noofbagssoyabeans=request.json['noofbagssoyabeans'],
        noofbagsmaize=request.json['noofbagsmaize'],noofbagssorghum=request.json['noofbagssorghum'],
        noofbagscocoabeans=request.json['noofbagscocoabeans'],croptrainedon=request.json['croptrainedon'],
        wherewhenwhotrained=request.json['wherewhenwhotrained'],nooftraining=request.json['nooftraining'],
        pruningfrequency=request.json['pruningfrequency'],cropbasedproblems=request.json['cropbasedproblems'],
        tooyoungcrops=request.json['tooyoungcrops'],youngcropsandstage=request.json['youngcropsandstage'],
        cultivationstartdate=request.json['cultivationstartdate'],isintensivefarmingpractised=request.json['isintensivefarmingpractised'],
        economicactivities=request.json['economicactivities'])
                db.session.add(farmerproductivity)
                db.session.commit()
                return {"error":False,"message":f'productivity{added}',"data":farmerproductivity.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get productivity with bvn
class Productivitybvn(Resource):
    def get(self, bvn):
        farmer = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'productivity{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'productivity{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
  
# get all productivity
class AllProductivity(Resource):
    def get(self):
        all_farmers = ProductivityViabilityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'productivity{retrieved}','data': all_farmers})

# with pagination
class ListProductivity(Resource):
    def get(self, limit):
        all_farmers = ProductivityViabilityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get productivity with mobile
class Productivitymobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = ProductivityViabilityTable.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = ProductivityViabilityTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = ProductivityViabilityTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.cropscultivated=request.json['cropscultivated']
                farmer.growscrops=request.json['growscrops']
                farmer.oilpalmfertilizers=request.json['oilpalmfertilizers']
                farmer.cocoafertilizers=request.json['cocoafertilizers']
                farmer.fertilizerfrequency=request.json['fertilizerfrequency']
                farmer.pestfungherbicides=request.json['pestfungherbicides']
                farmer.stagechemicalapplied=request.json['stagechemicalapplied']
                farmer.noofoildrums=request.json['noofoildrums']
                farmer.noofbagssesame=request.json['noofbagssesame']
                farmer.noofbagssoyabeans=request.json['noofbagssoyabeans']
                farmer.noofbagsmaize=request.json['noofbagsmaize']
                farmer.noofbagssorghum=request.json['noofbagssorghum']
                farmer.noofbagscocoabeans=request.json['noofbagscocoabeans']
                farmer.croptrainedon=request.json['croptrainedon']
                farmer.wherewhenwhotrained=request.json['wherewhenwhotrained']
                farmer.nooftraining=request.json['nooftraining']
                farmer.pruningfrequency=request.json['pruningfrequency']
                farmer.cropbasedproblems=request.json['cropbasedproblems']
                farmer.tooyoungcrops=request.json['tooyoungcrops']
                farmer.youngcropsandstage=request.json['youngcropsandstage']
                farmer.cultivationstartdate=request.json['cultivationstartdate']
                farmer.isintensivefarmingpractised=request.json['isintensivefarmingpractised']
                farmer.economicactivities=request.json['economicactivities']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    def get(self, mobile):
        farmer = ProductivityViabilityTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'productivity{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = ProductivityViabilityTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'productivity{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}