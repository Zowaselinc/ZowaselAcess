from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add psychometrics
class AddPsychometrics(Resource):	
    def post(self):
        try:
            farmer = PsychometricsTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmerpsychometrics = PsychometricsTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
                fluidintelligence=request.json['fluidintelligence'],
        attitudesandbeliefs=request.json['attitudesandbeliefs'],agribusinessskills=request.json['agribusinessskills'],
        ethicsandhonesty=request.json['ethicsandhonesty'],savesenough=request.json['savesenough'],
        haslazyneighbors=request.json['haslazyneighbors'])
                db.session.add(farmerpsychometrics)
                db.session.commit()
                return {"error":False,"message":f'psychometrics{added}',"data":farmerpsychometrics.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get psychometrics by bvn
class Psychometricsbvn(Resource):
    def get(self, bvn):
        farmer = PsychometricsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'psychometrics{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = PsychometricsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'psychometrics{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
# get all psychometrics
class AllPsychometrics(Resource):
    def get(self):
        all_farmers = PsychometricsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'psychometrics{retrieved}','data': all_farmers})

# with pagination
class ListPsychometrics(Resource):
    def get(self, limit):
        all_farmers = PsychometricsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
# get psychometrics by mobile
class Psychometricsmobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = PsychometricsTable.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = PsychometricsTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = PsychometricsTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.fluidintelligence=request.json['fluidintelligence']
                farmer.attitudesandbeliefs=request.json['attitudesandbeliefs']
                farmer.agribusinessskills=request.json['agribusinessskills']
                farmer.ethicsandhonesty=request.json['ethicsandhonesty']
                farmer.savesenough=request.json['savesenough']
                farmer.haslazyneighbors=request.json['haslazyneighbors']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    
    def get(self, mobile):
        farmer = PsychometricsTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'psychometrics{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = PsychometricsTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'psychometrics{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}