from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add crop info
class AddCropInfo(Resource):	
    def post(self):
        try:
            new_data = CropInfo(tracing_id=request.json['tracing_id'],crop_type=request.json['crop_type'],sourcing_location=request.json['sourcing_location'],
        crop_origin=request.json['crop_origin'],crop_qty=request.json['crop_qty'],crop_variety=request.json['crop_variety'],
        cooperative=request.json['cooperative'],no_of_farmer_group=request.json['no_of_farmer_group'],
        female_to_male=request.json['female_to_male'],farmer_name=request.json['farmer_name'],gender=request.json['gender'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'crop info{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# getcrop info with id
class CropInfoTracing(Resource):
    def put(self, tracing_id):
        try:
            # pull row from db table
            farmer = CropInfo.query.filter_by(tracing_id=tracing_id).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":tidnotfound}
            # if found, validate new values
            if farmer:
                # validate new tracing_id
                if farmer.tracing_id != request.json['tracing_id']:
                    checkdup = CropInfo.query.filter_by(tracing_id=request.json['tracing_id']).first()
                    if checkdup:
                        return {"error":True,"message":tidexists}
                    else:
                        farmer.tracing_id=request.json['tracing_id']
                # assign other fields
                farmer.crop_type=request.json['crop_type']
                farmer.sourcing_location=request.json['sourcing_location']
                farmer.crop_origin=request.json['crop_origin']
                farmer.crop_qty=request.json['crop_qty']
                farmer.crop_variety=request.json['crop_variety']
                farmer.cooperative=request.json['cooperative']
                farmer.no_of_farmer_group=request.json['no_of_farmer_group']
                farmer.female_to_male=request.json['female_to_male']
                farmer.farmer_name=request.json['farmer_name'],
                farmer.gender=request.json['gender']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    def get(self, tracing_id):
        farmer = CropInfo.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            return {"error":False,"message":f'crop info{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":tidnotfound}
    def delete(self, tracing_id):
        farmer = CropInfo.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'crop info{removed}'}
        else:
            return {"error":True,"message":tidnotfound}

# get all crop info
class AllCropInfo(Resource):
    def get(self):
        all_farmers = CropInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'crop info{retrieved}','data': all_farmers})

# with pagination
class ListCropInfo(Resource):
    def get(self,limit):
        all_farmers = CropInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))