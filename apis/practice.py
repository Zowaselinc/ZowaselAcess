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
                farmerpractice = FarmPractice(bvn=request.json['bvn'],sizeoffarm=request.json['sizeoffarm'],
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
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))


