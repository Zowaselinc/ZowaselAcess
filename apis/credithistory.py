from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add credit history
class AddCreditHistory(Resource):
    def post(self):
        try:
            farmer = CreditHistoryTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmercredithistory = CreditHistoryTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
        hastakenloanbefore=request.json['hastakenloanbefore'],sourceofloan=request.json['sourceofloan'],
        pastloanamount=request.json['pastloanamount'],howloanwasrepaid=request.json['howloanwasrepaid'],
        isreadytopayinterest=request.json['isreadytopayinterest'],canprovidecollateral=request.json['canprovidecollateral'],
        whynocollateral=request.json['whynocollateral'])
                db.session.add(farmercredithistory)
                db.session.commit()
                return {"error":False,"message":f'credit history{added}',"data":farmercredithistory.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get credit history by bvn
class CreditHistorybvn(Resource):
    def get(self, bvn):
        farmer = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'credit history{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'credit history{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all credit history
class AllCreditHistory(Resource):
    def get(self):
        all_farmers = CreditHistoryTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'credit history{retrieved}','data': all_farmers})

# with pagination
class ListCreditHistory(Resource):
    def get(self, limit):
        all_farmers = CreditHistoryTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get credit history by mobile
class CreditHistorymobile(Resource):
    def get(self, mobile):
        farmer = CreditHistoryTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'credit history{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = CreditHistoryTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'credit history{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}