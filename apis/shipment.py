from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add shipment
class AddShipment(Resource):	
    def post(self):
        try:
            new_data = Shipment(tracing_id=request.json['tracing_id'],location=request.json['location'],
        loading_date=request.json['loading_date'],no_of_people=request.json['no_of_people'],
        vehicle_type=request.json['vehicle_type'],plate_no=request.json['plate_no'],vehicle_capacity=request.json['vehicle_capacity'],
        driver_name=request.json['driver_name'],driver_number=request.json['driver_number'],insurance=request.json['insurance'],
        delivery_time=request.json['delivery_time'],delivery_date=request.json['delivery_date'],
        arrival_time=request.json['arrival_time'],no_of_police=request.json['no_of_police'],local_levy=request.json['local_levy'],
        state_levy=request.json['state_levy'],truck_levy=request.json['truck_levy'],
        inter_state_levy=request.json['inter_state_levy'],no_of_offloaders=request.json['no_of_offloaders'],
        quality_check=request.json['quality_check'],quality_checked=request.json['quality_checked'],
        quality_accepted=request.json['quality_accepted'],quality_rejected=request.json['quality_rejected'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'shipment{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get shipment by id
class ShipmentTracing(Resource):
    def put(self, tracing_id):
        try:
            # pull row from db table
            farmer = Shipment.query.filter_by(tracing_id=tracing_id).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":tidnotfound}
            # if found, validate new values
            if farmer:
                # validate new tracing_id
                if farmer.tracing_id != request.json['tracing_id']:
                    checkdup = Shipment.query.filter_by(tracing_id=request.json['tracing_id']).first()
                    if checkdup:
                        return {"error":True,"message":tidexists}
                    else:
                        farmer.tracing_id=request.json['tracing_id']
                # assign other fields
                farmer.location=request.json['location']
                farmer.loading_date=request.json['loading_date']
                farmer.no_of_people=request.json['no_of_people']
                farmer.vehicle_type=request.json['vehicle_type']
                farmer.plate_no=request.json['plate_no']
                farmer.vehicle_capacity=request.json['vehicle_capacity']
                farmer.driver_name=request.json['driver_name']
                farmer.driver_number=request.json['driver_number']
                farmer.insurance=request.json['insurance']
                farmer.delivery_time=request.json['delivery_time']
                farmer.delivery_date=request.json['delivery_date']
                farmer.arrival_time=request.json['arrival_time']
                farmer.no_of_police=request.json['no_of_police']
                farmer.local_levy=request.json['local_levy']
                farmer.state_levy=request.json['state_levy']
                farmer.truck_levy=request.json['truck_levy']
                farmer.inter_state_levy=request.json['inter_state_levy']
                farmer.no_of_offloaders=request.json['no_of_offloaders']
                farmer.quality_check=request.json['quality_check']
                farmer.quality_checked=request.json['quality_checked']
                farmer.quality_accepted=request.json['quality_accepted']
                farmer.quality_rejected=request.json['quality_rejected']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    
    def get(self, tracing_id):
        farmer = Shipment.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            return {"error":False,"message":f'shipment{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":tidnotfound}
    def delete(self, tracing_id):
        farmer = Shipment.query.filter_by(tracing_id=tracing_id).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'shipment{removed}'}
        else:
            return {"error":True,"message":tidnotfound}

# get all shipment
class AllShipment(Resource):
    def get(self):
        all_farmers = Shipment.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'shipment{retrieved}','data': all_farmers})
# with pagination
class ListShipment(Resource):
    def get(self, limit):
        all_farmers = Shipment.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))