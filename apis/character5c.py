from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add all charater tables at once
class AddCharacter5c(Resource):
    def post(self):
        try:
            farmercredithistory = CreditHistoryTable(bvn=request.json['bvn'],
        hastakenloanbefore=request.json['hastakenloanbefore'],sourceofloan=request.json['sourceofloan'],
        pastloanamount=request.json['pastloanamount'],howloanwasrepaid=request.json['howloanwasrepaid'],
        isreadytopayinterest=request.json['isreadytopayinterest'],canprovidecollateral=request.json['canprovidecollateral'],
        whynocollateral=request.json['whynocollateral'])
            farmerproductivity = ProductivityViabilityTable(bvn=request.json['bvn'],
        cropscultivated=request.json['cropscultivated'],growscrops=request.json['growscrops'],
        oilpalmfertilizers=request.json['oilpalmfertilizers'],cocoafertilizers=request.json['cocoafertilizers'],
        fertilizerfrequency=request.json['fertilizerfrequency'],pestfungherbicides=request.json['pestfungherbicides'],
        stagechemicalapplied=request.json['stagechemicalapplied'],noofoildrums=request.json['noofoildrums'],
        noofbagssesame=request.json['noofbagssesame'],noofbagssoyabeans=request.json['noofbagssoyabeans'],
        noofbagsmaize=request.json['noofbagsmaize'],noofbagssorghum=request.json['noofbagssorghum'],
        noofbagscocoabeans=request.json['noofbagscocoabeans'],croptrainedon=request.json['croptrainedon'],
        wherewhenwhotrained=request.json['wherewhenwhotrained'],nooftraining=request.json['nooftraining'],
        pruningfrequency=request.json['pruningfrequency'],cropbasedproblems=request.json['cropbasedproblems'],
        tooyoungcrops=request.json['tooyoungcrops'],youngcropsandstage=request.json['youngcropsandstage'],
        cultivationstartdate=request.json['cultivationstartdate'],isintensivefarmingpractised=request.json['isintensivefarmingpractised'],
        economicactivities=request.json['economicactivities'])
            farmeragronomy = AgronomyServicesTable(bvn=request.json['bvn'],
        knowsagriprocessed=request.json['knowsagriprocessed'],agronomistthattrainedyou=request.json['agronomistthattrainedyou'],
        canmanageecosystem=request.json['canmanageecosystem'],howtomanageecosystem=request.json['howtomanageecosystem'],
        istrainingbeneficial=request.json['istrainingbeneficial'],fieldroutines=request.json['fieldroutines'],
        harvestingchanges=request.json['harvestingchanges'],iscropcalendarbeneficial=request.json['iscropcalendarbeneficial'],
        cropcalendarbenefits=request.json['cropcalendarbenefits'],recordkeepingbenefits=request.json['recordkeepingbenefits'])
            farmerpsychometrics = PsychometricsTable(bvn=request.json['bvn'],fluidintelligence=request.json['fluidintelligence'],
        attitudesandbeliefs=request.json['attitudesandbeliefs'],agribusinessskills=request.json['agribusinessskills'],
        ethicsandhonesty=request.json['ethicsandhonesty'],savesenough=request.json['savesenough'],
        haslazyneighbors=request.json['haslazyneighbors'])
            farmermobiledata = MobileDataTable(bvn=request.json['bvn'],mobilephonetype=request.json['mobilephonetype'],
        avweeklyphoneuse=request.json['avweeklyphoneuse'],callsoutnumber=request.json['callsoutnumber'],
        callsoutminutes=request.json['callsoutminutes'],callsinnumber=request.json['callsinnumber'],
        callinminutes=request.json['callinminutes'],smssent=request.json['smssent'],
        dataprecedingplanswitch=request.json['dataprecedingplanswitch'],billpaymenthistory=request.json['billpaymenthistory'],
        avweeklydatarefill=request.json['avweeklydatarefill'],noOfmobileapps=request.json['noOfmobileapps'],
        avtimespentonapp=request.json['avtimespentonapp'],mobileappkinds=request.json['mobileappkinds'],
        appdeleterate=request.json['appdeleterate'])
            # Add data only if Id does not exist in database already
            farmer = CreditHistoryTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmercredithistory)
            farmer = ProductivityViabilityTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmerproductivity)
            farmer = AgronomyServicesTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmeragronomy)
            farmer = PsychometricsTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmerpsychometrics)
            farmer = MobileDataTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmermobiledata)
            db.session.commit()
            return {"error":False,"message":f'character{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
class Character5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        farmer2 = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        farmer3 = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        farmer4 = PsychometricsTable.query.filter_by(bvn=bvn).first()
        farmer5 = MobileDataTable.query.filter_by(bvn=bvn).first()
        
        if not farmer1:
            farmer1={"error":True,"message":bvnnotfound}
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":bvnnotfound}
        else:
            farmer2=farmer2.json()
        if not farmer3:
            farmer3={"error":True,"message":bvnnotfound}
        else:
            farmer3=farmer3.json()
        if not farmer4:
            farmer4={"error":True,"message":bvnnotfound}
        else:
            farmer4=farmer4.json()
        if not farmer5:
            farmer5={"error":True,"message":bvnnotfound}
        else:
            farmer5=farmer5.json()
        return {"error":False,"message":f'character{retrieved}',"data":{'credithistory':farmer1,'productivity':farmer2,'agronomy':farmer3,'psychometrics':farmer4,'mobiledata':farmer5}}
        
    def delete(self, bvn):
        farmer1 = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        farmer2 = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        farmer3 = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        farmer4 = PsychometricsTable.query.filter_by(bvn=bvn).first()
        farmer5 = MobileDataTable.query.filter_by(bvn=bvn).first()
        if farmer1:
            db.session.delete(farmer1)
            db.session.commit()
        if farmer2:
            db.session.delete(farmer2)
            db.session.commit()
        if farmer3:
            db.session.delete(farmer3)
            db.session.commit()
        if farmer4:
            db.session.delete(farmer4)
            db.session.commit()
        if farmer5:
            db.session.delete(farmer5)
            db.session.commit()
        return {"error":False,"message":f'character{removed}'}

class AllCharacter5c(Resource):
    def get(self):
        all_farmer1 = CreditHistoryTable.query.all()
        all_farmer1 = [farmer.json() for farmer in all_farmer1]
        all_farmer2 = ProductivityViabilityTable.query.all()
        all_farmer2 = [farmer.json() for farmer in all_farmer2]
        all_farmer3 = AgronomyServicesTable.query.all()
        all_farmer3 = [farmer.json() for farmer in all_farmer3]
        all_farmer4 = PsychometricsTable.query.all()
        all_farmer4 = [farmer.json() for farmer in all_farmer4]
        all_farmer5 = MobileDataTable.query.all()
        all_farmer5 = [farmer.json() for farmer in all_farmer5]
        return {"error":False,"message":f'character{retrieved}',"data":{'credithistory':all_farmer1,'productivity':all_farmer2,'agronomy':all_farmer3,'psychometrics':all_farmer4,'mobiledata':all_farmer5}}
