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
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get crop quality with id
class CropQualityTracing(Resource):
    def put(self, tracing_id):
        try:
            # pull row from db table
            farmer = CropQuality.query.filter_by(tracing_id=tracing_id).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":tidnotfound}
            # if found, validate new values
            if farmer:
                # validate new tracing_id
                if farmer.tracing_id != request.json['tracing_id']:
                    checkdup = CropQuality.query.filter_by(tracing_id=request.json['tracing_id']).first()
                    if checkdup:
                        return {"error":True,"message":tidexists}
                    else:
                        farmer.tracing_id=request.json['tracing_id']
                # assign other fields
                farmer.moisture_content=request.json['moisture_content']
                farmer.foreign_matter=request.json['foreign_matter']
                farmer.test_weight=request.json['test_weight']
                farmer.quality=request.json['quality']
                farmer.rotten_shriveled=request.json['rotten_shriveled']
                farmer.hardness=request.json['hardness']
                farmer.splits=request.json['splits']
                farmer.oil_content=request.json['oil_content']
                farmer.infestation=request.json['infestation']
                farmer.hectoliter=request.json['hectoliter']
                farmer.total_defects=request.json['total_defects']
                farmer.dockage=request.json['dockage']
                farmer.ash_content=request.json['ash_content']
                farmer.insoluble_ash=request.json['insoluble_ash']
                farmer.volatile=request.json['volatile']
                farmer.mold_weight=request.json['mold_weight']
                farmer.drying_process=request.json['drying_process']
                farmer.dead_insects=request.json['dead_insects']
                farmer.excreta=request.json['excreta']
                farmer.insect_defiled=request.json['insect_defiled']
                farmer.curcumin=request.json['curcumin']
                farmer.extraneous=request.json['extraneous']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
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
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
