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
            farmer = CreditAccessTable.query.filter_by(mobile=request.json['mobile']).first()
            if farmer:
                return {"error":True,"message":mobileexists}
            else:
                farmercreditaccess = CreditAccessTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
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
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get credit access by mobile
class CreditAccessmobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = CreditAccessTable.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = CreditAccessTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = CreditAccessTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.hasservedastreasurer=request.json['hasservedastreasurer']
                farmer.durationastreasurer=request.json['durationastreasurer']
                farmer.savesmoneymonthly=request.json['savesmoneymonthly']
                farmer.savingsamount=request.json['savingsamount']
                farmer.haddifficultyrepaying=request.json['haddifficultyrepaying']
                farmer.difficultloanamount=request.json['difficultloanamount']
                farmer.difficultyreason=request.json['difficultyreason']
                farmer.noofdifficultloans=request.json['noofdifficultloans']
                farmer.noofrepaidloans=request.json['noofrepaidloans']
                farmer.noofloansontime=request.json['noofloansontime']
                farmer.estmonthlyincome=request.json['estmonthlyincome']
                farmer.costofcultivation=request.json['costofcultivation']
                farmer.farmproduceexchanged=request.json['farmproduceexchanged']
                farmer.nooftimesexchanged=request.json['nooftimesexchanged']
                farmer.collateral=request.json['collateral']
                farmer.applyloanamount=request.json['applyloanamount']
                farmer.yearsofcultivating=request.json['collateral']
                farmer.annualturnover=request.json['annualturnover']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
        
    def get(self, mobile):
        farmer = CreditAccessTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'credit access{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = CreditAccessTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'credit access{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}