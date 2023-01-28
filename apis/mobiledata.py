from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add mobile data
class AddMobileData(Resource):	
    def post(self):
        try:
            farmer = MobileDataTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmermobiledata = MobileDataTable(bvn=request.json['bvn'],mobilephonetype=request.json['mobilephonetype'],
        avweeklyphoneuse=request.json['avweeklyphoneuse'],callsoutnumber=request.json['callsoutnumber'],
        callsoutminutes=request.json['callsoutminutes'],callsinnumber=request.json['callsinnumber'],
        callinminutes=request.json['callinminutes'],smssent=request.json['smssent'],
        dataprecedingplanswitch=request.json['dataprecedingplanswitch'],billpaymenthistory=request.json['billpaymenthistory'],
        avweeklydatarefill=request.json['avweeklydatarefill'],noOfmobileapps=request.json['noOfmobileapps'],
        avtimespentonapp=request.json['avtimespentonapp'],mobileappkinds=request.json['mobileappkinds'],
        appdeleterate=request.json['appdeleterate'])
                db.session.add(farmermobiledata)
                db.session.commit()
                return {"error":False,"message":f'mobile data{added}',"data":farmermobiledata.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get mobile data with bvn  
class MobileDatabvn(Resource):
    def get(self, bvn):
        farmer = MobileDataTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'mobile data{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = MobileDataTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'mobile data{retrieved}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all mobile data
class AllMobileData(Resource):
    def get(self):
        all_farmers = MobileDataTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'mobile data{retrieved}','data': all_farmers})

# with pagination
class ListMobileData(Resource):
    def get(self, limit):
        all_farmers = MobileDataTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
