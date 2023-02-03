from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add capital
class AddCapital(Resource):	
    def post(self):
        try:
            farmer = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                return {"error":True,"message":bvnexists}
            farmer = CapitalTable.query.filter_by(mobile=request.json['mobile']).first()
            if farmer:
                return {"error":True,"message":mobileexists}
            else:
                farmercapital = CapitalTable(bvn=request.json['bvn'],mobile=request.json['mobile'],mainincomesource=request.json['mainincomesource'],
        otherincomesource=request.json['otherincomesource'],noofincomeearners=request.json['noofincomeearners'],
        hasbankaccount=request.json['hasbankaccount'],firstfundingoption=request.json['firstfundingoption'],
        needsaloan=request.json['needsaloan'],paybackmonths=request.json['paybackmonths'],
        harvestqtychanged=request.json['harvestqtychanged'],pestexpensechanged=request.json['pestexpensechanged'])
                db.session.add(farmercapital)
                db.session.commit()
                return {"error":False,"message":f'capital{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

# get capital by bvn
class Capitalbvn(Resource):
    def put(self, bvn):
        try:
            # pull row from db table
            farmer = CapitalTable.query.filter_by(bvn=bvn).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":bvnnotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = CapitalTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.mainincomesource=request.json['mainincomesource']
                farmer.otherincomesource=request.json['otherincomesource']
                farmer.noofincomeearners=request.json['noofincomeearners']
                farmer.hasbankaccount=request.json['hasbankaccount']
                farmer.firstfundingoption=request.json['firstfundingoption']
                farmer.needsaloan=request.json['needsaloan']
                farmer.paybackmonths=request.json['paybackmonths']
                farmer.harvestqtychanged=request.json['harvestqtychanged']
                farmer.pestexpensechanged=request.json['pestexpensechanged']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    def get(self, bvn):
        farmer = CapitalTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":f'capital{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = CapitalTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'capital{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}

# get all capital 
class AllCapital(Resource):
    def get(self):
        all_farmers = CapitalTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'capital{retrieved}','data': all_farmers})

# with pagination
class ListCapital(Resource):
    def get(self, limit):
        all_farmers = CapitalTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        f'/list/limit={limit}',
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

# get capital by mobile
class Capitalmobile(Resource):
    def put(self, mobile):
        try:
            # pull row from db table
            farmer = CapitalTable.query.filter_by(mobile=mobile).first()
            # return error if not found
            if not farmer:
                return {"error":True,"message":mobilenotfound}
            # if found, validate new values
            if farmer:
                # validate new bvn
                if farmer.bvn != request.json['bvn']:
                    checkdup = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
                    if checkdup:
                        return {"error":True,"message":bvnexists}
                    else:
                        farmer.bvn=request.json['bvn']
                # validate new mobile number
                if farmer.mobile != request.json['mobile']:
                    checkdup = CapitalTable.query.filter_by(mobile=request.json['mobile']).first()
                    if checkdup:
                        return {"error":True,"message":mobileexists}
                    else:
                        farmer.mobile=request.json['mobile']
                # assign other fields
                farmer.mainincomesource=request.json['mainincomesource']
                farmer.otherincomesource=request.json['otherincomesource']
                farmer.noofincomeearners=request.json['noofincomeearners']
                farmer.hasbankaccount=request.json['hasbankaccount']
                farmer.firstfundingoption=request.json['firstfundingoption']
                farmer.needsaloan=request.json['needsaloan']
                farmer.paybackmonths=request.json['paybackmonths']
                farmer.harvestqtychanged=request.json['harvestqtychanged']
                farmer.pestexpensechanged=request.json['pestexpensechanged']
                db.session.commit()
                return {"error":False,"message":f'farmer{updated}',"data":farmer.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
    def get(self, mobile):
        farmer = CapitalTable.query.filter_by(mobile=mobile).first()
        if farmer:
            return {"error":False,"message":f'capital{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":mobilenotfound}
    def delete(self, mobile):
        farmer = CapitalTable.query.filter_by(mobile=mobile).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'capital{removed}'}
        else:
            return {"error":True,"message":mobilenotfound}