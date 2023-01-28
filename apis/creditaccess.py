from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add credit access
class AddCreditAccess(Resource):
    def post(self):
        try:
            farmer = CreditAccessTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                farmercreditaccess = CreditAccessTable(bvn=request.json['bvn'],
        hasservedastreasurer=request.json['hasservedastreasurer'],durationastreasurer=request.json['durationastreasurer'],
        savesmoneymonthly=request.json['savesmoneymonthly'],savingsamount=request.json['savingsamount'],
        haddifficultyrepaying=request.json['haddifficultyrepaying'],difficultloanamount=request.json['difficultloanamount'],
        difficultyreason=request.json['difficultyreason'],noofdifficultloans=request.json['noofdifficultloans'],
        noofrepaidloans=request.json['noofrepaidloans'],noofloansontime=request.json['noofloansontime'],
        estmonthlyincome=request.json['estmonthlyincome'],costofcultivation=request.json['costofcultivation'],
        farmproduceexchanged=request.json['farmproduceexchanged'],nooftimesexchanged=request.json['nooftimesexchanged'],
        collateral=request.json['collateral'],applyloanamount=request.json['applyloanamount'],
        yearsofcultivating=request.json['collateral'],annualturnover=request.json['annualturnover'])
                db.session.add(farmercreditaccess)
                db.session.commit()
                return {"error":False,"message":f'credit access{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get credit access by bvn
class CreditAccessbvn(Resource):
    def get(self, bvn):
        farmer = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'credit access{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'credit access{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
    
# get all credit access
class AllCreditAccess(Resource):
    def get(self):
        all_farmers = CreditAccessTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'credit access{retrieved}','data': all_farmers})

# with pagination
class ListCreditAccess(Resource):
    def get(self, limit):
        all_farmers = CreditAccessTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
