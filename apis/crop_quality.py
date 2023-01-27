from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add crop quality
class AddCropQuality(Resource):	
    def post(self):
        try:
            new_data = CropQuality(tracing_id=request.json['tracing_id'],moisture_content=request.json['moisture_content'],
        foreign_matter=request.json['foreign_matter'],test_weight=request.json['test_weight'],quality=request.json['quality'],
        rotten_shriveled=request.json['rotten_shriveled'],hardness=request.json['hardness'],splits=request.json['splits'],
        oil_content=request.json['oil_content'],infestation=request.json['infestation'],hectoliter=request.json['hectoliter'],
        total_defects=request.json['total_defects'],dockage=request.json['dockage'],ash_content=request.json['ash_content'],
        insoluble_ash=request.json['insoluble_ash'],volatile=request.json['volatile'],mold_weight=request.json['mold_weight'],
        drying_process=request.json['drying_process'],dead_insects=request.json['dead_insects'],excreta=request.json['excreta'],
        insect_defiled=request.json['insect_defiled'],curcumin=request.json['curcumin'],extraneous=request.json['extraneous'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'crop quality{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}

# get crop quality with id
class CropQualityTracing(Resource):
    def get(self, tracing_id):
        farmer = CropQuality.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            return {"error":False,"message":f'crop quality{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":tidnotfound}
    def delete(self, tracing_id):
        farmer = CropQuality.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'crop quality{removed}'}
        else:
            return {"error":True,"message":tidnotfound}


# get all crop quality
class AllCropQuality(Resource):
    def get(self):
        all_farmers = CropQuality.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'crop quality{retrieved}','data': all_farmers})

# with pagination
class ListCropQuality(Resource):
    def get(self,limit):
        all_farmers = CropQuality.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
