from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add practice
class AddFarmPractice(Resource):	
    def post(self):
        try:
            farmer = FarmPractice.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmerpractice = FarmPractice(bvn=request.json['bvn'],mobile=request.json['mobile'],
                sizeoffarm=request.json['sizeoffarm'],
        farmisrentedorleased=request.json['farmisrentedorleased'],noofyearsleased=request.json['noofyearsleased'],
        usesmachines=request.json['usesmachines'],rotatescrops=request.json['rotatescrops'],
        noOfhectaresproducedyearly=request.json['noOfhectaresproducedyearly'],approxfertilizeruse=request.json['approxfertilizeruse'],
        nooffertlizerapplications=request.json['nooffertlizerapplications'],decisionforspraying=request.json['decisionforspraying'],
        weedcontrolpractice=request.json['weedcontrolpractice'],estimatedincomepercrop=request.json['estimatedincomepercrop'],
        cropthatcansellwell=request.json['cropthatcansellwell'],hasfarmplanorproject=request.json['hasfarmplanorproject'],
        farmprojectinfo=request.json['farmprojectinfo'])
                db.session.add(farmerpractice)
                db.session.commit()
                return {"error":False,"message":f'practice{added}',"data":farmerpractice.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get practice with bvn
class Practicebvn(Resource):
    def get(self, bvn):
        farmer = FarmPractice.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'practice{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = FarmPractice.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'practice{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
    
# get all practice
class AllPractice(Resource):
    def get(self):
        all_farmers = FarmPractice.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'practice{retrieved}','data': all_farmers})

# with pagination
class ListPractice(Resource):
    def get(self,limit):
        all_farmers = FarmPractice.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))


# get practice with mobile
class Practicemobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = FarmPractice.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = FarmPractice.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = FarmPractice.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.sizeoffarm=request.json['sizeoffarm']
                farmer.farmisrentedorleased=request.json['farmisrentedorleased']
                farmer.noofyearsleased=request.json['noofyearsleased']
                farmer.usesmachines=request.json['usesmachines']
                farmer.rotatescrops=request.json['rotatescrops']
                farmer.noOfhectaresproducedyearly=request.json['noOfhectaresproducedyearly']
                farmer.approxfertilizeruse=request.json['approxfertilizeruse']
                farmer.nooffertlizerapplications=request.json['nooffertlizerapplications']
                farmer.decisionforspraying=request.json['decisionforspraying']
                farmer.weedcontrolpractice=request.json['weedcontrolpractice']
                farmer.estimatedincomepercrop=request.json['estimatedincomepercrop']
                farmer.cropthatcansellwell=request.json['cropthatcansellwell']
                farmer.hasfarmplanorproject=request.json['hasfarmplanorproject']
                farmer.farmprojectinfo=request.json['farmprojectinfo']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    def get(self, mobile):
        farmer = FarmPractice.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'practice{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = FarmPractice.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'practice{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}