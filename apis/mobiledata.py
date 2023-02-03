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
                farmermobiledata = MobileDataTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
                mobilephonetype=request.json['mobilephonetype'],
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
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get mobile data with mobile  
class MobileDatamobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = MobileDataTable.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = MobileDataTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = MobileDataTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.mobilephonetype=request.json['mobilephonetype']
                farmer.avweeklyphoneuse=request.json['avweeklyphoneuse']
                farmer.callsoutnumber=request.json['callsoutnumber']
                farmer.callsoutminutes=request.json['callsoutminutes']
                farmer.callsinnumber=request.json['callsinnumber']
                farmer.callinminutes=request.json['callinminutes']
                farmer.smssent=request.json['smssent']
                farmer.dataprecedingplanswitch=request.json['dataprecedingplanswitch']
                farmer.billpaymenthistory=request.json['billpaymenthistory']
                farmer.avweeklydatarefill=request.json['avweeklydatarefill']
                farmer.noOfmobileapps=request.json['noOfmobileapps']
                farmer.avtimespentonapp=request.json['avtimespentonapp']
                farmer.mobileappkinds=request.json['mobileappkinds']
                farmer.appdeleterate=request.json['appdeleterate']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    
    
    def get(self, mobile):
        farmer = MobileDataTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'mobile data{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = MobileDataTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'mobile data{retrieved}'}
        else:
            return {"error":True,"message":mobilenotfound}