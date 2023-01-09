# Import flask 
from flask import Flask, jsonify, request, current_app
from flask_cors import CORS,cross_origin
from flask_sqlalchemy import SQLAlchemy
#from flask_restplus import Resource, Api, fields
from flask_restx import Api, Resource
from flask_mysqldb import MySQL
from models import *
import csv
import io
from io import StringIO


# Import database models with app context
#with app.app_context():
  #from models import *
#from flasgger import Swagger
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask_migrate import Migrate
import numpy as np
import pandas as pd
import pickle
from modelExample import preprocess_df, bin_target
model = pickle.load(open('modelExample.pkl','rb'))
api = Api(app, title='Zowasel')
Migrate(app,db)
app.config['CORS_HEADERS'] = 'Content-Type'


def applyLoan(bvn):
    crop_card = Cropcard.query.filter_by(bvn=bvn).first()
    print(bvn)
    if crop_card:
        prices = [int(crop_card.fertilizer_cost),int(crop_card.mechanization_cost),int(crop_card.labour_cost),
        int(crop_card.harvest_cost),int(crop_card.other_cost),10000] 
        price = np.median(prices)
    else:
        price = 0
    print()
    return price

def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        return {"error":False,"data":"no record"}
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj


# Kyf

class AddFarmer(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = FarmerTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            message = {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        farmer = FarmerTable.query.filter_by(email=request.json['email']).first()
        if farmer:
            message = {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with email already exists"}
        else:
            farmerkyf = FarmerTable(firstname=request.json['firstname'],surname=request.json['surname'],
        middlename=request.json['middlename'],email=request.json['email'],telephone=request.json['telephone'],
        age=request.json['age'],
        gender=request.json['gender'],language = request.json['language'],maritalstatus=request.json['maritalstatus'],
        bankname = request.json['bankname'],accountno = request.json['accountno'],bvn=request.json['bvn'],
        meansofid=request.json['meansofid'],issuedate=request.json['issuedate'],expirydate=request.json['expirydate'],
        nin=request.json['nin'],permanentaddress=request.json['permanentaddress'],landmark=request.json['landmark'],
        stateoforigin=request.json['stateoforigin'],isinagroup = request.json['isinagroup'],
        reasonnogroup = request.json['reasonnogroup'],group=request.json['group'],
        numberofmembers = request.json['numberofmembers'],firstnamenok = request.json['firstnamenok'],
        surnamenok = request.json['surnamenok'],middlenamenok = request.json['middlenamenok'], 
        relationshipnok = request.json['relationshipnok'],occupationnok     = request.json['occupationnok'],
        telephonenok  = request.json['telephonenok'],permanentaddressnok  = request.json['permanentaddressnok'],
        landmarknok  = request.json['landmarknok'],ninnok  = request.json['ninnok'])
            db.session.add(farmerkyf)
            db.session.commit()
            message = {"error":False,"message":"success"}
        return message

# -------------5cs of Credit Scoring-------------------------------------------------------------------------------------

# 1.capital

class AddCapital(Resource):	
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmercapital = CapitalTable(bvn=request.json['bvn'],mainincomesource=request.json['mainincomesource'],
        otherincomesource=request.json['otherincomesource'],noofincomeearners=request.json['noofincomeearners'],
        hasbankaccount=request.json['hasbankaccount'],firstfundingoption=request.json['firstfundingoption'],
        needsaloan=request.json['needsaloan'],paybackmonths=request.json['paybackmonths'],
        harvestqtychanged=request.json['harvestqtychanged'],pestexpensechanged=request.json['pestexpensechanged'])
            db.session.add(farmercapital)
            db.session.commit()
            return {"error":False,"message":"success"}
        
class AddCreditAccess(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CreditAccessTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
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
            return {"error":False,"message":"success"}


class AddCapital5c(Resource):	
    def post(self):
        farmercapital = CapitalTable(bvn=request.json['bvn'],mainincomesource=request.json['mainincomesource'],
        otherincomesource=request.json['otherincomesource'],noofincomeearners=request.json['noofincomeearners'],
        hasbankaccount=request.json['hasbankaccount'],firstfundingoption=request.json['firstfundingoption'],
        needsaloan=request.json['needsaloan'],paybackmonths=request.json['paybackmonths'],
        harvestqtychanged=request.json['harvestqtychanged'],pestexpensechanged=request.json['pestexpensechanged'])
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
        # Add data only if Id does not exist in database already
        farmer = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in capital"})     
        else:
            db.session.add(farmercapital)
            db.session.commit()
        # Add data only if Id does not exist in database already
        farmer = CreditAccessTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in Credit Access"})
        else:
            db.session.add(farmercreditaccess)
            db.session.commit()
        return {"error":False,"message":"success"}


# 2.character

class AddCreditHistory(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CreditHistoryTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmercredithistory = CreditHistoryTable(bvn=request.json['bvn'],
        hastakenloanbefore=request.json['hastakenloanbefore'],sourceofloan=request.json['sourceofloan'],
        pastloanamount=request.json['pastloanamount'],howloanwasrepaid=request.json['howloanwasrepaid'],
        isreadytopayinterest=request.json['isreadytopayinterest'],canprovidecollateral=request.json['canprovidecollateral'],
        whynocollateral=request.json['whynocollateral'])
            db.session.add(farmercredithistory)
            db.session.commit()
            return farmercredithistory.json()

class AddProductivityViability(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = ProductivityViabilityTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmerproductivity = ProductivityViabilityTable(bvn=request.json['bvn'],
        cropscultivated=request.json['cropscultivated'],growscrops=request.json['growscrops'],
        oilpalmfertilizers=request.json['oilpalmfertilizers'],cocoafertilizers=request.json['cocoafertilizers'],
        fertilizerfrequency=request.json['fertilizerfrequency'],pestfungherbicides=request.json['pestfungherbicides'],
        stagechemicalapplied=request.json['stagechemicalapplied'],noofoildrums=request.json['noofoildrums'],
        noofbagssesame=request.json['noofbagssesame'],noofbagssoyabeans=request.json['NoOfBagsSoyaBeans'],
        noofbagsmaize=request.json['noofbagsmaize'],noofbagssorghum=request.json['noofbagssorghum'],
        noofbagscocoabeans=request.json['noofbagscocoabeans'],croptrainedon=request.json['croptrainedon'],
        wherewhenwhotrained=request.json['wherewhenwhotrained'],nooftraining=request.json['nooftraining'],
        pruningfrequency=request.json['pruningfrequency'],cropbasedproblems=request.json['cropbasedproblems'],
        tooyoungcrops=request.json['tooyoungcrops'],youngcropsandstage=request.json['youngcropsandstage'],
        cultivationstartdate=request.json['cultivationstartdate'],isintensivefarmingpractised=request.json['isintensivefarmingpractised'],
        economicactivities=request.json['economicactivities'])
            db.session.add(farmerproductivity)
            db.session.commit()
            return farmerproductivity.json()

class AddAgronomyServices(Resource):	
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = AgronomyServicesTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmeragronomy = AgronomyServicesTable(bvn=request.json['bvn'],
        knowsagriprocessed=request.json['knowsagriprocessed'],agronomistthattrainedyou=request.json['agronomistthattrainedyou'],
        canmanageecosystem=request.json['canmanageecosystem'],howtomanageecosystem=request.json['howtomanageecosystem'],
        istrainingbeneficial=request.json['istrainingbeneficial'],fieldroutines=request.json['fieldroutines'],
        harvestingchanges=request.json['harvestingchanges'],iscropcalendarbeneficial=request.json['iscropcalendarbeneficial'],
        cropcalendarbenefits=request.json['cropcalendarbenefits'],recordkeepingbenefits=request.json['recordkeepingbenefits'])
            db.session.add(farmeragronomy)
            db.session.commit()
            return farmeragronomy.json()
class AddPsychometrics(Resource):	
    def post(self):
        farmer = PsychometricsTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmerpsychometrics = PsychometricsTable(bvn=request.json['bvn'],fluidintelligence=request.json['fluidintelligence'],
        attitudesandbeliefs=request.json['attitudesandbeliefs'],agribusinessskills=request.json['agribusinessskills'],
        ethicsandhonesty=request.json['ethicsandhonesty'],savesenough=request.json['savesenough'],
        haslazyneighbors=request.json['haslazyneighbors'])
            db.session.add(farmerpsychometrics)
            db.session.commit()
            return farmerpsychometrics.json()

class AddMobileData(Resource):	
    def post(self):
        farmer = MobileDataTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmermobiledata = MobileDataTable(bvn=request.json['bvn'],mobilephonetype=request.json['mobilephonetype'],
        avweeklyphoneuse=request.json['avweeklyphoneuse'],callsoutnumber=request.json['callsoutnumber'],
        callsoutminutes=request.json['callsoutminutes'],callsinnumber=request.json['callsinnumber'],
        callinminutes=request.json['callinminutes'],SMSsent=request.json['SMSsent'],
        dataprecedingplanswitch=request.json['dataprecedingplanswitch'],billpaymenthistory=request.json['billpaymenthistory'],
        avweeklydatarefill=request.json['avweeklydatarefill'],noOfmobileapps=request.json['noOfmobileapps'],
        avtimespentonapp=request.json['avtimespentonapp'],mobileappkinds=request.json['mobileappkinds'],
        appdeleterate=request.json['appdeleterate'])
            db.session.add(farmermobiledata)
            db.session.commit()
            return farmermobiledata.json()


class AddCharacter5c(Resource):
    def post(self):
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
        noofbagssesame=request.json['noofbagssesame'],NoOfBagsSoyaBeans=request.json['NoOfBagsSoyaBeans'],
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
        callinminutes=request.json['callinminutes'],SMSsent=request.json['SMSsent'],
        dataprecedingplanswitch=request.json['dataprecedingplanswitch'],billpaymenthistory=request.json['billpaymenthistory'],
        avweeklydatarefill=request.json['avweeklydatarefill'],noOfmobileapps=request.json['noOfmobileapps'],
        avtimespentonapp=request.json['avtimespentonapp'],mobileappkinds=request.json['mobileappkinds'],
        appdeleterate=request.json['appdeleterate'])
        # Add data only if Id does not exist in database already
        farmer = CreditHistoryTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in CreditHistoryTable"})
        else:
            db.session.add(farmercredithistory)
        farmer = ProductivityViabilityTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in ProductivityViabilityTable"})
        else:
            db.session.add(farmerproductivity)
        farmer = AgronomyServicesTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in AgronomyServicesTable"})
        else:
            db.session.add(farmeragronomy)
        farmer = PsychometricsTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in PsychometricsTable"})
        else:
            db.session.add(farmerpsychometrics)
        farmer = MobileDataTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in MobileDataTable"})
        else:
            db.session.add(farmermobiledata)
        db.session.commit()
        return {"error":False,"message":"success"}


# 3.collateral

class AddFarmlandData(Resource):	
    def post(self):
        farmer = FarmlandTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmerland = FarmlandTable(bvn=request.json['bvn'],nooffarmlands=request.json['nooffarmlands'],
        ownerorcaretaker=request.json['ownerorcaretaker'],farmownername=request.json['farmownername'],
        FarmOwnerPhoneNo=request.json['FarmOwnerPhoneNo'],relationshipwithowner=request.json['relationshipwithowner'],
        inheritedfrom=request.json['inheritedfrom'],sizeoffarm=request.json['sizeoffarm'],
        farmcoordinates=request.json['farmcoordinates'],farmaddress=request.json['farmaddress'],
        keepsanimals=request.json['keepsanimals'],animalsfeedon=request.json['animalsfeedon'])
            db.session.add(farmerland)
            db.session.commit()
            return farmerland.json()

class AddCollateral5c(Resource):	
    def post(self):
        farmerland = FarmlandTable(bvn=request.json['bvn'],nooffarmlands=request.json['nooffarmlands'],
        ownerorcaretaker=request.json['ownerorcaretaker'],farmownername=request.json['farmownername'],
        FarmOwnerPhoneNo=request.json['FarmOwnerPhoneNo'],relationshipwithowner=request.json['relationshipwithowner'],
        inheritedfrom=request.json['inheritedfrom'],sizeoffarm=request.json['sizeoffarm'],
        farmcoordinates=request.json['farmcoordinates'],farmaddress=request.json['farmaddress'],
        keepsanimals=request.json['keepsanimals'],animalsfeedon=request.json['animalsfeedon'])

        farmer = FarmlandTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerland)
        db.session.commit()
        return {"error":False,"message":"success"}

#  4.capacity

class AddCapacity(Resource):	
    def post(self):
        farmer = CapacityTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmercapacity = CapacityTable(bvn=request.json['bvn'],
        howlongbeenfarming=request.json['howlongbeenfarming'],participatedintraining=request.json['participatedintraining'],
        farmingpractice=request.json['farmingpractice'],keepsanimals=request.json['keepsanimals'],
        hascooperative=request.json['hascooperative'],cooperativename=request.json['cooperativename'],
        educationlevel=request.json['educationlevel'])
            db.session.add(farmercapacity)
            db.session.commit()
            return {"error":False,"message":"success","data":farmercapacity.json()}

class AddFarmPractice(Resource):	
    def post(self):
        farmer = FarmPractice.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmerpractice = FarmPractice(bvn=request.json['bvn'],sizeoffarm=request.json['sizeoffarm'],
        farmisrentedorleased=request.json['farmisrentedorleased'],noofyearsleased=request.json['noofyearsleased'],
        usesmachines=request.json['usesmachines'],rotatescrops=request.json['rotatescrops'],
        noOfhectaresproducedyearly=request.json['noOfhectaresproducedyearly'],approxfertilizeruse=request.json['approxfertilizeruse'],
        nooffertlizerapplications=request.json['nooffertlizerapplications'],decisionforspraying=request.json['decisionforspraying'],
        weedcontrolpractice=request.json['weedcontrolpractice'],estimatedincomepercrop=request.json['estimatedincomepercrop'],
        cropthatcansellwell=request.json['cropthatcansellwell'],hasfarmplanorproject=request.json['hasfarmplanorproject'],
        FarmProjectInfo=request.json['FarmProjectInfo'])
            db.session.add(farmerpractice)
            db.session.commit()
            return {"error":False,"message":"success","data":farmerpractice.json()}

class AddMechanization(Resource):	
    def post(self):
        farmer = MechanizationTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmermechanization = MechanizationTable(bvn=request.json['bvn'],
        machinesused=request.json['machinesused'],machinehashelped=request.json['machinehashelped'],
        advisemachineorlabour=request.json['advisemachineorlabour'],othermachinesneeded=request.json['othermachinesneeded'],
        canacquiremorelands=request.json['canacquiremorelands'],percentcostsaved=request.json['percentcostsaved'])
            db.session.add(farmermechanization)
            db.session.commit()
            return {"error":False,"message":"success","data":farmermechanization.json()}

class AddCultivation(Resource):	
    def post(self):
        farmer = CultivationTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmercultivation = CultivationTable(bvn=request.json['bvn'],type_of_labor=request.json['type_of_labor'],
        pay_for_labor=request.json['pay_for_labor'],how_many_housechildren_help=request.json['how_many_housechildren_help'],
        season_children_help=request.json['season_children_help'],labor_children_do=request.json['labor_children_do'],
        household_vs_hire_cost=request.json['household_vs_hire_cost'],labor_women_do=request.json['labor_women_do'],
        percent_female_hired=request.json['percent_female_hired'])
            db.session.add(farmercultivation)
            db.session.commit()
            return {"error":False,"message":"success","data":farmercultivation.json()}

class AddHarvest(Resource):	
    def post(self):
        farmer = HarvestTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists"}
        else:
            farmerharvest = HarvestTable(bvn=request.json['bvn'],when_is_harvest_season=request.json['when_is_harvest_season'],
        no_of_hired_workers=request.json['no_of_hired_workers'],no_of_family_workers=request.json['no_of_family_workers'],
        no_of_permanent_workers=request.json['no_of_permanent_workers'],no_hired_constantly=request.json['no_hired_constantly'])
            db.session.add(farmerharvest)
            db.session.commit()
            return {"error":False,"message":"success","data":farmerharvest.json()}

class AddCapacity5c(Resource):	
    def post(self):
        farmercapacity = CapacityTable(bvn=request.json['bvn'],
        howlongbeenfarming=request.json['howlongbeenfarming'],participatedintraining=request.json['participatedintraining'],
        farmingpractice=request.json['farmingpractice'],keepsanimals=request.json['keepsanimals'],
        hascooperative=request.json['hascooperative'],cooperativename=request.json['cooperativename'],
        educationlevel=request.json['educationlevel'])
        farmerpractice = FarmPractice(bvn=request.json['bvn'],sizeoffarm=request.json['sizeoffarm'],
        farmisrentedorleased=request.json['farmisrentedorleased'],noofyearsleased=request.json['noofyearsleased'],
        usesmachines=request.json['usesmachines'],rotatescrops=request.json['rotatescrops'],
        noOfhectaresproducedyearly=request.json['noOfhectaresproducedyearly'],approxfertilizeruse=request.json['approxfertilizeruse'],
        nooffertlizerapplications=request.json['nooffertlizerapplications'],decisionforspraying=request.json['decisionforspraying'],
        weedcontrolpractice=request.json['weedcontrolpractice'],estimatedincomepercrop=request.json['estimatedincomepercrop'],
        cropthatcansellwell=request.json['cropthatcansellwell'],hasfarmplanorproject=request.json['hasfarmplanorproject'],
        FarmProjectInfo=request.json['FarmProjectInfo'])
        farmermechanization = MechanizationTable(bvn=request.json['bvn'],
        machinesused=request.json['machinesused'],machinehashelped=request.json['machinehashelped'],
        advisemachineorlabour=request.json['advisemachineorlabour'],othermachinesneeded=request.json['othermachinesneeded'],
        canacquiremorelands=request.json['canacquiremorelands'],percentcostsaved=request.json['percentcostsaved'])
        farmercultivation = CultivationTable(bvn=request.json['bvn'],type_of_labor=request.json['type_of_labor'],
        pay_for_labor=request.json['pay_for_labor'],how_many_housechildren_help=request.json['how_many_housechildren_help'],
        season_children_help=request.json['season_children_help'],labor_children_do=request.json['labor_children_do'],
        household_vs_hire_cost=request.json['household_vs_hire_cost'],labor_women_do=request.json['labor_women_do'],
        percent_female_hired=request.json['percent_female_hired'])
        farmerharvest = HarvestTable(bvn=request.json['bvn'],when_is_harvest_season=request.json['when_is_harvest_season'],
        no_of_hired_workers=request.json['no_of_hired_workers'],no_of_family_workers=request.json['no_of_family_workers'],
        no_of_permanent_workers=request.json['no_of_permanent_workers'],no_hired_constantly=request.json['no_hired_constantly'])

        farmer = CapacityTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercapacity)
        
        farmer = FarmPractice.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerpractice)
        
        farmer = MechanizationTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmermechanization)
        
        farmer = CultivationTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercultivation)
        
        farmer = HarvestTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerharvest)
            db.session.commit()
            return {"error":False,"message":"success"}



# 5.Condition
class AddConditions(Resource):	
    def post(self):
        farmercondition = ConditionsTable(bvn=request.json['bvn'],duration=request.json['duration'],
        seller=request.json['seller'],seller_mou=request.json['seller_mou'])
        
        farmer = ConditionsTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercondition)
            db.session.commit()
        return {"error":False,"message":"success","data":farmercondition.json()}

class AddConditions5c(Resource):	
    def post(self):
        farmercondition = ConditionsTable(bvn=request.json['bvn'],
        duration=request.json['duration'],seller=request.json['seller'],seller_mou=request.json['seller_mou'])
        
        farmer = ConditionsTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercondition)
            db.session.commit()
        return {"error":False,"message":"success","data":farmercondition.json()}


class AddScoreAnalytics(Resource):	
    def post(self):
        new_data = ScoreAnalytics(bvn=request.json['bvn'],scores=request.json['scores'],
        conditions=request.json['conditions'],capital=request.json['capital'],collateral=request.json['collateral'],
        capacity=request.json['capacity'],character=request.json['character'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}



# Sustainability

class AddCareTable(Resource):	
    def post(self):
        new_data = CareTable(bvn=request.json['bvn'],healthcentloc=request.json['healthcentloc'],
        healthcentcount=request.json['healthcentcount'],healthcentdistance=request.json['healthcentdistance'],
        healthcentfunctional=request.json['healthcentfunctional'],affordable=request.json['affordable'],
        farmdistance=request.json['farmdistance'],injuryevent=request.json['injuryevent'],firstaid=request.json['firstaid'],
        lastcheck=request.json['lastcheck'],inschool=request.json['inschool'],level=request.json['level'],
        schoolcount=request.json['schoolcount'],schoolfunctional=request.json['schoolfunctional'],
        qualification=request.json['qualification'],studytime=request.json['studytime'],
        studywhere=request.json['studywhere'],altIncomesource=request.json['altIncomesource'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}


class AddPlanet(Resource):	
    def post(self):
        new_data = Planet(bvn=request.json['bvn'],plantoexpand=request.json['plantoexpand'],crop=request.json['crop'],
        variety=request.json['variety'],raiseorbuy=request.json['raiseorbuy'],buywhere=request.json['buywhere'],
        seedlingprice=request.json['seedlingprice'],qtybought=request.json['qtybought'],degradedland=request.json['degradedland'],
        croprotation=request.json['croprotation'],season=request.json['season'],disaster=request.json['disaster'],
        burning=request.json['burning'],mill=request.json['mill'],energysource=request.json['energysource'],replacedtree=request.json['replacedtree'],
        placement=request.json['placement'],sourceofwater=request.json['sourceofwater'],covercrops=request.json['covercrops'],
        intercrop=request.json['intercrop'],cropintercropped=request.json['cropintercropped'],wastemgt=request.json['wastemgt'],
        wastedisposal=request.json['wastedisposal'],recyclewaste=request.json['recyclewaste'],suffered=request.json['suffered'],
        whensuffered=request.json['whensuffered'],greywater=request.json['greywater'],recyclegreywater=request.json['recyclegreywater'],
        pollution=request.json['pollution'],pollutionfreq=request.json['pollutionfreq'],measures=request.json['measures'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}


class AddSafety(Resource):	
    def post(self):
        new_data = Safety(bvn=request.json['bvn'],ferment=request.json['ferment'],
        fermentdays=request.json['fermentdays'],fermentreason=request.json['fermentreason'],brokenqty=request.json['brokenqty'],
        dowithbroken=request.json['dowithbroken'],unripeqty=request.json['unripeqty'],dowithunripe=request.json['dowithunripe'],
        cocoastore=request.json['cocoastore'],ffbstore=request.json['ffbstore'],herbicide=request.json['herbicide'],
        herbicidestore=request.json['herbicidestore'],agrochemsource=request.json['agrochemsource'],harvesttool=request.json['harvesttool'],
        wear=request.json['wear'],disposal=request.json['disposal'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}

class AddLivingTable(Resource):	
    def post(self):
        new_data = LivingTable(bvn=request.json['bvn'],houseowned=request.json['houseowned'],
        stayswithfamily=request.json['stayswithfamily'],relationshipwithowner=request.json['relationshipwithowner'],
        householdeats=request.json['householdeats'],maleunderage=request.json['maleunderage'],
        femaleunderage=request.json['femaleunderage'],childrenunderage=request.json['childrenunderage'],
        maleaboveage=request.json['maleaboveage'],femaleaboveage=request.json['femaleaboveage'],
        childrenaboveage=request.json['childrenaboveage'],liveswith=request.json['liveswith'],ownotherlands=request.json['ownotherlands'],
        standardofliving=request.json['standardofliving'],sourceofwater=request.json['sourceofwater'],
        sourceeverytime=request.json['sourceeverytime'],cookingmethod=request.json['cookingmethod'],
        haveelectricity=request.json['haveelectricity'],powerpayment=request.json['powerpayment'],typeoftoilet=request.json['typeoftoilet'],
        kitchensink=request.json['kitchensink'],hasgroup=request.json['hasgroup'],group=request.json['group'],
        position=request.json['position'],hasaccessedInput=request.json['hasaccessedInput'],input=request.json['input'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}

# Traceability

class AddCropInfo(Resource):	
    def post(self):
        new_data = CropInfo(tracing_id=request.json['tracing_id'],crop_type=request.json['crop_type'],sourcing_location=request.json['sourcing_location'],
        crop_origin=request.json['crop_origin'],crop_qty=request.json['crop_qty'],crop_variety=request.json['crop_variety'],
        cooperative=request.json['cooperative'],no_of_farmer_group=request.json['no_of_farmer_group'],
        female_to_male=request.json['female_to_male'],farmer_name=request.json['farmer_name'],gender=request.json['gender'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}


class AddCropQuality(Resource):	
    def post(self):
        new_data = CropQuality(tracing_id=request.json['tracing_id'],moisture_content=request.json['moisture_content'],
        foreign_matter=request.json['foreign_matter'],test_weight=request.json['test_weight'],quality=request.json['quality'],
        rotten_shriveled=request.json['rotten_shriveled'],hardness=request.json['hardness'],splits=request.json['splits'],
        oil_content=request.json['oil_content'],infestation=request.json['infestation'],hectoliter=request.json['hectoliter'],
        total_defects=request.json['total_defects'],dockage=request.json['dockage'],ash_content=request.json['ash_content'],
        insoluble_ash=request.json['insoluble_ash'],volatile=request.json['volatile'],mold_weight=request.json['mold_weight'],
        drying_process=request.json['drying_process'],dead_insects=request.json['dead_insects'],excreta=request.json['excreta'],
        insect_defiled=request.json['insect_defiled'],curcumin=request.json['curcumin'],extraneous=request.json['extraneous'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}


class AddInputsInfo(Resource):	
    def post(self):
        new_data = InputsInfo(tracing_id=request.json['tracing_id'],fertilizers=request.json['fertilizers'],herbicides=request.json['herbicides'],
        fungicides=request.json['fungicides'],insecticides=request.json['insecticides'],seeds=request.json['seeds'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}


class AddWarehouse(Resource):	
    def post(self):
        new_data = Warehouse(tracing_id=request.json['tracing_id'],location=request.json['location'],warehouse_type=request.json['warehouse_type'],
        capacity=request.json['capacity'],standard=request.json['standard'],insurance=request.json['insurance'],
        duration=request.json['duration'],cost=request.json['cost'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}

class AddShipment(Resource):	
    def post(self):
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
        return {"error":False,"message":"success","data":new_data.json()}

class AddRecommendation(Resource):	
    def post(self):
        new_data = Recommendation(tracing_id=request.json['tracing_id'],rec_one=request.json['rec_one'],
        rec_two=request.json['rec_two'],rec_three=request.json['rec_three'])
        db.session.add(new_data)
        db.session.commit()
        return {"error":False,"message":"success","data":new_data.json()}

class AddCropCard(Resource):	
    def post(self):
        card = Cropcard(bvn=request.json['bvn'],farmer_name=request.json['farmer_name'],
        crop_name=request.json['crop_name'],fertilizer_cost=request.json['fertilizer_cost'],
        fertilizer=request.json['fertilizer'],mechanization_cost=request.json['mechanization_cost'],
        mechanization=request.json['mechanization'], labour_cost=request.json['labour_cost'],
        labour=request.json['labour'],harvest_cost=request.json['harvest_cost'],
        harvest=request.json['harvest'],other_cost=request.json['other_cost'],
        others=request.json['others'],
        date_filled=request.json['date_filled'])
        db.session.add(card)
        db.session.commit()
        # upload loan amount
        bvn=request.json['bvn']
        farmer = ScoreCard.query.filter_by(bvn=bvn).first()
        if farmer:
            print(farmer.applyLoanAmount)
            farmer.applyLoanAmount = applyLoan(bvn)   
            print(farmer.applyLoanAmount)
            tdf = pd.DataFrame([['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits']],columns=['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits'])
            tdf['bvn'] = farmer.bvn
            tdf['age'] = farmer.age
            tdf['number_of_land'] = farmer.number_of_land
            tdf['address'] = farmer.address
            tdf['owner_caretaker'] = farmer.owner_caretaker
            tdf['crop'] = farmer.crop
            tdf['intercropping'] = farmer.intercropping
            tdf['machines'] = farmer.machines
            tdf['estimate_monthly_income'] = farmer.estimate_monthly_income
            tdf['years_cultivating'] = farmer.years_cultivating
            tdf['gender'] = farmer.gender
            tdf['owns_a_bank_account'] = farmer.owns_a_bank_account
            tdf['size_of_farm'] = farmer.size_of_farm
            tdf['number_of_crops'] = farmer.number_of_crops
            tdf['is_in_a_cooperative'] = farmer.is_in_a_cooperative
            tdf['no_of_agronomist_visits'] = farmer.no_of_agronomist_visits
            tdf['applyLoanAmount']=farmer.applyLoanAmount
            tdf = tdf.rename({
            'number_of_land':'numberOfLand','estimate_monthly_income':'estimateMonthlyIncome',
            'years_cultivating':'yearsCultivating'
        },axis=1)
            cols=['age', 'numberOfLand', 'owner_caretaker', 'crop','applyLoanAmount',
            'intercropping', 'machines', 'estimateMonthlyIncome','yearsCultivating']
            tdf = preprocess_df(tdf[cols])
            train_cols = ['number_of_land', 'owner_caretaker', 'intercropping', 'machines',
       'estimate_monthly_income', 'apply_loan_amount', 'years_cultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
            farmer.score = model.predict_proba(tdf[train_cols])[:,1].round(2)[0]
            farmer.bin=bin_target([farmer.score])[0]
            db.session.commit()
        return {"error":False,"message":"success"}
# Credit Scoring
class AddScoreCard(Resource):	
    def post(self):
        recommendations = 'Success'
        bvn=request.json['bvn']
        farmer = ScoreCard.query.filter_by(bvn=bvn).all()
        if farmer:
            recommendations+='Scorecard Exists'
        '''
        if not farmer:
            card = ScoreCard(bvn=request.json['bvn'],age=request.json['age'],
        number_of_land=request.json['number_of_land'],address=request.json['address'],
        owner_caretaker=request.json['owner_caretaker'],crop=request.json['crop'],
        intercropping=request.json['intercropping'], machines=request.json['machines'],
        estimate_monthly_income=request.json['estimate_monthly_income'],
        years_cultivating=request.json['years_cultivating'],gender=request.json['gender'],
        owns_a_bank_account=request.json['owns_a_bank_account'],size_of_farm=request.json['size_of_farm'],
        number_of_crops=request.json['number_of_crops'],is_in_a_cooperative=request.json['is_in_a_cooperative'],
        no_of_agronomist_visits=request.json['no_of_agronomist_visits'])
            db.session.add(card)
            db.session.commit()
        '''
        bvn=request.json['bvn']
        farmer = FarmerTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add KYF '
        farmer = CapitalTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add capital '
        farmer = CreditHistoryTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add character '
        farmer = FarmlandTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add collateral '
        farmer = CapacityTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add capacity '
        farmer = ConditionsTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add conditions'
        #return {"message":recommendations}
        
        farmer = ScoreCard.query.filter_by(bvn=bvn).all()
        if not farmer:
            farmer = pd.DataFrame([['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits']],columns=['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits'])
            for col in farmer.columns:
                farmer[col] = request.json[col]
            print(farmer)
            farmer['applyLoanAmount'] = applyLoan(bvn)
            farmer = farmer.rename({
            'number_of_land':'numberOfLand','estimate_monthly_income':'estimateMonthlyIncome',
            'years_cultivating':'yearsCultivating'
        },axis=1)
            cols=['age', 'numberOfLand', 'owner_caretaker', 'crop','applyLoanAmount',
            'intercropping', 'machines', 'estimateMonthlyIncome','yearsCultivating']
            tdf = preprocess_df(farmer[cols])
            train_cols = ['number_of_land', 'owner_caretaker', 'intercropping', 'machines',
       'estimate_monthly_income', 'apply_loan_amount', 'years_cultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
            score = model.predict_proba(tdf[train_cols])[:,1].round(2)
            bin=bin_target(score)
            history = ScoreCard(bvn=request.json['bvn'],age=request.json['age'],
        number_of_land=request.json['number_of_land'],address=request.json['address'],
        owner_caretaker=request.json['owner_caretaker'],crop=request.json['crop'],
        intercropping=request.json['intercropping'], machines=request.json['machines'],
        estimate_monthly_income=request.json['estimate_monthly_income'],
        years_cultivating=request.json['years_cultivating'],gender=request.json['gender'],
        owns_a_bank_account=request.json['owns_a_bank_account'],size_of_farm=request.json['size_of_farm'],
        number_of_crops=request.json['number_of_crops'],is_in_a_cooperative=request.json['is_in_a_cooperative'],
        no_of_agronomist_visits=request.json['no_of_agronomist_visits'],
        applyLoanAmount=farmer['applyLoanAmount'][0],
        score=score[0], bin=bin[0])
            db.session.add(history)
            db.session.commit()
        return jsonify({"error":False,"message":recommendations})

class Scorecardbvn(Resource):
    def get(self, bvn):
        cards = ScoreCard.query.filter_by(bvn=bvn).all()
        if cards:
            return {"error":False,"message":"success","data":[card.json() for card in cards]}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        cards = ScoreCard.query.filter_by(bvn=bvn).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return ({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"})
        

class Cropcardbvn(Resource):
    def get(self, bvn):
        cards = Cropcard.query.filter_by(bvn=bvn).all()
        if cards:
            return {"error":False,"message":"success","data":[card.json() for card in cards]}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        cards = Cropcard.query.filter_by(bvn=bvn).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return ({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"})
        
class Cropcardid(Resource):
    def get(self, id):
        cards = Cropcard.query.filter_by(id=id).all()
        if cards:
            return {"error":False,"message":"success","data":[card.json() for card in cards]}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}
    def delete(self, id):
        cards = Cropcard.query.filter_by(id=id).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return ({"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"})
        
class Cropcardcrop_name(Resource):
    def get(self, crop_name):
        cards = Cropcard.query.filter_by(crop_name=crop_name).all()
        if cards:
            return {"error":False,"message":"success","data":[card.json() for card in cards]}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"crop_name not found"}
    def delete(self, crop_name):
        cards = Cropcard.query.filter_by(crop_name=crop_name).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return ({"error":True,"message":"Sorry your request can not be processed at the moment","data":"crop_name not found"})
        
'''
class ScoreHistorybvn(Resource):
    def get(self, bvn):
        farmer = ScoreHistory.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = ScoreHistory.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return ({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"})
        
'''
class Scorecardid(Resource):
    def get(self, id):
        farmer = ScoreCard.query.filter_by(id=id).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}
    def delete(self, id):
        farmer = ScoreCard.query.filter_by(id=id).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return ({"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"})
        

'''
class ScoreFarmer(Resource):
    def post(self):
        bvn=request.json['bvn']
        #applyLoanAmount=request.json['applyLoanAmount']
        farmer = ScoreCard.query.filter_by(bvn=bvn).first()
        cols=['age', 'number_of_land', 'owner_caretaker', 'crop',
            'intercropping', 'machines', 'estimate_monthly_income','years_cultivating']
        if farmer:
            farmer=farmer.json()
            farmer = pd.DataFrame(farmer, index=[0])
            tdf = preprocess_df(farmer[cols])
            train_cols = ['number_of_land', 'owner_caretaker', 'intercropping', 'machines',
       'estimate_monthly_income', 'applyLoanAmount', 'years_cultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
            score = model.predict_proba(tdf[train_cols])[:,1]
            bin=bin_target(score)
            history = ScoreHistory(bvn=farmer['bvn'],age=farmer['age'],
        number_of_land=farmer['number_of_land'],address=farmer['address'],
        owner_caretaker=farmer['owner_caretaker'],crop=farmer['crop'],
        intercropping=request.json['intercropping'], machines=farmer['machines'],
        estimate_monthly_income=farmer['estimate_monthly_income'],
        years_cultivating=farmer['years_cultivating'],gender=farmer['gender'],
        owns_a_bank_account=farmer['owns_a_bank_account'],size_of_farm=farmer['size_of_farm'],
        number_of_crops=farmer['number_of_crops'],is_in_a_cooperative=farmer['is_in_a_cooperative'],
        no_of_agronomist_visits=farmer['no_of_agronomist_visits'],
        applyLoanAmount=request.json['applyLoanAmount'],
        score=score, bin=bin)
            db.session.add(history)
            db.session.commit()
            return {'bvn':bvn, 'score':score, 'bin':bin }
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class ScoreFarmerDragAndDrop(Resource):
    def post(self):
        bvn=request.json['bvn']
        applyLoanAmount=request.json['applyLoanAmount']
        features=request.json['features']
        features = list(features)
        farmer = ScoreCard.query.filter_by(bvn=bvn).first()
        cols=['age', 'number_of_land', 'owner_caretaker', 'crop',
            'intercropping', 'machines', 'estimate_monthly_income','years_cultivating']
        if farmer:
            farmer=farmer.json()
            farmer = pd.DataFrame(farmer, index=[0])
        for col in cols:
            if col not in features:
                farmer[col] = np.nan
            tdf = preprocess_df(farmer[cols])
            train_cols = ['number_of_land', 'owner_caretaker', 'intercropping', 'machines',
       'estimate_monthly_income', 'applyLoanAmount', 'years_cultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
            score = model.predict_proba(tdf[train_cols])[:,1]
            bin=bin_target(score)
            history = ScoreHistory(bvn=farmer['bvn'],age=farmer['age'],
        number_of_land=farmer['number_of_land'],address=farmer['address'],
        owner_caretaker=farmer['owner_caretaker'],crop=farmer['crop'],
        intercropping=request.json['intercropping'], machines=farmer['machines'],
        estimate_monthly_income=farmer['estimate_monthly_income'],
        years_cultivating=farmer['years_cultivating'],gender=farmer['gender'],
        owns_a_bank_account=farmer['owns_a_bank_account'],size_of_farm=farmer['size_of_farm'],
        number_of_crops=farmer['number_of_crops'],is_in_a_cooperative=farmer['is_in_a_cooperative'],
        no_of_agronomist_visits=farmer['no_of_agronomist_visits'],
        applyLoanAmount=request.json['applyLoanAmount'],
       score=score, bin=bin)
            db.session.add(history)
            db.session.commit()
            return {'bvn':bvn, 'score':score, 'bin':bin }
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
'''
# Market

class AddBuyersDailyPrice(Resource):	
    def post(self):
        new_data = BuyersDailyPrice(
        crop=request.json['crop'],
        location=request.json['location'],
        classification=request.json['classification'],
        min_price=request.json['min_price'],
        max_price=request.json['max_price'],
        ave_price=request.json['ave_price'],
        quality_spec=request.json['quality_spec'],
        date_filled=request.json['date_filled']
        )
        db.session.add(new_data)
        db.session.commit()
        message = {"error":False,"message":"success"}
        return message

class AddBuyersOffers(Resource):	
    def post(self):
        new_data = BuyersOffers(
        crop=request.json['crop'],
        location=request.json['location'],
        classification=request.json['classification'],
        min_price=request.json['min_price'],
        max_price=request.json['max_price'],
        ave_price=request.json['ave_price'],
        quality_spec=request.json['quality_spec'],
        date_filled=request.json['date_filled']
        )
        db.session.add(new_data)
        db.session.commit()
        message = {"error":False,"message":"success"}
        return message   

class AddFarmGatePrices(Resource):	
    def post(self):
        new_data = FarmGatePrices(
        crop=request.json['crop'],
        location=request.json['location'],
        classification=request.json['classification'],
        min_price=request.json['min_price'],
        max_price=request.json['max_price'],
        ave_price=request.json['ave_price'],
        quality_spec=request.json['quality_spec'],
        date_filled=request.json['date_filled']
        )
        db.session.add(new_data)
        db.session.commit()
        message = {"error":False,"message":"success"}
        return message  

class AddMarketPrices(Resource):	
    def post(self):
        new_data = MarketPrices(
        crop=request.json['crop'],
        location=request.json['location'],
        classification=request.json['classification'],
        min_price=request.json['min_price'],
        max_price=request.json['max_price'],
        ave_price=request.json['ave_price'],
        quality_spec=request.json['quality_spec'],
        date_filled=request.json['date_filled']
        )
        db.session.add(new_data)
        db.session.commit()
        message = {"error":False,"message":"success"}
        return message    
class BuyersDailyPriceid(Resource):
    def get(self, id):
        price = BuyersDailyPrice.query.filter_by(id=id).first()
        if price:
            return price.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}
    def delete(self, id):
        price = BuyersDailyPrice.query.filter_by(id=id).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":"success"}
class BuyersOffersid(Resource):
    def get(self, id):
        price = BuyersOffers.query.filter_by(id=id).first()
        if price:
            return price.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}
    def delete(self, id):
        price = BuyersOffers.query.filter_by(id=id).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":"success"}
class FarmGatePricesid(Resource):
    def get(self, id):
        price = FarmGatePrices.query.filter_by(id=id).first()
        if price:
            return price.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}
    def delete(self, id):
        price = FarmGatePrices.query.filter_by(id=id).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":"success"}
class MarketPricesid(Resource):
    def get(self, id):
        price = MarketPrices.query.filter_by(id=id).first()
        if price:
            return price.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}
    def delete(self, id):
        price = MarketPrices.query.filter_by(id=id).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":"success"}



class BuyersDailyPricecrop(Resource):
    def get(self, crop):
        price = BuyersDailyPrice.query.filter_by(crop=crop).all()
        if price:
            all_prices = [prices.json() for prices in price]
            return jsonify({"error":False,"message":"success","data": all_prices})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"crop not found"}
    def delete(self, crop):
        price = BuyersDailyPrice.query.filter_by(crop=crop).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":"success"}
class BuyersOfferscrop(Resource):
    def get(self, crop):
        price = BuyersOffers.query.filter_by(crop=crop).all()
        if price:
            all_prices = [prices.json() for prices in price]
            return jsonify({"error":False,"message":"success","data": all_prices})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"crop not found"}
    def delete(self, crop):
        price = BuyersOffers.query.filter_by(crop=crop).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":"success"}
class FarmGatePricescrop(Resource):
    def get(self, crop):
        price = FarmGatePrices.query.filter_by(crop=crop).all()
        if price:
            all_prices = [prices.json() for prices in price]
            return jsonify({"error":False,"message":"success","data":all_prices})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"crop not found"}
    def delete(self, crop):
        price = FarmGatePrices.query.filter_by(crop=crop).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":"success"}
class MarketPricescrop(Resource):
    def get(self, crop):
        price = MarketPrices.query.filter_by(crop=crop).all()
        if price:
            all_prices = [prices.json() for prices in price]
            return jsonify({"error":False,"message":"success","data": all_prices})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"crop not found"}
    def delete(self, crop):
        price = MarketPrices.query.filter_by(crop=crop).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":"success"}
# Loans

class AddLoan(Resource):	
    def post(self):
        type=request.json['type']
        loan = Loan.query.filter_by(type=type).first()
        if loan:
            message = {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Loan type already exists"}
        if not loan:
            new_data = Loan(
        type=request.json['type'],
        company=request.json['company'],
        repayment_months=request.json['repayment_months'],
        interest_rate_per_annum=request.json['interest_rate_per_annum']
        )
            db.session.add(new_data)
            db.session.commit()
            message = {"error":False,"message":"success"}
        return message


class AddLoanTransfer(Resource):	
    def post(self):
        type = request.json['type']
        bvn=request.json['bvn']
        loan = Loan.query.filter_by(type=type).first()
        if not loan:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Loan type not found"}
        farmer = ScoreCard.query.filter_by(bvn=bvn).first()
        if not farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Farmer not found"}
        if farmer:
            if loan:
                new_data = LoanTransfer(type=type,company=loan.company,
                amount=farmer.applyLoanAmount,group=farmer.is_in_a_cooperative,
                score=farmer.score,bin=farmer.bin,
                repayment_amount=float(farmer.applyLoanAmount)*(((loan.interest_rate_per_annum*(loan.repayment_months/12))+100)/100),
                status='Offered',bvn=bvn,repayment_months=loan.repayment_months,
                repaid = 0, balance = 0,transfer_date='Pending',due_date='Pending')
                db.session.add(new_data)
                db.session.commit()
                return {"error":False,"message":"success","data":new_data.json()}
                


class AcceptTransfer(Resource):	
    def get(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            loan.status = 'Accepted'
            loan.balance = loan.repayment_amount
            loan.transfer_date = datetime.now()
            x=int(loan.repayment_months)
            loan.due_date = datetime.now() + relativedelta(months=+x)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}

class RejectTransfer(Resource):	
    def get(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            loan.status = 'Rejected'
            #loan.transfer_date = datetime.now()
            loan.due_date = 'Rejected'
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}

class UpdateTransfer(Resource):	
    def get(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            if loan.status == 'Accepted':
                loan.repaid = float(loan.repaid) + float(request.json['amount'])
                loan.balance = float(loan.balance) - float(request.json['amount'])
                loan.repaid = int(loan.repaid)
                loan.balance = int(loan.balance)
                if float(loan.balance)<=0:
                    loan.status = 'Cleared'
                db.session.commit()
                return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}

class Loantype(Resource):
    def get(self, type):
        loan = Loan.query.filter_by(type=type).first()
        if loan:
            return {"error":False,"message":"success","data":loan.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"type not found"}
    def delete(self, type):
        loan = Loan.query.filter_by(type=type).first()
        if loan:
            db.session.delete(loan)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"type not found"}
    
class Loancompany(Resource):
    def get(self, company):
        all_loans = Loan.query.filter_by(company=company).all()
        if all_loans:
            all_loans = [farmer.json() for farmer in all_loans]
            return jsonify({"error":False,"message":"success","data": all_loans})
            
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Company not found"}
    def delete(self, company):
        loan = Loan.query.filter_by(company=company).first()
        db.session.delete(loan)
        db.session.commit()
        return {"error":False,"message":"success"}

# -----------Traceability----------------------------------------------------------------------------------------

class CropInfoTracing(Resource):
    def get(self, tracing_id):
        farmer = CropInfo.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"tracing_id not found"}
    def delete(self, tracing_id):
        farmer = CropInfo.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {"error":False,"message":"success"}

class CropQualityTracing(Resource):
    def get(self, tracing_id):
        farmer = CropQuality.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"tracing_id not found"}
    def delete(self, tracing_id):
        farmer = CropQuality.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {"error":False,"message":"success"}

class ShipmentTracing(Resource):
    def get(self, tracing_id):
        farmer = Shipment.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"tracing_id not found"}
    def delete(self, tracing_id):
        farmer = Shipment.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {"error":False,"message":"success"}
class InputsInfoTracing(Resource):
    def get(self, tracing_id):
        farmer = InputsInfo.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"tracing_id not found"}
    def delete(self, tracing_id):
        farmer = InputsInfo.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {"error":False,"message":"success"}
class WarehouseTracing(Resource):
    def get(self, tracing_id):
        farmer = Warehouse.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"tracing_id not found"}
    def delete(self, tracing_id):
        farmer = Warehouse.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {"error":False,"message":"success"}
class RecommendationTracing(Resource):
    def get(self, tracing_id):
        farmer = Recommendation.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"tracing_id not found"}
    def delete(self, tracing_id):
        farmer = Recommendation.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {"error":False,"message":"success"}

# ------------Get Requests-------------------------------------------------------------------------------------------------

class Farmerbvn(Resource):
    def get(self, bvn):
        farmer = FarmerTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = FarmerTable.query.filter_by(bvn=bvn).first()
        if farmer:
            farmer = FarmerTable.query.filter_by(bvn=bvn).first()
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Farmertag(Resource):
    def get(self, tag):
        farmer = FarmerTable.query.filter_by(tag=tag).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"tag not found"}
    def delete(self, tag):
        farmer = FarmerTable.query.filter_by(tag=tag).first()
        if farmer:
            farmer = FarmerTable.query.filter_by(bvn=bvn).first()
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"tag not found"}
class Farmergroup(Resource):
    def get(self, group):
        all_farmers = FarmerTable.query.filter_by(group=group).all()
        if farmer:
            all_farmers = [farmer.json() for farmer in all_farmers]
            return jsonify({'error': False,'message': 'success','data': all_farmers})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Group not found"}
    def delete(self, group):
        farmer = FarmerTable.query.filter_by(group=group).all()
        if farmer:
            farmer = FarmerTable.query.filter_by(group=group).first()
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Group not found"}
    
class Agronomybvn(Resource):
    def get(self, bvn):
        farmer = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    

class Capacitybvn(Resource):
    def get(self, bvn):
        farmer = CapacityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = CapacityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Capitalbvn(Resource):
    def get(self, bvn):
        farmer = CapitalTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = CapitalTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Carebvn(Resource):
    def get(self, bvn):
        farmer = CareTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = CareTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Conditionsbvn(Resource):
    def get(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class ScoreAnalyticsbvn(Resource):
    def get(self, bvn):
        farmer = ScoreAnalytics.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = ScoreAnalytics.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class CreditAccessbvn(Resource):
    def get(self, bvn):
        farmer = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Capital5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CapitalTable.query.filter_by(bvn=bvn).first()
        farmer2 = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if not farmer1:
            farmer1={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer2=farmer2.json()
        return {"error":False,"message":"success","data":{'capital':farmer1,'creditaccess':farmer2}}
        
class Character5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        farmer2 = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        farmer3 = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        farmer4 = PsychometricsTable.query.filter_by(bvn=bvn).first()
        farmer5 = MobileDataTable.query.filter_by(bvn=bvn).first()
        
        if not farmer1:
            farmer1={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer2=farmer2.json()
        if not farmer3:
            farmer3={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer3=farmer3.json()
        if not farmer4:
            farmer4={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer4=farmer4.json()
        if not farmer5:
            farmer5={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer5=farmer5.json()
        return {"error":False,"message":"success","data":{'credithistory':farmer1,'productivity':farmer2,'agronomy':farmer3,'psychometrics':farmer4,'mobiledata':farmer5}}
        
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
        return {"error":False,"message":"success"}

class Collateral5cbvn(Resource):
    def get(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {'farmland':farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not in FarmlandTable"})
        return {"error":False,"message":"success"}
class Capacity5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CapacityTable.query.filter_by(bvn=bvn).first()
        farmer2 = FarmPractice.query.filter_by(bvn=bvn).first()
        farmer3 = MechanizationTable.query.filter_by(bvn=bvn).first()
        farmer4 = CultivationTable.query.filter_by(bvn=bvn).first()
        farmer5 = HarvestTable.query.filter_by(bvn=bvn).first()
        
        if not farmer1:
            farmer1={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer2=farmer2.json()
        if not farmer3:
            farmer3={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer3=farmer3.json()
        if not farmer4:
            farmer4={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer4=farmer4.json()
        if not farmer5:
            farmer5={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
        else:
            farmer5=farmer5.json()
        return {"error":False,"message":"success","data":{'capacity':farmer1,'practice':farmer2,'mechanization':farmer3,'cultivation':farmer4,'harvest':farmer5}}
        
    def delete(self, bvn):
        farmer1 = CapacityTable.query.filter_by(bvn=bvn).first()
        farmer2 = FarmPractice.query.filter_by(bvn=bvn).first()
        farmer3 = MechanizationTable.query.filter_by(bvn=bvn).first()
        farmer4 = CultivationTable.query.filter_by(bvn=bvn).first()
        farmer5 = HarvestTable.query.filter_by(bvn=bvn).first()
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
        return {"error":False,"message":"success"}
class Conditions5cbvn(Resource):
    def get(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":{'conditions':farmer.json()}}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not in FarmlandTable"})
        return {"error":False,"message":"success"}
class CreditHistorybvn(Resource):
    def get(self, bvn):
        farmer = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    

class Cultivationbvn(Resource):
    def get(self, bvn):
        farmer = CultivationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = CultivationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Farmlandbvn(Resource):
    def get(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Harvestbvn(Resource):
    def get(self, bvn):
        farmer = HarvestTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = HarvestTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Livingbvn(Resource):
    def get(self, bvn):
        farmer = LivingTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = LivingTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Mechanizationbvn(Resource):
    def get(self, bvn):
        farmer = MechanizationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = MechanizationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    

class MobileDatabvn(Resource):
    def get(self, bvn):
        farmer = MobileDataTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = MobileDataTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    

class Planetbvn(Resource):
    def get(self, bvn):
        farmer = Planet.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = Planet.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Practicebvn(Resource):
    def get(self, bvn):
        farmer = FarmPractice.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = FarmPractice.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    

class Productivitybvn(Resource):
    def get(self, bvn):
        farmer = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
    
class Psychometricsbvn(Resource):
    def get(self, bvn):
        farmer = PsychometricsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = PsychometricsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Safetybvn(Resource):
    def get(self, bvn):
        farmer = Safety.query.filter_by(bvn=bvn).first()
        if farmer:
            return {"error":False,"message":"success","data":farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = Safety.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    

class Transferbvn(Resource):
    def get(self, bvn):
        farmer = LoanTransfer.query.filter_by(bvn=bvn).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":"success","data": transfers})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    def delete(self, bvn):
        farmer = LoanTransfer.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn not found"}
    
class Transferid(Resource):
    def get(self, id):
        farmer = LoanTransfer.query.filter_by(id=id).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":"success","data": transfers})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}
    def delete(self, id):
        farmer = LoanTransfer.query.filter_by(id=id).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id not found"}
    
class Transfergroup(Resource):
    def get(self, group):
        farmer = LoanTransfer.query.filter_by(group=group).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":"success","data": transfers})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"group not found"}
    def delete(self, group):
        farmer = LoanTransfer.query.filter_by(group=group).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"group not found"}

class Transfercompany(Resource):
    def get(self, company):
        farmer = LoanTransfer.query.filter_by(company=company).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":"success","data": transfers})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"company not found"}
    def delete(self, company):
        farmer = LoanTransfer.query.filter_by(company=company).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"company not found"}
class Transferstatus(Resource):
    def get(self, status):
        farmer = LoanTransfer.query.filter_by(status=status).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":"success","data": transfers})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"status not found"}
    def delete(self, status):
        farmer = LoanTransfer.query.filter_by(status=status).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":"success"}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"status not found"}
   
# All Loans, Farmers, Prices


class AllBuyersDailyPrice(Resource):
    def get(self):
        price = BuyersDailyPrice.query.all() 
        price = [prices.json() for prices in price]
        return jsonify({"error":False,"message":"success","data": price})

class AllBuyersOffers(Resource):
    def get(self):
        price = BuyersOffers.query.all() 
        price = [prices.json() for prices in price]
        return jsonify({"error":False,"message":"success","data": price})

class AllFarmGatePrices(Resource):
    def get(self):
        price = FarmGatePrices.query.all() 
        price = [prices.json() for prices in price]
        return jsonify({"error":False,"message":"success","data": price})
class AllMarketPrices(Resource):
    def get(self):
        price = MarketPrices.query.all() 
        price = [prices.json() for prices in price]
        return jsonify({"error":False,"message":"success","data": price})
        
class AllFarmers(Resource):
    def get(self):
        all_farmers = FarmerTable.query.all()        
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})
        


class AllAgronomy(Resource):
    def get(self):
        all_farmers = AgronomyServicesTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllCapacity(Resource):
    def get(self):
        all_farmers = CapacityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllCapital(Resource):
    def get(self):
        all_farmers = CapitalTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllCare(Resource):
    def get(self):
        all_farmers = CareTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllConditions(Resource):
    def get(self):
        all_farmers = ConditionsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllScoreAnalytics(Resource):
    def get(self):
        all_farmers = ScoreAnalytics.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllCreditAccess(Resource):
    def get(self):
        all_farmers = CreditAccessTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})
class AllCapital5c(Resource):
    def get(self):
        all_farmer1 = CapitalTable.query.all()
        all_farmer1 = [farmer.json() for farmer in all_farmer1]
        all_farmer2 = CreditAccessTable.query.all()
        all_farmer2 = [farmer.json() for farmer in all_farmer2]
        return {'capital':all_farmer1,'creditaccess':all_farmer2}
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
        return {'credithistory':all_farmer1,'productivity':all_farmer2,'agronomy':all_farmer3,'psychometrics':all_farmer4,'mobiledata':all_farmer5}
class AllCollateral5c(Resource):
    def get(self):
        all_farmers = FarmlandTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return {'farmland':all_farmers}
class AllCapacity5c(Resource):
    def get(self):
        all_farmer1 = CapacityTable.query.all()
        all_farmer1 = [farmer.json() for farmer in all_farmer1]
        all_farmer2 = FarmPractice.query.all()
        all_farmer2 = [farmer.json() for farmer in all_farmer2]
        all_farmer3 = MechanizationTable.query.all()
        all_farmer3 = [farmer.json() for farmer in all_farmer3]
        all_farmer4 = CultivationTable.query.all()
        all_farmer4 = [farmer.json() for farmer in all_farmer4]
        all_farmer5 = HarvestTable.query.all()
        all_farmer5 = [farmer.json() for farmer in all_farmer5]
        return {'capacity':all_farmer1,'practice':all_farmer2,'mechanization':all_farmer3,'cultivation':all_farmer4,'harvest':all_farmer5}

class AllConditions5c(Resource):
    def get(self):
        all_farmers = ConditionsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return {'conditions':all_farmers}
class AllCreditHistory(Resource):
    def get(self):
        all_farmers = CreditHistoryTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllCropInfo(Resource):
    def get(self):
        all_farmers = CropInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllCropQuality(Resource):
    def get(self):
        all_farmers = CropQuality.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllCultivation(Resource):
    def get(self):
        all_farmers = CultivationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllFarmland(Resource):
    def get(self):
        all_farmers = FarmlandTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllHarvest(Resource):
    def get(self):
        all_farmers = HarvestTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllInputsInfo(Resource):
    def get(self):
        all_farmers = InputsInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllLiving(Resource):
    def get(self):
        all_farmers = LivingTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllMechanization(Resource):
    def get(self):
        all_farmers = MechanizationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllMobileData(Resource):
    def get(self):
        all_farmers = MobileDataTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllPlanet(Resource):
    def get(self):
        all_farmers = Planet.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllPractice(Resource):
    def get(self):
        all_farmers = FarmPractice.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllProductivity(Resource):
    def get(self):
        all_farmers = ProductivityViabilityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllPsychometrics(Resource):
    def get(self):
        all_farmers = PsychometricsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllRecommendation(Resource):
    def get(self):
        all_farmers = Recommendation.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllSafety(Resource):
    def get(self):
        all_farmers = Safety.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})
class AllScorecard(Resource):
    def get(self):
        all_farmers = ScoreCard.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})
class AllCropcard(Resource):
    def get(self):
        all_cards = Cropcard.query.all()
        all_cards = [farmer.json() for farmer in all_cards]
        return jsonify({"error":False,"message":"success","data": all_cards})

'''
class AllScoreHistory(Resource):
    def get(self):
        all_farmers = ScoreHistory.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})
'''

class AllShipment(Resource):
    def get(self):
        all_farmers = Shipment.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllTransfer(Resource):
    def get(self):
        all_farmers = LoanTransfer.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllWarehouse(Resource):
    def get(self):
        all_farmers = Warehouse.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': 'success','data': all_farmers})

class AllLoans(Resource):
    def get(self):
        all_loans = db.session.query(Loan).all()
        all_loans = [loan.json() for loan in all_loans]
        return jsonify({"error":False,"message":"success","data":all_loans})

'''
class ListFarmers(Resource):
    def get(self):
        all_farmers = FarmerTable.query.all()        
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))
'''

class ListBuyersDailyPrice(Resource):
    def get(self):
        price = BuyersDailyPrice.query.all() 
        price = [prices.json() for prices in price]
        return jsonify(get_paginated_list(
        price, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListBuyersOffers(Resource):
    def get(self):
        price = BuyersOffers.query.all() 
        price = [prices.json() for prices in price]
        return jsonify(get_paginated_list(
        price, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListFarmGatePrices(Resource):
    def get(self):
        price = FarmGatePrices.query.all() 
        price = [prices.json() for prices in price]
        return jsonify(get_paginated_list(
        price, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))
class ListMarketPrices(Resource):
    def get(self):
        price = MarketPrices.query.all() 
        price = [prices.json() for prices in price]
        return jsonify(get_paginated_list(
        price, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))
        
class ListFarmers(Resource):
    def get(self):
        all_farmers = FarmerTable.query.all()        
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))
        


class ListAgronomy(Resource):
    def get(self):
        all_farmers = AgronomyServicesTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListCapacity(Resource):
    def get(self):
        all_farmers = CapacityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListCapital(Resource):
    def get(self):
        all_farmers = CapitalTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListCare(Resource):
    def get(self):
        all_farmers = CareTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListConditions(Resource):
    def get(self):
        all_farmers = ConditionsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListScoreAnalytics(Resource):
    def get(self):
        all_farmers = ScoreAnalytics.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListCreditAccess(Resource):
    def get(self):
        all_farmers = CreditAccessTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListCreditHistory(Resource):
    def get(self):
        all_farmers = CreditHistoryTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListCropInfo(Resource):
    def get(self):
        all_farmers = CropInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListCropQuality(Resource):
    def get(self):
        all_farmers = CropQuality.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListCultivation(Resource):
    def get(self):
        all_farmers = CultivationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListFarmland(Resource):
    def get(self):
        all_farmers = FarmlandTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListHarvest(Resource):
    def get(self):
        all_farmers = HarvestTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListInputsInfo(Resource):
    def get(self):
        all_farmers = InputsInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListLiving(Resource):
    def get(self):
        all_farmers = LivingTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListMechanization(Resource):
    def get(self):
        all_farmers = MechanizationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListMobileData(Resource):
    def get(self):
        all_farmers = MobileDataTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListPlanet(Resource):
    def get(self):
        all_farmers = Planet.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListPractice(Resource):
    def get(self):
        all_farmers = FarmPractice.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListProductivity(Resource):
    def get(self):
        all_farmers = ProductivityViabilityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListPsychometrics(Resource):
    def get(self):
        all_farmers = PsychometricsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListRecommendation(Resource):
    def get(self):
        all_farmers = Recommendation.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListSafety(Resource):
    def get(self):
        all_farmers = Safety.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))
class ListScorecard(Resource):
    def get(self):
        all_farmers = ScoreCard.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))
class ListCropcard(Resource):
    def get(self):
        all_cards = Cropcard.query.all()
        all_cards = [farmer.json() for farmer in all_cards]
        return jsonify(get_paginated_list(
        all_cards, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))
'''
class ListScoreHistory(Resource):
    def get(self):
        all_farmers = ScoreHistory.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))
'''

class ListShipment(Resource):
    def get(self):
        all_farmers = Shipment.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListTransfer(Resource):
    def get(self):
        all_farmers = LoanTransfer.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListWarehouse(Resource):
    def get(self):
        all_farmers = Warehouse.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

class ListLoans(Resource):
    def get(self):
        all_loans = db.session.query(Loan).all()
        all_loans = [loan.json() for loan in all_loans]
        return jsonify(get_paginated_list(
        all_loans, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))


# Bulk Files

class AddBulkFarmer(Resource):
    def post(self):
        csv_raw = request.files.get("kyf_file").read().decode("utf-8")
        csv = StringIO(csv_raw)
        df = pd.read_csv(csv)
        print(df.shape)
        if len(df)>0:
            for r in range(1,len(df)):
                dfr = df.iloc[r,:]
                farmer = FarmerTable.query.filter_by(bvn=dfr['bvn'])
                if not farmer:
                    farmerkyf = FarmerTable(firstname=dfr['firstname'],surname=dfr['surname'],
        middlename=dfr['middlename'],email=dfr['email'],telephone=dfr['telephone'],age=dfr['age'],
        gender=dfr['gender'],language = dfr['language'],maritalstatus=dfr['maritalstatus'],
        bankname = dfr['bankname'],accountno = dfr['accountno'],bvn=dfr['bvn'],
        meansofid=dfr['meansofid'],issuedate=dfr['issuedate'],expirydate=dfr['expirydate'],
        nin=dfr['nin'],permanentaddress=dfr['permanentaddress'],landmark=dfr['landmark'],
        stateoforigin=dfr['stateoforigin'],isinagroup = dfr['isinagroup'],
        reasonnogroup = dfr['reasonnogroup'],group=dfr['group'],
        numberofmembers = dfr['numberofmembers'],firstnamenok = dfr['firstnamenok'],
        surnamenok = dfr['surnamenok'],middlenamenok = dfr['middlenamenok'], 
        relationshipnok = dfr['relationshipnok'],occupationnok     = dfr['occupationnok'],
        telephonenok  = dfr['telephonenok'],permanentaddressnok  = dfr['permanentaddressnok'],
        landmarknok  = dfr['landmarknok'],ninnok  = dfr['ninnok'])
                    db.session.add(farmerkyf)
                    db.session.commit()
                return {"error":False,"message":'done'}

class AddBulkScorecard(Resource):
    def post(self):
        csv_raw = request.files.get("scorecard_file").read().decode("utf-8")
        csv = StringIO(csv_raw)
        df = pd.read_csv(csv)
        print(df.shape)
        if len(df)>0:
            for r in range(1,len(df)):
                dfr = df.iloc[r,:]
                farmer = ScoreCard.query.filter_by(bvn=dfr['bvn']).all()
                
                
                '''
                if not farmer:
                    card = ScoreCard(bvn=dfr['bvn'],age=dfr['age'],number_of_land=dfr['number_of_land'],address=dfr['address'],
        owner_caretaker=dfr['owner_caretaker'],crop=dfr['crop'],intercropping=dfr['intercropping'], machines=dfr['machines'],
        estimate_monthly_income=dfr['estimate_monthly_income'],years_cultivating=dfr['years_cultivating'],gender=dfr['gender'],
        owns_a_bank_account=dfr['owns_a_bank_account'],size_of_farm=dfr['size_of_farm'],number_of_crops=dfr['number_of_crops'],is_in_a_cooperative=dfr['is_in_a_cooperative'],
        no_of_agronomist_visits=dfr['no_of_agronomist_visits'])
                    db.session.add(card)
                    db.session.commit()
                '''
                if not farmer:
                    farmer = pd.DataFrame([['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits']],columns=['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits'])
                    for col in farmer.columns:
                        farmer[col] = dfr[col]
                    farmer['applyLoanAmount'] = applyLoan(farmer['bvn'])
                    farmer = farmer.rename({'number_of_land':'numberOfLand','estimate_monthly_income':'estimateMonthlyIncome',
                     'years_cultivating':'yearsCultivating'},axis=1)
                    cols=['age', 'numberOfLand', 'owner_caretaker', 'crop','applyLoanAmount',
                    'intercropping', 'machines', 'estimateMonthlyIncome','yearsCultivating']
                    tdf = preprocess_df(farmer[cols])
                    train_cols = ['number_of_land', 'owner_caretaker', 'intercropping', 'machines',
       'estimate_monthly_income', 'apply_loan_amount', 'years_cultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
                    score = model.predict_proba(tdf[train_cols])[:,1].round(2)
                    bin=bin_target(score)
                    history = ScoreCard(bvn=dfr['bvn'],age=dfr['age'],number_of_land=dfr['number_of_land'],address=dfr['address'],
        owner_caretaker=dfr['owner_caretaker'],crop=dfr['crop'],intercropping=dfr['intercropping'], machines=dfr['machines'],
        estimate_monthly_income=dfr['estimate_monthly_income'],years_cultivating=dfr['years_cultivating'],gender=dfr['gender'],
        owns_a_bank_account=dfr['owns_a_bank_account'],size_of_farm=dfr['size_of_farm'],number_of_crops=dfr['number_of_crops'],is_in_a_cooperative=dfr['is_in_a_cooperative'],
        no_of_agronomist_visits=dfr['no_of_agronomist_visits'],applyLoanAmount=farmer['applyLoanAmount'][0],
        score=score[0], bin=bin[0])
                    db.session.add(history)
                    db.session.commit()
        return jsonify({"error":False,"message":"done"})

farmer = api.namespace('api/farmer', description='farmer kyf')
farmer.add_resource(AddFarmer,'/add')
farmer.add_resource(Farmerbvn,'/bvn=<bvn>')
farmer.add_resource(Farmertag,'/tag=<tag>')
farmer.add_resource(Farmergroup,'/group=<group>')
farmer.add_resource(AllFarmers,'/all')
farmer.add_resource(ListFarmers, '/list')

care = api.namespace('api/care', description='care')
care.add_resource(AddCareTable,'/add')
care.add_resource(Carebvn,'/bvn=<bvn>')
care.add_resource(AllCare,'/all')
care.add_resource(ListCare, '/list')

living = api.namespace('api/living', description='Living')
living.add_resource(AddLivingTable,'/add')
living.add_resource(Livingbvn,'/bvn=<bvn>')
living.add_resource(AllLiving,'/all')
living.add_resource(ListLiving, '/list')

planet = api.namespace('api/planet', description='nature of crops and lands')
planet.add_resource(AddPlanet,'/add')
planet.add_resource(Planetbvn,'/bvn=<bvn>')
planet.add_resource(AllPlanet,'/all')
planet.add_resource(ListPlanet, '/list')

safety = api.namespace('api/safety', description='food safety and quality')
safety.add_resource(AddSafety,'/add')
safety.add_resource(Safetybvn,'/bvn=<bvn>')
safety.add_resource(AllSafety,'/all')
safety.add_resource(ListSafety, '/list')

capital = api.namespace('api/capital', description='farmer capital')
capital.add_resource(AddCapital,'/add')
capital.add_resource(Capitalbvn,'/bvn=<bvn>')
capital.add_resource(AllCapital,'/all')
capital.add_resource(ListCapital, '/list')

harvest = api.namespace('api/harvest', description='farmer harvest')
harvest.add_resource(AddHarvest,'/add')
harvest.add_resource(Harvestbvn,'/bvn=<bvn>')
harvest.add_resource(AllHarvest,'/all')
harvest.add_resource(ListHarvest, '/list')

agronomy = api.namespace('api/agronomy', description='farmer agronomy')
agronomy.add_resource(AddAgronomyServices,'/add')
agronomy.add_resource(Agronomybvn,'/bvn=<bvn>')
agronomy.add_resource(AllAgronomy,'/all')
agronomy.add_resource(ListAgronomy, '/list')

capacity = api.namespace('api/capacity', description='farmer capacity')
capacity.add_resource(AddCapacity,'/add')
capacity.add_resource(Capacitybvn,'/bvn=<bvn>')
capacity.add_resource(AllCapacity,'/all')
capacity.add_resource(ListCapacity, '/list')

farmland = api.namespace('api/farmland', description='farmland')
farmland.add_resource(AddFarmlandData,'/add')
farmland.add_resource(Farmlandbvn,'/bvn=<bvn>')
farmland.add_resource(AllFarmland,'/all')
farmland.add_resource(ListFarmland, '/list')

transfer = api.namespace('api/transfer', description='loan transfers')
transfer.add_resource(AddLoanTransfer,'/add')
transfer.add_resource(Transferbvn,'/bvn=<bvn>')
transfer.add_resource(Transferid,'/id=<id>')
transfer.add_resource(Transfercompany,'/company=<company>')
transfer.add_resource(Transfergroup,'/group=<group>')
transfer.add_resource(Transferstatus,'/status=<status>')
transfer.add_resource(AllTransfer,'/all')
transfer.add_resource(ListTransfer, '/list')
transfer.add_resource(AcceptTransfer,'/accept/id=<id>')
transfer.add_resource(UpdateTransfer,'/update/id=<id>')
transfer.add_resource(RejectTransfer,'/reject/id=<id>')

'''
accepttransfer = api.namespace('api/accept_transfer', description='accept loan transfers')
accepttransfer.add_resource(AcceptTransfer,'/id=<id>')
rejecttransfer = api.namespace('api/reject_transfer', description='rejectloan transfers')
updatetransfer.add_resource(UpdateTransfer,'/id=<id>')
updatetransfer = api.namespace('api/update_transfer', description='update loan transfers')
updatetransfer.add_resource(UpdateTransfer,'/id=<id>')
'''

practice = api.namespace('api/practice', description='farm practice')
practice.add_resource(AddFarmPractice,'/add')
practice.add_resource(Practicebvn,'/bvn=<bvn>')
practice.add_resource(AllPractice,'/all')
practice.add_resource(ListPractice, '/list')

scorecard = api.namespace('api/scorecard', description='scorecard')
scorecard.add_resource(AddScoreCard,'/add')
scorecard.add_resource(Scorecardbvn,'/bvn=<bvn>')
scorecard.add_resource(Scorecardid,'/id=<id>')
scorecard.add_resource(AllScorecard,'/all')
scorecard.add_resource(ListScorecard, '/list')

cropcard = api.namespace('api/cropcard', description='cropcard')
cropcard.add_resource(AddCropCard,'/add')
cropcard.add_resource(Cropcardid,'/id=<id>')
cropcard.add_resource(Cropcardbvn,'/bvn=<bvn>')
cropcard.add_resource(Cropcardcrop_name,'/crop_name=<crop_name>')
cropcard.add_resource(AllCropcard,'/all')
cropcard.add_resource(ListCropcard, '/list')

'''
scorehistory = api.namespace('api/scorehistory', description='scorehistory')
scorehistory.add_resource(ScoreHistorybvn,'/bvn=<bvn>')
scorehistory.add_resource(ScoreHistoryid,'/id=<id>')
scorehistory.add_resource(AllScoreHistory,'/all')
scorehistory.add_resource(ListScoreHistory, '/list')
'''
scoreanalytics = api.namespace('api/scoreanalytics', description='scoreanalytics')
scoreanalytics.add_resource(AddScoreAnalytics,'/add')
scoreanalytics.add_resource(ScoreAnalyticsbvn,'/bvn=<bvn>')
scoreanalytics.add_resource(AllScoreAnalytics,'/all')
scoreanalytics.add_resource(ListScoreAnalytics, '/list')

conditions = api.namespace('api/conditions', description='conditions')
conditions.add_resource(AddConditions,'/add')
conditions.add_resource(Conditionsbvn,'/bvn=<bvn>')
conditions.add_resource(AllConditions,'/all')
conditions.add_resource(ListConditions, '/list')

mobiledata = api.namespace('api/mobiledata', description='mobiledata')
mobiledata.add_resource(AddMobileData,'/add')
mobiledata.add_resource(MobileDatabvn,'/bvn=<bvn>')
mobiledata.add_resource(AllMobileData,'/all')
mobiledata.add_resource(ListMobileData, '/list')

cultivation = api.namespace('api/cultivation', description='cultivation')
cultivation.add_resource(AddCultivation,'/add')
cultivation.add_resource(Cultivationbvn,'/bvn=<bvn>')
cultivation.add_resource(AllCultivation,'/all')
cultivation.add_resource(ListCultivation, '/list')

creditaccess = api.namespace('api/creditaccess', description='credit access')
creditaccess.add_resource(AddCreditAccess,'/add')
creditaccess.add_resource(CreditAccessbvn,'/bvn=<bvn>')
creditaccess.add_resource(AllCreditAccess,'/all')
creditaccess.add_resource(ListCreditAccess, '/list')

productivity = api.namespace('api/productivity', description='productivity viability')
productivity.add_resource(AddProductivityViability,'/add')
productivity.add_resource(Productivitybvn,'/bvn=<bvn>')
productivity.add_resource(AllProductivity,'/all')
productivity.add_resource(ListProductivity, '/list')

credithistory = api.namespace('api/credithistory', description='credit history')
credithistory.add_resource(AddCreditHistory,'/add')
credithistory.add_resource(CreditHistorybvn,'/bvn=<bvn>')
credithistory.add_resource(AllCreditHistory,'/all')
credithistory.add_resource(ListCreditHistory, '/list')

mechanization = api.namespace('api/mechanization', description='mechanization')
mechanization.add_resource(AddMechanization,'/add')
mechanization.add_resource(Mechanizationbvn,'/bvn=<bvn>')
mechanization.add_resource(AllMechanization,'/all')
mechanization.add_resource(ListMechanization, '/list')

psychometrics = api.namespace('api/psychometrics', description='psychometrics')
psychometrics.add_resource(AddPsychometrics,'/add')
psychometrics.add_resource(Psychometricsbvn,'/bvn=<bvn>')
psychometrics.add_resource(AllPsychometrics,'/all')
psychometrics.add_resource(ListPsychometrics, '/list')

crop_info = api.namespace('api/crop_info', description='crop information traceability')
crop_info.add_resource(AddCropInfo,'/add')
crop_info.add_resource(CropInfoTracing,'/tracing_id=<tracing_id>')
crop_info.add_resource(AllCropInfo,'/all')
crop_info.add_resource(ListCropInfo, '/list')

crop_quality = api.namespace('api/crop_quality', description='crop quality traceability')
crop_quality.add_resource(AddCropQuality,'/add')
crop_quality.add_resource(CropQualityTracing,'/tracing_id=<tracing_id>')
crop_quality.add_resource(AllCropQuality,'/all')
crop_quality.add_resource(ListCropQuality, '/list')

shipment = api.namespace('api/shipment', description='shipment traceability')
shipment.add_resource(AddShipment,'/add')
shipment.add_resource(ShipmentTracing,'/tracing_id=<tracing_id>')
shipment.add_resource(AllShipment,'/all')
shipment.add_resource(ListShipment, '/list')

inputs_info = api.namespace('api/inputs_info', description='inputs_info traceability')
inputs_info.add_resource(AddInputsInfo,'/add')
inputs_info.add_resource(InputsInfoTracing,'/tracing_id=<tracing_id>')
inputs_info.add_resource(AllInputsInfo,'/all')
inputs_info.add_resource(ListInputsInfo, '/list')

warehouse = api.namespace('api/warehouse', description='warehouse traceability')
warehouse.add_resource(AddWarehouse,'/add')
warehouse.add_resource(WarehouseTracing,'/tracing_id=<tracing_id>')
warehouse.add_resource(AllWarehouse,'/all')
warehouse.add_resource(ListWarehouse, '/list')

recommendation = api.namespace('api/recommendation', description='recommendation traceability')
recommendation.add_resource(AddRecommendation,'/add')
recommendation.add_resource(RecommendationTracing,'/tracing_id=<tracing_id>')
recommendation.add_resource(AllRecommendation,'/all')
recommendation.add_resource(ListRecommendation, '/list')

loans = api.namespace('api/loan',description='load loans')
loans.add_resource(AddLoan,'/add')
loans.add_resource(Loantype,'/type=<type>')
loans.add_resource(Loancompany,'/company=<company>')
loans.add_resource(AllLoans,'/all')
loans.add_resource(ListLoans, '/list')

buyers_offers = api.namespace('api/buyers_offers',description='load buyers_offers')
buyers_offers.add_resource(AddBuyersOffers,'/add')
buyers_offers.add_resource(BuyersOffersid,'/id=<id>')
buyers_offers.add_resource(BuyersOfferscrop,'/crop=<crop>')
buyers_offers.add_resource(AllBuyersOffers,'/all')
buyers_offers.add_resource(ListBuyersOffers, '/list')

buyers_daily_price = api.namespace('api/daily_price',description='load buyers_daily_price')
buyers_daily_price.add_resource(AddBuyersDailyPrice,'/add')
buyers_daily_price.add_resource(BuyersDailyPriceid,'/id=<id>')
buyers_daily_price.add_resource(BuyersDailyPricecrop,'/crop=<crop>')
buyers_daily_price.add_resource(AllBuyersDailyPrice,'/all')
buyers_daily_price.add_resource(ListBuyersDailyPrice, '/list')

farmgate_prices = api.namespace('api/farmgate_prices',description='load farmgate_prices')
farmgate_prices.add_resource(AddFarmGatePrices,'/add')
farmgate_prices.add_resource(FarmGatePricesid,'/id=<id>')
farmgate_prices.add_resource(FarmGatePricescrop,'/crop=<crop>')
farmgate_prices.add_resource(AllFarmGatePrices,'/all')
farmgate_prices.add_resource(ListFarmGatePrices, '/list')

market_prices = api.namespace('api/market_prices',description='load market_prices')
market_prices.add_resource(AddMarketPrices,'/add')
market_prices.add_resource(MarketPricesid,'/id=<id>')
market_prices.add_resource(MarketPricescrop,'/crop=<crop>')
market_prices.add_resource(AllMarketPrices,'/all')
market_prices.add_resource(ListMarketPrices, '/list')

bulk = api.namespace('api/bulk', description='bulk files')
bulk.add_resource(AddBulkFarmer,'/farmer')
bulk.add_resource(AddBulkScorecard,'/scorecard')

capital5c = api.namespace('api/5c_capital', description='farmer 5c_capital')
capital5c.add_resource(AddCapital5c,'/add')
capital5c.add_resource(Capital5cbvn,'/bvn=<bvn>')
capital5c.add_resource(AllCapital5c,'/all')

character5c = api.namespace('api/5c_character', description='farmer 5c_character')
character5c.add_resource(AddCharacter5c,'/add')
character5c.add_resource(Character5cbvn,'/bvn=<bvn>')
character5c.add_resource(AllCharacter5c,'/all')

collateral5c = api.namespace('api/5c_collateral', description='farmer 5c_collateral')
collateral5c.add_resource(AddCollateral5c,'/add')
collateral5c.add_resource(Collateral5cbvn,'/bvn=<bvn>')
collateral5c.add_resource(AllCollateral5c,'/all')

capacity5c = api.namespace('api/5c_capacity', description='farmer 5c_capacity')
capacity5c.add_resource(AddCapacity5c,'/add')
capacity5c.add_resource(Capacity5cbvn,'/bvn=<bvn>')
capacity5c.add_resource(AllCapacity5c,'/all')

conditions5c = api.namespace('api/5c_conditions', description='farmer 5c_conditions')
conditions5c.add_resource(AddConditions5c,'/add')
conditions5c.add_resource(Conditions5cbvn,'/bvn=<bvn>')
conditions5c.add_resource(AllConditions5c,'/all')

'''
scorefarmer = api.namespace('api/score', description='credit scoring (deprecated)')
scorefarmer.add_resource(ScoreFarmer,'/')
scorefarmer.add_resource(ScoreFarmerDragAndDrop,'/filter')
'''
# Running app
if __name__ == '__main__':
    
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
