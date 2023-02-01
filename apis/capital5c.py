from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add all capital tables at once
class AddCapital5c(Resource):	
    def post(self):
        try:
            farmercapital = CapitalTable(bvn=request.json['bvn'],mobile=request.json['mobile'],mainincomesource=request.json['mainincomesource'],
        otherincomesource=request.json['otherincomesource'],noofincomeearners=request.json['noofincomeearners'],
        hasbankaccount=request.json['hasbankaccount'],firstfundingoption=request.json['firstfundingoption'],
        needsaloan=request.json['needsaloan'],paybackmonths=request.json['paybackmonths'],
        harvestqtychanged=request.json['harvestqtychanged'],pestexpensechanged=request.json['pestexpensechanged'])
            farmercreditaccess = CreditAccessTable(bvn=request.json['bvn'],
        hasservedastreasurer=request.json['hasservedastreasurer'],mobile=request.json['mobile'],durationastreasurer=request.json['durationastreasurer'],
        savesmoneymonthly=request.json['savesmoneymonthly'],savingsamount=request.json['savingsamount'],
        haddifficultyrepaying=request.json['haddifficultyrepaying'],difficultloanamount=request.json['difficultloanamount'],
        difficultyreason=request.json['difficultyreason'],noofdifficultloans=request.json['noofdifficultloans'],
        noofrepaidloans=request.json['noofrepaidloans'],noofloansontime=request.json['noofloansontime'],
        estmonthlyincome=request.json['estmonthlyincome'],costofcultivation=request.json['costofcultivation'],
        farmproduceexchanged=request.json['farmproduceexchanged'],nooftimesexchanged=request.json['nooftimesexchanged'],
        collateral=request.json['collateral'],applyloanamount=request.json['applyloanamount'],
        yearsofcultivating=request.json['collateral'],annualturnover=request.json['annualturnover'])
            # Add data only if Id does not exist in database already
            farmer = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass    
            else:
                db.session.add(farmercapital)
            # Add data only if Id does not exist in database already
            farmer = CreditAccessTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmercreditaccess)
            db.session.commit()
            return {"error":False,"message":f'capital{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

class Capital5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CapitalTable.query.filter_by(bvn=bvn).first()
        farmer2 = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if not farmer1:
            farmer1={"error":True,"message":bvnnotfound}
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":bvnnotfound}
        else:
            farmer2=farmer2.json()
        return {"error":False,"message":f'capital{retrieved}',"data":{'capital':farmer1,'creditaccess':farmer2}}
        
class AllCapital5c(Resource):
    def get(self):
        all_farmer1 = CapitalTable.query.all()
        all_farmer1 = [farmer.json() for farmer in all_farmer1]
        all_farmer2 = CreditAccessTable.query.all()
        all_farmer2 = [farmer.json() for farmer in all_farmer2]
        return {"error":False,"message":f'capital{retrieved}',"data":{'capital':all_farmer1,'creditaccess':all_farmer2}}
