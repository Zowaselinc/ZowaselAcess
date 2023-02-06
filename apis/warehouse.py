from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add warehouse
class AddWarehouse(Resource):	
    def post(self):
        try:
            new_data = Warehouse(tracing_id=request.json['tracing_id'],location=request.json['location'],warehouse_type=request.json['warehouse_type'],
        capacity=request.json['capacity'],standard=request.json['standard'],insurance=request.json['insurance'],
        duration=request.json['duration'],cost=request.json['cost'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'Warehouse{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get warehouse with id
class WarehouseTracing(Resource):
    def put(self, tracing_id):
        try:
            # pull row from db table
            farmer = Warehouse.query.filter_by(tracing_id=tracing_id).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":tidnotfound}
            # if found, validate new values
            if farmer:
                # validate new tracing_id
                if farmer.tracing_id != request.json['tracing_id']:
                    checkdup = Warehouse.query.filter_by(tracing_id=request.json['tracing_id']).first()
                    if checkdup:
                        return {"error":True,"message":tidexists}
                    else:
                        farmer.tracing_id=request.json['tracing_id']
                # assign other fields
                farmer.location=request.json['location']
                farmer.warehouse_type=request.json['warehouse_type']
                farmer.capacity=request.json['capacity']
                farmer.standard=request.json['standard']
                farmer.insurance=request.json['insurance']
                farmer.duration=request.json['duration']
                farmer.cost=request.json['cost']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    
    def get(self, tracing_id):
        farmer = Warehouse.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            return {"error":False,"message":added,"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":tidnotfound}
    def delete(self, tracing_id):
        farmer = Warehouse.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'Warehouse{removed}'}
        else:
            return {"error":True,"message":tidnotfound}
# get all warehouse
class AllWarehouse(Resource):
    def get(self):
        all_farmers = Warehouse.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'Warehouse{retrieved}','data': all_farmers})

# with pagination
class ListWarehouse(Resource):
    def get(self, limit):
        all_farmers = Warehouse.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))


