# Import flask 
from flask import Flask, jsonify, request, current_app
from flask_cors import CORS,cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api, fields
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
from flask_migrate import Migrate
import numpy as np
import pandas as pd
import pickle
from modelExample import preprocess_df, bin_target
model = pickle.load(open('modelExample.pkl','rb'))
api = Api(app, title='Zowasel')
Migrate(app,db)
app.config['CORS_HEADERS'] = 'Content-Type'


# Post Requests

# return {"error":True,"message":"Sorry your request can not be processed at the moment","data":""}


# Kyf

class AddFarmer(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = FarmerTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            message = {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
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
            message = {'message':'success'}
        return message

# -------------5cs of Credit Scoring-------------------------------------------------------------------------------------

# 1.Capital

class AddCapital(Resource):	
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmercapital = CapitalTable(bvn=request.json['bvn'],MainIncomeSource=request.json['MainIncomeSource'],
        OtherIncomeSource=request.json['OtherIncomeSource'],NoOfIncomeEarners=request.json['NoOfIncomeEarners'],
        HasBankAccount=request.json['HasBankAccount'],FirstFundingOption=request.json['FirstFundingOption'],
        NeedsALoan=request.json['NeedsALoan'],PayBackMonths=request.json['PayBackMonths'],
        HarvestQtyChanged=request.json['HarvestQtyChanged'],PestExpenseChanged=request.json['PestExpenseChanged'])
            db.session.add(farmercapital)
            db.session.commit()
            return {'message':'success'}
        
class AddCreditAccess(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CreditAccessTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmercreditaccess = CreditAccessTable(bvn=request.json['bvn'],
        HasServedAsTreasurer=request.json['HasServedAsTreasurer'],DurationAsTreasurer=request.json['DurationAsTreasurer'],
        SavesMoneyMonthly=request.json['SavesMoneyMonthly'],SavingsAmount=request.json['SavingsAmount'],
        HadDifficultyRepaying=request.json['HadDifficultyRepaying'],DifficultLoanAmount=request.json['DifficultLoanAmount'],
        DifficultyReason=request.json['DifficultyReason'],NoOfDifficultLoans=request.json['NoOfDifficultLoans'],
        NoOfRepaidLoans=request.json['NoOfRepaidLoans'],NoOfLoansOnTime=request.json['NoOfLoansOnTime'],
        EstMonthlyIncome=request.json['EstMonthlyIncome'],CostOfCultivation=request.json['CostOfCultivation'],
        FarmProduceExchanged=request.json['FarmProduceExchanged'],NoOfTimesExchanged=request.json['NoOfTimesExchanged'],
        Collateral=request.json['Collateral'],ApplyLoanAmount=request.json['ApplyLoanAmount'],
        YearsOfCultivating=request.json['Collateral'],AnnualTurnover=request.json['AnnualTurnover'])
            db.session.add(farmercreditaccess)
            db.session.commit()
            return {'message':'success'}


class AddCapital5c(Resource):	
    def post(self):
        farmercapital = CapitalTable(bvn=request.json['bvn'],MainIncomeSource=request.json['MainIncomeSource'],
        OtherIncomeSource=request.json['OtherIncomeSource'],NoOfIncomeEarners=request.json['NoOfIncomeEarners'],
        HasBankAccount=request.json['HasBankAccount'],FirstFundingOption=request.json['FirstFundingOption'],
        NeedsALoan=request.json['NeedsALoan'],PayBackMonths=request.json['PayBackMonths'],
        HarvestQtyChanged=request.json['HarvestQtyChanged'],PestExpenseChanged=request.json['PestExpenseChanged'])
        farmercreditaccess = CreditAccessTable(bvn=request.json['bvn'],
        HasServedAsTreasurer=request.json['HasServedAsTreasurer'],DurationAsTreasurer=request.json['DurationAsTreasurer'],
        SavesMoneyMonthly=request.json['SavesMoneyMonthly'],SavingsAmount=request.json['SavingsAmount'],
        HadDifficultyRepaying=request.json['HadDifficultyRepaying'],DifficultLoanAmount=request.json['DifficultLoanAmount'],
        DifficultyReason=request.json['DifficultyReason'],NoOfDifficultLoans=request.json['NoOfDifficultLoans'],
        NoOfRepaidLoans=request.json['NoOfRepaidLoans'],NoOfLoansOnTime=request.json['NoOfLoansOnTime'],
        EstMonthlyIncome=request.json['EstMonthlyIncome'],CostOfCultivation=request.json['CostOfCultivation'],
        FarmProduceExchanged=request.json['FarmProduceExchanged'],NoOfTimesExchanged=request.json['NoOfTimesExchanged'],
        Collateral=request.json['Collateral'],ApplyLoanAmount=request.json['ApplyLoanAmount'],
        YearsOfCultivating=request.json['Collateral'],AnnualTurnover=request.json['AnnualTurnover'])
        # Add data only if Id does not exist in database already
        farmer = CapitalTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in Capital!"})     
        else:
            db.session.add(farmercapital)
            db.session.commit()
        # Add data only if Id does not exist in database already
        farmer = CreditAccessTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in Credit Access!"})
        else:
            db.session.add(farmercreditaccess)
            db.session.commit()
        return {'message':'success'}


# 2.Character

class AddCreditHistory(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CreditHistoryTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmercredithistory = CreditHistoryTable(bvn=request.json['bvn'],
        HasTakenLoanBefore=request.json['HasTakenLoanBefore'],SourceOfLoan=request.json['SourceOfLoan'],
        PastLoanAmount=request.json['PastLoanAmount'],HowLoanWasRepaid=request.json['HowLoanWasRepaid'],
        IsReadyToPayInterest=request.json['IsReadyToPayInterest'],CanProvideCollateral=request.json['CanProvideCollateral'],
        WhyNoCollateral=request.json['WhyNoCollateral'])
            db.session.add(farmercredithistory)
            db.session.commit()
            return farmercredithistory.json()

class AddProductivityViability(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = ProductivityViabilityTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmerproductivity = ProductivityViabilityTable(bvn=request.json['bvn'],
        CropsCultivated=request.json['CropsCultivated'],GrowsCrops=request.json['GrowsCrops'],
        OilPalmFertilizers=request.json['OilPalmFertilizers'],CocoaFertilizers=request.json['CocoaFertilizers'],
        FertilizerFrequency=request.json['FertilizerFrequency'],PestFungHerbicides=request.json['PestFungHerbicides'],
        StageChemicalApplied=request.json['StageChemicalApplied'],NoOfOilDrums=request.json['NoOfOilDrums'],
        NoOfBagsSesame=request.json['NoOfBagsSesame'],NoOfBagsSoyaBeans=request.json['NoOfBagsSoyaBeans'],
        NoOfBagsMaize=request.json['NoOfBagsMaize'],NoOfBagsSorghum=request.json['NoOfBagsSorghum'],
        NoOfBagsCocoaBeans=request.json['NoOfBagsCocoaBeans'],CropTrainedOn=request.json['CropTrainedOn'],
        WhereWhenWhoTrained=request.json['WhereWhenWhoTrained'],NoOfTraining=request.json['NoOfTraining'],
        PruningFrequency=request.json['PruningFrequency'],CropBasedProblems=request.json['CropBasedProblems'],
        TooYoungCrops=request.json['TooYoungCrops'],YoungCropsAndStage=request.json['YoungCropsAndStage'],
        CultivationStartdate=request.json['CultivationStartdate'],IsIntensiveFarmingPractised=request.json['IsIntensiveFarmingPractised'],
        EconomicActivities=request.json['EconomicActivities'])
            db.session.add(farmerproductivity)
            db.session.commit()
            return farmerproductivity.json()

class AddAgronomyServices(Resource):	
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = AgronomyServicesTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmeragronomy = AgronomyServicesTable(bvn=request.json['bvn'],
        KnowsAgriProcessed=request.json['KnowsAgriProcessed'],AgronomistThatTrainedYou=request.json['AgronomistThatTrainedYou'],
        CanManageEcosystem=request.json['CanManageEcosystem'],HowToManageEcosystem=request.json['HowToManageEcosystem'],
        IsTrainingBeneficial=request.json['IsTrainingBeneficial'],FieldRoutines=request.json['FieldRoutines'],
        HarvestingChanges=request.json['HarvestingChanges'],IsCropCalendarBeneficial=request.json['IsCropCalendarBeneficial'],
        CropCalendarBenefits=request.json['CropCalendarBenefits'],RecordKeepingBenefits=request.json['RecordKeepingBenefits'])
            db.session.add(farmeragronomy)
            db.session.commit()
            return farmeragronomy.json()
class AddPsychometrics(Resource):	
    def post(self):
        farmer = PsychometricsTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmerpsychometrics = PsychometricsTable(bvn=request.json['bvn'],FluidIntelligence=request.json['FluidIntelligence'],
        AttitudesandBeliefs=request.json['AttitudesandBeliefs'],AgribusinessSkills=request.json['AgribusinessSkills'],
        EthicsandHonesty=request.json['EthicsandHonesty'],SavesEnough=request.json['SavesEnough'],
        HasLazyNeighbors=request.json['HasLazyNeighbors'])
            db.session.add(farmerpsychometrics)
            db.session.commit()
            return farmerpsychometrics.json()

class AddMobileData(Resource):	
    def post(self):
        farmer = MobileDataTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmermobiledata = MobileDataTable(bvn=request.json['bvn'],MobilePhoneType=request.json['MobilePhoneType'],
        Avweeklyphoneuse=request.json['Avweeklyphoneuse'],Callsoutnumber=request.json['Callsoutnumber'],
        Callsoutminutes=request.json['Callsoutminutes'],Callsinnumber=request.json['Callsinnumber'],
        Callinminutes=request.json['Callinminutes'],SMSsent=request.json['SMSsent'],
        Dataprecedingplanswitch=request.json['Dataprecedingplanswitch'],Billpaymenthistory=request.json['Billpaymenthistory'],
        Avweeklydatarefill=request.json['Avweeklydatarefill'],NoOfmobileapps=request.json['NoOfmobileapps'],
        AvTimeSpentOnApp=request.json['AvTimeSpentOnApp'],MobileAppKinds=request.json['MobileAppKinds'],
        AppDeleteRate=request.json['AppDeleteRate'])
            db.session.add(farmermobiledata)
            db.session.commit()
            return farmermobiledata.json()


class AddCharacter5c(Resource):
    def post(self):
        farmercredithistory = CreditHistoryTable(bvn=request.json['bvn'],
        HasTakenLoanBefore=request.json['HasTakenLoanBefore'],SourceOfLoan=request.json['SourceOfLoan'],
        PastLoanAmount=request.json['PastLoanAmount'],HowLoanWasRepaid=request.json['HowLoanWasRepaid'],
        IsReadyToPayInterest=request.json['IsReadyToPayInterest'],CanProvideCollateral=request.json['CanProvideCollateral'],
        WhyNoCollateral=request.json['WhyNoCollateral'])
        farmerproductivity = ProductivityViabilityTable(bvn=request.json['bvn'],
        CropsCultivated=request.json['CropsCultivated'],GrowsCrops=request.json['GrowsCrops'],
        OilPalmFertilizers=request.json['OilPalmFertilizers'],CocoaFertilizers=request.json['CocoaFertilizers'],
        FertilizerFrequency=request.json['FertilizerFrequency'],PestFungHerbicides=request.json['PestFungHerbicides'],
        StageChemicalApplied=request.json['StageChemicalApplied'],NoOfOilDrums=request.json['NoOfOilDrums'],
        NoOfBagsSesame=request.json['NoOfBagsSesame'],NoOfBagsSoyaBeans=request.json['NoOfBagsSoyaBeans'],
        NoOfBagsMaize=request.json['NoOfBagsMaize'],NoOfBagsSorghum=request.json['NoOfBagsSorghum'],
        NoOfBagsCocoaBeans=request.json['NoOfBagsCocoaBeans'],CropTrainedOn=request.json['CropTrainedOn'],
        WhereWhenWhoTrained=request.json['WhereWhenWhoTrained'],NoOfTraining=request.json['NoOfTraining'],
        PruningFrequency=request.json['PruningFrequency'],CropBasedProblems=request.json['CropBasedProblems'],
        TooYoungCrops=request.json['TooYoungCrops'],YoungCropsAndStage=request.json['YoungCropsAndStage'],
        CultivationStartdate=request.json['CultivationStartdate'],IsIntensiveFarmingPractised=request.json['IsIntensiveFarmingPractised'],
        EconomicActivities=request.json['EconomicActivities'])
        farmeragronomy = AgronomyServicesTable(bvn=request.json['bvn'],
        KnowsAgriProcessed=request.json['KnowsAgriProcessed'],AgronomistThatTrainedYou=request.json['AgronomistThatTrainedYou'],
        CanManageEcosystem=request.json['CanManageEcosystem'],HowToManageEcosystem=request.json['HowToManageEcosystem'],
        IsTrainingBeneficial=request.json['IsTrainingBeneficial'],FieldRoutines=request.json['FieldRoutines'],
        HarvestingChanges=request.json['HarvestingChanges'],IsCropCalendarBeneficial=request.json['IsCropCalendarBeneficial'],
        CropCalendarBenefits=request.json['CropCalendarBenefits'],RecordKeepingBenefits=request.json['RecordKeepingBenefits'])
        farmerpsychometrics = PsychometricsTable(bvn=request.json['bvn'],FluidIntelligence=request.json['FluidIntelligence'],
        AttitudesandBeliefs=request.json['AttitudesandBeliefs'],AgribusinessSkills=request.json['AgribusinessSkills'],
        EthicsandHonesty=request.json['EthicsandHonesty'],SavesEnough=request.json['SavesEnough'],
        HasLazyNeighbors=request.json['HasLazyNeighbors'])
        farmermobiledata = MobileDataTable(bvn=request.json['bvn'],MobilePhoneType=request.json['MobilePhoneType'],
        Avweeklyphoneuse=request.json['Avweeklyphoneuse'],Callsoutnumber=request.json['Callsoutnumber'],
        Callsoutminutes=request.json['Callsoutminutes'],Callsinnumber=request.json['Callsinnumber'],
        Callinminutes=request.json['Callinminutes'],SMSsent=request.json['SMSsent'],
        Dataprecedingplanswitch=request.json['Dataprecedingplanswitch'],Billpaymenthistory=request.json['Billpaymenthistory'],
        Avweeklydatarefill=request.json['Avweeklydatarefill'],NoOfmobileapps=request.json['NoOfmobileapps'],
        AvTimeSpentOnApp=request.json['AvTimeSpentOnApp'],MobileAppKinds=request.json['MobileAppKinds'],
        AppDeleteRate=request.json['AppDeleteRate'])
        # Add data only if Id does not exist in database already
        farmer = CreditHistoryTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in CreditHistoryTable!"})
        else:
            db.session.add(farmercredithistory)
        farmer = ProductivityViabilityTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in ProductivityViabilityTable!"})
        else:
            db.session.add(farmerproductivity)
        farmer = AgronomyServicesTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in AgronomyServicesTable!"})
        else:
            db.session.add(farmeragronomy)
        farmer = PsychometricsTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in PsychometricsTable!"})
        else:
            db.session.add(farmerpsychometrics)
        farmer = MobileDataTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists in MobileDataTable!"})
        else:
            db.session.add(farmermobiledata)
        db.session.commit()
        return {'message':'success'}


# 3.Collateral

class AddFarmlandData(Resource):	
    def post(self):
        farmer = FarmlandTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmerland = FarmlandTable(bvn=request.json['bvn'],NoOfFarmlands=request.json['NoOfFarmlands'],
        OwnerOrCaretaker=request.json['OwnerOrCaretaker'],FarmOwnerName=request.json['FarmOwnerName'],
        FarmOwnerPhoneNo=request.json['FarmOwnerPhoneNo'],RelationshipWithOwner=request.json['RelationshipWithOwner'],
        InheritedFrom=request.json['InheritedFrom'],SizeOfFarm=request.json['SizeOfFarm'],
        FarmCoordinates=request.json['FarmCoordinates'],FarmAddress=request.json['FarmAddress'],
        KeepsAnimals=request.json['KeepsAnimals'],AnimalsFeedOn=request.json['AnimalsFeedOn'])
            db.session.add(farmerland)
            db.session.commit()
            return farmerland.json()

class AddCollateral5c(Resource):	
    def post(self):
        farmerland = FarmlandTable(bvn=request.json['bvn'],NoOfFarmlands=request.json['NoOfFarmlands'],
        OwnerOrCaretaker=request.json['OwnerOrCaretaker'],FarmOwnerName=request.json['FarmOwnerName'],
        FarmOwnerPhoneNo=request.json['FarmOwnerPhoneNo'],RelationshipWithOwner=request.json['RelationshipWithOwner'],
        InheritedFrom=request.json['InheritedFrom'],SizeOfFarm=request.json['SizeOfFarm'],
        FarmCoordinates=request.json['FarmCoordinates'],FarmAddress=request.json['FarmAddress'],
        KeepsAnimals=request.json['KeepsAnimals'],AnimalsFeedOn=request.json['AnimalsFeedOn'])

        farmer = FarmlandTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerland)
        db.session.commit()
        return {'message':'success'}

#  4.Capacity

class AddCapacity(Resource):	
    def post(self):
        farmer = CapacityTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmercapacity = CapacityTable(bvn=request.json['bvn'],
        HowLongBeenFarming=request.json['HowLongBeenFarming'],ParticipatedInTraining=request.json['ParticipatedInTraining'],
        FarmingPractice=request.json['FarmingPractice'],KeepsAnimals=request.json['KeepsAnimals'],
        HasCooperative=request.json['HasCooperative'],CooperativeName=request.json['CooperativeName'],
        EducationLevel=request.json['EducationLevel'])
            db.session.add(farmercapacity)
            db.session.commit()
            return farmercapacity.json()

class AddFarmPractice(Resource):	
    def post(self):
        farmer = FarmPractice.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmerpractice = FarmPractice(bvn=request.json['bvn'],SizeOfFarm=request.json['SizeOfFarm'],
        FarmIsRentedorLeased=request.json['FarmIsRentedorLeased'],NoOfYearsLeased=request.json['NoOfYearsLeased'],
        UsesMachines=request.json['UsesMachines'],RotatesCrops=request.json['RotatesCrops'],
        NoOfHectaresProducedYearly=request.json['NoOfHectaresProducedYearly'],ApproxFertilizerUse=request.json['ApproxFertilizerUse'],
        NoOfFertlizerApplications=request.json['NoOfFertlizerApplications'],DecisionForSpraying=request.json['DecisionForSpraying'],
        WeedControlPractice=request.json['WeedControlPractice'],EstimatedIncomePerCrop=request.json['EstimatedIncomePerCrop'],
        CropthatcanSellWell=request.json['CropthatcanSellWell'],HasFarmPlanOrProject=request.json['HasFarmPlanOrProject'],
        FarmProjectInfo=request.json['FarmProjectInfo'])
            db.session.add(farmerpractice)
            db.session.commit()
            return farmerpractice.json()

class AddMechanization(Resource):	
    def post(self):
        farmer = MechanizationTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmermechanization = MechanizationTable(bvn=request.json['bvn'],
        MachinesUsed=request.json['MachinesUsed'],MachineHasHelped=request.json['MachineHasHelped'],
        AdviseMachineOrLabour=request.json['AdviseMachineOrLabour'],OtherMachinesNeeded=request.json['OtherMachinesNeeded'],
        CanAcquireMoreLands=request.json['CanAcquireMoreLands'],PercentCostSaved=request.json['PercentCostSaved'])
            db.session.add(farmermechanization)
            db.session.commit()
            return farmermechanization.json()

class AddCultivation(Resource):	
    def post(self):
        farmer = CultivationTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmercultivation = CultivationTable(bvn=request.json['bvn'],type_of_labor=request.json['type_of_labor'],
        pay_for_labor=request.json['pay_for_labor'],how_many_housechildren_help=request.json['how_many_housechildren_help'],
        season_children_help=request.json['season_children_help'],labor_children_do=request.json['labor_children_do'],
        household_vs_hire_cost=request.json['household_vs_hire_cost'],labor_women_do=request.json['labor_women_do'],
        percent_female_hired=request.json['percent_female_hired'])
            db.session.add(farmercultivation)
            db.session.commit()
            return farmercultivation.json()

class AddHarvest(Resource):	
    def post(self):
        farmer = HarvestTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with bvn already exists!"}
        else:
            farmerharvest = HarvestTable(bvn=request.json['bvn'],when_is_harvest_season=request.json['when_is_harvest_season'],
        no_of_hired_workers=request.json['no_of_hired_workers'],no_of_family_workers=request.json['no_of_family_workers'],
        no_of_permanent_workers=request.json['no_of_permanent_workers'],no_hired_constantly=request.json['no_hired_constantly'])
            db.session.add(farmerharvest)
            db.session.commit()
            return farmerharvest.json()

class AddCapacity5c(Resource):	
    def post(self):
        farmercapacity = CapacityTable(bvn=request.json['bvn'],
        HowLongBeenFarming=request.json['HowLongBeenFarming'],ParticipatedInTraining=request.json['ParticipatedInTraining'],
        FarmingPractice=request.json['FarmingPractice'],KeepsAnimals=request.json['KeepsAnimals'],
        HasCooperative=request.json['HasCooperative'],CooperativeName=request.json['CooperativeName'],
        EducationLevel=request.json['EducationLevel'])
        farmerpractice = FarmPractice(bvn=request.json['bvn'],SizeOfFarm=request.json['SizeOfFarm'],
        FarmIsRentedorLeased=request.json['FarmIsRentedorLeased'],NoOfYearsLeased=request.json['NoOfYearsLeased'],
        UsesMachines=request.json['UsesMachines'],RotatesCrops=request.json['RotatesCrops'],
        NoOfHectaresProducedYearly=request.json['NoOfHectaresProducedYearly'],ApproxFertilizerUse=request.json['ApproxFertilizerUse'],
        NoOfFertlizerApplications=request.json['NoOfFertlizerApplications'],DecisionForSpraying=request.json['DecisionForSpraying'],
        WeedControlPractice=request.json['WeedControlPractice'],EstimatedIncomePerCrop=request.json['EstimatedIncomePerCrop'],
        CropthatcanSellWell=request.json['CropthatcanSellWell'],HasFarmPlanOrProject=request.json['HasFarmPlanOrProject'],
        FarmProjectInfo=request.json['FarmProjectInfo'])
        farmermechanization = MechanizationTable(bvn=request.json['bvn'],
        MachinesUsed=request.json['MachinesUsed'],MachineHasHelped=request.json['MachineHasHelped'],
        AdviseMachineOrLabour=request.json['AdviseMachineOrLabour'],OtherMachinesNeeded=request.json['OtherMachinesNeeded'],
        CanAcquireMoreLands=request.json['CanAcquireMoreLands'],PercentCostSaved=request.json['PercentCostSaved'])
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
            return {'message':'success'}



# 5.Condition
class AddConditions(Resource):	
    @cross_origin(origin='*',headers=['content-type'])
    def post(self):
        farmercondition = ConditionsTable(bvn=request.json['bvn'],duration=request.json['duration'],
        seller=request.json['seller'],seller_mou=request.json['seller_mou'])
        
        farmer = ConditionsTable.query.filter_by(bvn=request.json['bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercondition)
            db.session.commit()
        return farmercondition.json()

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
        return farmercondition.json()


class AddScoreAnalytics(Resource):	
    def post(self):
        new_data = ScoreAnalytics(bvn=request.json['bvn'],Scores=request.json['Scores'],
        Conditions=request.json['Conditions'],Capital=request.json['Capital'],Collateral=request.json['Collateral'],
        Capacity=request.json['Capacity'],Character=request.json['Character'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()



# Sustainability

class AddCareTable(Resource):	
    def post(self):
        new_data = CareTable(bvn=request.json['bvn'],HealthCentLoc=request.json['HealthCentLoc'],
        HealthCentCount=request.json['HealthCentCount'],HealthCentDistance=request.json['HealthCentDistance'],
        HealthCentFunctional=request.json['HealthCentFunctional'],Affordable=request.json['Affordable'],
        FarmDistance=request.json['FarmDistance'],InjuryEvent=request.json['InjuryEvent'],FirstAid=request.json['FirstAid'],
        LastCheck=request.json['LastCheck'],InSchool=request.json['InSchool'],Level=request.json['Level'],
        SchoolCount=request.json['SchoolCount'],SchoolFunctional=request.json['SchoolFunctional'],
        Qualification=request.json['Qualification'],StudyTime=request.json['StudyTime'],
        StudyWhere=request.json['StudyWhere'],AltIncomeSource=request.json['AltIncomeSource'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


class AddPlanet(Resource):	
    def post(self):
        new_data = Planet(bvn=request.json['bvn'],PlanToExpand=request.json['PlanToExpand'],Crop=request.json['Crop'],
        Variety=request.json['Variety'],RaiseOrBuy=request.json['RaiseOrBuy'],BuyWhere=request.json['BuyWhere'],
        SeedlingPrice=request.json['SeedlingPrice'],QtyBought=request.json['QtyBought'],DegradedLand=request.json['DegradedLand'],
        CropRotation=request.json['CropRotation'],Season=request.json['Season'],Disaster=request.json['Disaster'],
        Burning=request.json['Burning'],Mill=request.json['Mill'],EnergySource=request.json['EnergySource'],ReplacedTree=request.json['ReplacedTree'],
        Placement=request.json['Placement'],SourceOfWater=request.json['SourceOfWater'],CoverCrops=request.json['CoverCrops'],
        Intercrop=request.json['Intercrop'],CropIntercropped=request.json['CropIntercropped'],WasteMgt=request.json['WasteMgt'],
        WasteDisposal=request.json['WasteDisposal'],RecycleWaste=request.json['RecycleWaste'],Suffered=request.json['Suffered'],
        WhenSuffered=request.json['WhenSuffered'],GreyWater=request.json['GreyWater'],RecycleGreyWater=request.json['RecycleGreyWater'],
        Pollution=request.json['Pollution'],PollutionFreq=request.json['PollutionFreq'],Measures=request.json['Measures'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


class AddSafety(Resource):	
    def post(self):
        new_data = Safety(bvn=request.json['bvn'],Ferment=request.json['Ferment'],
        FermentDays=request.json['FermentDays'],FermentReason=request.json['FermentReason'],BrokenQty=request.json['BrokenQty'],
        DoWithBroken=request.json['DoWithBroken'],UnripeQty=request.json['UnripeQty'],DoWithUnripe=request.json['DoWithUnripe'],
        CocoaStore=request.json['CocoaStore'],FFBStore=request.json['FFBStore'],Herbicide=request.json['Herbicide'],
        HerbicideStore=request.json['HerbicideStore'],AgroChemSource=request.json['AgroChemSource'],HarvestTool=request.json['HarvestTool'],
        Wear=request.json['Wear'],Disposal=request.json['Disposal'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddLivingTable(Resource):	
    def post(self):
        new_data = LivingTable(bvn=request.json['bvn'],HouseOwned=request.json['HouseOwned'],
        StaysWithFamily=request.json['StaysWithFamily'],RelationshipWithOwner=request.json['RelationshipWithOwner'],
        HouseHoldEats=request.json['HouseHoldEats'],MaleUnderAge=request.json['MaleUnderAge'],
        FemaleUnderAge=request.json['FemaleUnderAge'],ChildrenUnderAge=request.json['ChildrenUnderAge'],
        MaleAboveAge=request.json['MaleAboveAge'],FemaleAboveAge=request.json['FemaleAboveAge'],
        ChildrenAboveAge=request.json['ChildrenAboveAge'],LivesWith=request.json['LivesWith'],OwnOtherLands=request.json['OwnOtherLands'],
        StandardofLiving=request.json['StandardofLiving'],SourceOfWater=request.json['SourceOfWater'],
        SourceEverytime=request.json['SourceEverytime'],CookingMethod=request.json['CookingMethod'],
        HaveElectricity=request.json['HaveElectricity'],PowerPayment=request.json['PowerPayment'],Typeoftoilet=request.json['Typeoftoilet'],
        KitchenSink=request.json['KitchenSink'],HasGroup=request.json['HasGroup'],group=request.json['group'],
        Position=request.json['Position'],HasAccessedInput=request.json['HasAccessedInput'],Input=request.json['Input'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

# Traceability

class AddCropInfo(Resource):	
    def post(self):
        new_data = CropInfo(tracing_id=request.json['tracing_id'],crop_type=request.json['crop_type'],sourcing_location=request.json['sourcing_location'],
        crop_origin=request.json['crop_origin'],crop_qty=request.json['crop_qty'],crop_variety=request.json['crop_variety'],
        cooperative=request.json['cooperative'],no_of_farmer_group=request.json['no_of_farmer_group'],
        female_to_male=request.json['female_to_male'],farmer_name=request.json['farmer_name'],gender=request.json['gender'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


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
        return new_data.json()


class AddInputsInfo(Resource):	
    def post(self):
        new_data = InputsInfo(tracing_id=request.json['tracing_id'],Fertilizers=request.json['Fertilizers'],Herbicides=request.json['Herbicides'],
        Fungicides=request.json['Fungicides'],Insecticides=request.json['Insecticides'],Seeds=request.json['Seeds'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


class AddWarehouse(Resource):	
    def post(self):
        new_data = Warehouse(tracing_id=request.json['tracing_id'],location=request.json['location'],warehouse_type=request.json['warehouse_type'],
        capacity=request.json['capacity'],standard=request.json['standard'],insurance=request.json['insurance'],
        duration=request.json['duration'],cost=request.json['cost'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

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
        return new_data.json()

class AddRecommendation(Resource):	
    def post(self):
        new_data = Recommendation(tracing_id=request.json['tracing_id'],rec_one=request.json['rec_one'],
        rec_two=request.json['rec_two'],rec_three=request.json['rec_three'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

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
        return {'message':'success'}
# Credit Scoring
class AddScoreCard(Resource):	
    def post(self):
        recommendations = 'Success!'
        bvn=request.json['bvn']
        farmer = ScoreCard.query.filter_by(bvn=bvn).all()
        if farmer:
            recommendations+='Scorecard Exists!'
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
        bvn=request.json['bvn']
        farmer = FarmerTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add KYF!'
        farmer = CapitalTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add Capital!'
        farmer = CreditHistoryTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add Character!'
        farmer = FarmlandTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add Collateral!'
        farmer = CapacityTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add Capacity!'
        farmer = ConditionsTable.query.filter_by(bvn=bvn).all()
        if not farmer:
            recommendations+='Add Conditions!'
        #return {'message':recommendations}
        
        farmer = ScoreHistory.query.filter_by(bvn=bvn).all()
        if not farmer:
            farmer = pd.DataFrame([['bvn','age','number_of_land','address',
        'owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender',
        'owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits']],columns=['bvn','age','number_of_land','address',
        'owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender',
        'owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits'])
            for col in farmer.columns:
                farmer[col] = request.json[col]
        #farmer = pd.DataFrame(card, index=[0])
            print(farmer)
            farmer['applyLoanAmount'] = 50000
            farmer = farmer.rename({
            'number_of_land':'numberOfLand','estimate_monthly_income':'estimateMonthlyIncome',
            'years_cultivating':'yearsCultivating'
        },axis=1)
            cols=['age', 'numberOfLand', 'owner_caretaker', 'crop','applyLoanAmount',
            'intercropping', 'machines', 'estimateMonthlyIncome','yearsCultivating']
            tdf = preprocess_df(farmer[cols])
            train_cols = ['numberOfLand', 'owner_caretaker', 'intercropping', 'machines',
       'estimateMonthlyIncome',
        'applyLoanAmount',
         'yearsCultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
            score = model.predict_proba(tdf[train_cols])[:,1].round(2)
            bin=bin_target(score)
            history = ScoreHistory(bvn=request.json['bvn'],age=request.json['age'],
        number_of_land=request.json['number_of_land'],address=request.json['address'],
        owner_caretaker=request.json['owner_caretaker'],crop=request.json['crop'],
        intercropping=request.json['intercropping'], machines=request.json['machines'],
        estimate_monthly_income=request.json['estimate_monthly_income'],
        years_cultivating=request.json['years_cultivating'],gender=request.json['gender'],
        owns_a_bank_account=request.json['owns_a_bank_account'],size_of_farm=request.json['size_of_farm'],
        number_of_crops=request.json['number_of_crops'],is_in_a_cooperative=request.json['is_in_a_cooperative'],
        no_of_agronomist_visits=request.json['no_of_agronomist_visits'],
        applyLoanAmount=farmer['applyLoanAmount'][0],
        term_months='term_months',score=score[0], bin=bin[0])
            db.session.add(history)
            db.session.commit()
        return jsonify({'message':recommendations})

class Scorecardbvn(Resource):
    def get(self, bvn):
        cards = ScoreCard.query.filter_by(bvn=bvn).all()
        if cards:
            return [card.json() for card in cards]
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        cards = ScoreCard.query.filter_by(bvn=bvn).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"})
        return {'message':'success'}

class Cropcardbvn(Resource):
    def get(self, bvn):
        cards = Cropcard.query.filter_by(bvn=bvn).all()
        if cards:
            return [card.json() for card in cards]
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        cards = Cropcard.query.filter_by(bvn=bvn).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"})
        return {'message':'success'}
class Cropcardcrop_name(Resource):
    def get(self, crop_name):
        cards = Cropcard.query.filter_by(crop_name=crop_name).all()
        if cards:
            return [card.json() for card in cards]
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"crop_name Not Found"},404
    def delete(self, crop_name):
        cards = Cropcard.query.filter_by(crop_name=crop_name).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"crop_name Not Found"})
        return {'message':'success'}
class ScoreHistorybvn(Resource):
    def get(self, bvn):
        farmer = ScoreHistory.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = ScoreHistory.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"})
        return {'message':'success'}

class ScoreHistoryid(Resource):
    def get(self, id):
        farmer = ScoreHistory.query.filter_by(id=id).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id Not Found"},404
    def delete(self, id):
        farmer = ScoreHistory.query.filter_by(id=id).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"id Not Found"})
        return {'message':'success'}

class ScoreFarmer(Resource):
    def post(self):
        bvn=request.json['bvn']
        #applyLoanAmount=request.json['applyLoanAmount']
        #term_months=request.json['term_months']
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
        term_months=request.json['term_months'],score=score, bin=bin)
            db.session.add(history)
            db.session.commit()
            return {'bvn':bvn, 'score':score, 'bin':bin }
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class ScoreFarmerDragAndDrop(Resource):
    def post(self):
        bvn=request.json['bvn']
        applyLoanAmount=request.json['applyLoanAmount']
        #term_months=request.json['term_months']
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
        term_months=request.json['term_months'],score=score, bin=bin)
            db.session.add(history)
            db.session.commit()
            return {'bvn':bvn, 'score':score, 'bin':bin }
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
# Loans

class AddLoan(Resource):	
    def post(self):
        loan_type=request.json['loan_type']
        loan = Loan.query.filter_by(loan_type=loan_type).first()
        if loan:
            message = {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Loan type already exists!"}
        if not loan:
            new_data = Loan(
        loan_type=request.json['loan_type'],
        repayment_months=request.json['repayment_months'],
        interest_rate_per_annum=request.json['interest_rate_per_annum']
        )
            db.session.add(new_data)
            db.session.commit()
            message = {'message':'success'}
        return message

class AddLoanTransfer(Resource):	
    def post(self):
        new_data = LoanTransfer(loan_type=request.json['loan_type'],amount=request.json['amount'],
        repayment_amount=request.json['repayment_amount'],
        status=request.json['status'],farmer_name=request.json['farmer_name'],bvn=request.json['bvn'],
        transfer_date=request.json['transfer_date'],due_date=request.json['due_date'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class Loanloan_type(Resource):
    def get(self, loan_type):
        loan = Loan.query.filter_by(loan_type=loan_type).first()
        if loan:
            return loan.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"loan_type Not Found"},404
    def delete(self, loan_type):
        loan = Loan.query.filter_by(loan_type=loan_type).first()
        db.session.delete(loan)
        db.session.commit()
        return {'message':'success'}

# -----------Traceability----------------------------------------------------------------------------------------

class CropInfoTracing(Resource):
    def get(self, tracing_id):
        farmer = CropInfo.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, tracing_id):
        farmer = CropInfo.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'message':'success'}

class CropQualityTracing(Resource):
    def get(self, tracing_id):
        farmer = CropQuality.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, tracing_id):
        farmer = CropQuality.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'message':'success'}

class ShipmentTracing(Resource):
    def get(self, tracing_id):
        farmer = Shipment.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, tracing_id):
        farmer = Shipment.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'message':'success'}
class InputsInfoTracing(Resource):
    def get(self, tracing_id):
        farmer = InputsInfo.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, tracing_id):
        farmer = InputsInfo.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'message':'success'}

class RecommendationTracing(Resource):
    def get(self, tracing_id):
        farmer = Recommendation.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, tracing_id):
        farmer = Recommendation.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'message':'success'}

# ------------Get Requests-------------------------------------------------------------------------------------------------

class Farmerbvn(Resource):
    def get(self, bvn):
        farmer = FarmerTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = FarmerTable.query.filter_by(bvn=bvn).first()
        if farmer:
            farmer = FarmerTable.query.filter_by(bvn=bvn).first()
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    

class Agronomybvn(Resource):
    def get(self, bvn):
        farmer = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    

class Capacitybvn(Resource):
    def get(self, bvn):
        farmer = CapacityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = CapacityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Capitalbvn(Resource):
    def get(self, bvn):
        farmer = CapitalTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = CapitalTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Carebvn(Resource):
    def get(self, bvn):
        farmer = CareTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = CareTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Conditionsbvn(Resource):
    def get(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class CreditAccessbvn(Resource):
    def get(self, bvn):
        farmer = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Capital5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CapitalTable.query.filter_by(bvn=bvn).first()
        farmer2 = CreditAccessTable.query.filter_by(bvn=bvn).first()
        if not farmer1:
            farmer1='{"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}'
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer2=farmer2.json()
        return {'capital':farmer1,'creditaccess':farmer2}
        
class Character5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        farmer2 = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        farmer3 = AgronomyServicesTable.query.filter_by(bvn=bvn).first()
        farmer4 = PsychometricsTable.query.filter_by(bvn=bvn).first()
        farmer5 = MobileDataTable.query.filter_by(bvn=bvn).first()
        
        if not farmer1:
            farmer1='{"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}'
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer2=farmer2.json()
        if not farmer3:
            farmer3={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer3=farmer3.json()
        if not farmer4:
            farmer4={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer4=farmer4.json()
        if not farmer5:
            farmer5={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer5=farmer5.json()
        return {'credithistory':farmer1,'productivity':farmer2,'agronomy':farmer3,'psychometrics':farmer4,'mobiledata':farmer5}
        
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
        return {'message':'success'}

class Collateral5cbvn(Resource):
    def get(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {'farmland':farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not in FarmlandTable"})
        return {'message':'success'}
class Capacity5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CapacityTable.query.filter_by(bvn=bvn).first()
        farmer2 = FarmPractice.query.filter_by(bvn=bvn).first()
        farmer3 = MechanizationTable.query.filter_by(bvn=bvn).first()
        farmer4 = CultivationTable.query.filter_by(bvn=bvn).first()
        farmer5 = HarvestTable.query.filter_by(bvn=bvn).first()
        
        if not farmer1:
            farmer1='{"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}'
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer2=farmer2.json()
        if not farmer3:
            farmer3={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer3=farmer3.json()
        if not farmer4:
            farmer4={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer4=farmer4.json()
        if not farmer5:
            farmer5={"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"}
        else:
            farmer5=farmer5.json()
        return {'capacity':farmer1,'practice':farmer2,'mechanization':farmer3,'cultivation':farmer4,'harvest':farmer5}
        
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
        return {'message':'success'}
class Conditions5cbvn(Resource):
    def get(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return {'conditions':farmer.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = ConditionsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
        else:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not in FarmlandTable"})
        return {'message':'success'}
class CreditHistorybvn(Resource):
    def get(self, bvn):
        farmer = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = CreditHistoryTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    

class Cultivationbvn(Resource):
    def get(self, bvn):
        farmer = CultivationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = CultivationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Farmlandbvn(Resource):
    def get(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = FarmlandTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Harvestbvn(Resource):
    def get(self, bvn):
        farmer = HarvestTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = HarvestTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Livingbvn(Resource):
    def get(self, bvn):
        farmer = LivingTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = LivingTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Mechanizationbvn(Resource):
    def get(self, bvn):
        farmer = MechanizationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = MechanizationTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    

class MobileDatabvn(Resource):
    def get(self, bvn):
        farmer = MobileDataTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = MobileDataTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    

class Planetbvn(Resource):
    def get(self, bvn):
        farmer = Planet.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = Planet.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Practicebvn(Resource):
    def get(self, bvn):
        farmer = FarmPractice.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = FarmPractice.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    

class Productivitybvn(Resource):
    def get(self, bvn):
        farmer = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = ProductivityViabilityTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
    
class Psychometricsbvn(Resource):
    def get(self, bvn):
        farmer = PsychometricsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = PsychometricsTable.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Safetybvn(Resource):
    def get(self, bvn):
        farmer = Safety.query.filter_by(bvn=bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = Safety.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    

class Transferbvn(Resource):
    def get(self, bvn):
        farmer = LoanTransfer.query.filter_by(bvn=bvn).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({'status': 'success','transfers': transfers})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    def delete(self, bvn):
        farmer = LoanTransfer.query.filter_by(bvn=bvn).all()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"bvn Not Found"},404
    
class Transferid(Resource):
    def get(self, id):
        farmer = LoanTransfer.query.filter_by(id=id).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({'status': 'success','transfers': transfers})
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id Not Found"},404
    def delete(self, id):
        farmer = LoanTransfer.query.filter_by(id=id).all()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"id Not Found"},404
    
# All Loans, Farmers

class AllFarmers(Resource):
    def get(self):
        all_farmers = FarmerTable.query.all()        
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})
        

class AllAgronomy(Resource):
    def get(self):
        all_farmers = AgronomyServicesTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllCapacity(Resource):
    def get(self):
        all_farmers = CapacityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllCapital(Resource):
    def get(self):
        all_farmers = CapitalTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllCare(Resource):
    def get(self):
        all_farmers = CareTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllConditions(Resource):
    def get(self):
        all_farmers = ConditionsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllCreditAccess(Resource):
    def get(self):
        all_farmers = CreditAccessTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})
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
        return jsonify({'status': 'success','farmers': all_farmers})

class AllCropInfo(Resource):
    def get(self):
        all_farmers = CropInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllCropQuality(Resource):
    def get(self):
        all_farmers = CropQuality.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllCultivation(Resource):
    def get(self):
        all_farmers = CultivationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllFarmland(Resource):
    def get(self):
        all_farmers = FarmlandTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllHarvest(Resource):
    def get(self):
        all_farmers = HarvestTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllInputsInfo(Resource):
    def get(self):
        all_farmers = InputsInfo.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllLiving(Resource):
    def get(self):
        all_farmers = LivingTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllMechanization(Resource):
    def get(self):
        all_farmers = MechanizationTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllMobileData(Resource):
    def get(self):
        all_farmers = MobileDataTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllPlanet(Resource):
    def get(self):
        all_farmers = Planet.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllPractice(Resource):
    def get(self):
        all_farmers = FarmPractice.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllProductivity(Resource):
    def get(self):
        all_farmers = ProductivityViabilityTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllPsychometrics(Resource):
    def get(self):
        all_farmers = PsychometricsTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllRecommendation(Resource):
    def get(self):
        all_farmers = Recommendation.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllSafety(Resource):
    def get(self):
        all_farmers = Safety.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})
class AllScorecard(Resource):
    def get(self):
        all_farmers = ScoreCard.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})
class AllCropcard(Resource):
    def get(self):
        all_cards = Cropcard.query.all()
        return [card.json() for card in all_cards]
class AllScoreHistory(Resource):
    def get(self):
        all_farmers = ScoreHistory.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})


class AllShipment(Resource):
    def get(self):
        all_farmers = Shipment.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllTransfer(Resource):
    def get(self):
        all_farmers = LoanTransfer.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllWarehouse(Resource):
    def get(self):
        all_farmers = Warehouse.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'status': 'success','farmers': all_farmers})

class AllLoans(Resource):
    def get(self):
        all_loans = db.session.query(Loan).all()
        all_loans = [loan.json() for loan in all_loans]
        return jsonify({'status': 'success','loans': all_loans})



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
            return {'message':'Upload success'}


add = api.namespace('api',description='Add New Data')
add.add_resource(AddFarmer,'/farmer/add')
add.add_resource(AddScoreCard,'/scorecard/add')
add.add_resource(AddCropCard,'/cropcard/add')
add.add_resource(AddCapital,'/capital/add')
add.add_resource(AddCreditAccess,'/creditaccess/add')
add.add_resource(AddCreditHistory,'/credithistory/add')
add.add_resource(AddProductivityViability,'/productivity/add')
add.add_resource(AddCapacity,'/capacity/add')
add.add_resource(AddAgronomyServices,'/agronomy/add')
add.add_resource(AddConditions,'/conditions/add')
add.add_resource(AddCultivation,'/cultivation/add')
add.add_resource(AddFarmlandData,'/farmland/add')
add.add_resource(AddFarmPractice,'/practice/add')
add.add_resource(AddPsychometrics,'/psychometrics/add')
add.add_resource(AddMechanization,'/mechanization/add')
add.add_resource(AddMobileData,'/mobiledata/add')
add.add_resource(AddHarvest,'/harvest/add')
add.add_resource(AddLoan,'/loan/add')
add.add_resource(AddLoanTransfer,'/transfer/add')
add.add_resource(AddLivingTable,'/living/add')
add.add_resource(AddCareTable,'/care/add')
add.add_resource(AddCropInfo,'/crop_info/add')
add.add_resource(AddCropQuality,'/crop_quality/add')
add.add_resource(AddInputsInfo,'/inputs_info/add')
add.add_resource(AddPlanet,'/planet/add')
add.add_resource(AddRecommendation,'/recommendation/add')
add.add_resource(AddShipment,'/shipment/add')
add.add_resource(AddSafety,'/safety/add')
add.add_resource(AddWarehouse,'/warehouse/add')
add.add_resource(AddScoreAnalytics,'/score_analytics/add')
# 5c API Routes
add.add_resource(AddCapital5c,'/5c_capital/add')
add.add_resource(AddCapacity5c,'/5c_capacity/add')
add.add_resource(AddCharacter5c,'/5c_character/add')
add.add_resource(AddCollateral5c,'/5c_collateral/add')
add.add_resource(AddConditions5c,'/5c_conditions/add')


scorefarmer = api.namespace('api/score', description='credit scoring')
scorefarmer.add_resource(ScoreFarmer,'/')
scorefarmer.add_resource(ScoreFarmerDragAndDrop,'/filter')

farmer = api.namespace('api/farmer', description='know your farmer')
farmer.add_resource(Farmerbvn,'/bvn=<bvn>')
farmer.add_resource(AllFarmers,'/all')

care = api.namespace('api/care', description='access to healthcare and education')
care.add_resource(Carebvn,'/bvn=<bvn>')
care.add_resource(AllCare,'/all')

living = api.namespace('api/living', description='how farmer has been living')
living.add_resource(Livingbvn,'/bvn=<bvn>')
living.add_resource(AllLiving,'/all')

planet = api.namespace('api/planet', description='nature of crops and lands')
planet.add_resource(Planetbvn,'/bvn=<bvn>')
planet.add_resource(AllPlanet,'/all')

safety = api.namespace('api/safety', description='food safety and quality')
safety.add_resource(Safetybvn,'/bvn=<bvn>')
safety.add_resource(AllSafety,'/all')

capital = api.namespace('api/capital', description='farmer capital')
capital.add_resource(Capitalbvn,'/bvn=<bvn>')
capital.add_resource(AllCapital,'/all')

harvest = api.namespace('api/harvest', description='farmer harvest')
harvest.add_resource(Harvestbvn,'/bvn=<bvn>')
harvest.add_resource(AllHarvest,'/all')

agronomy = api.namespace('api/agronomy', description='farmer agronomy')
agronomy.add_resource(Agronomybvn,'/bvn=<bvn>')
agronomy.add_resource(AllAgronomy,'/all')

capacity = api.namespace('api/capacity', description='farmer capacity')
capacity.add_resource(Capacitybvn,'/bvn=<bvn>')
capacity.add_resource(AllCapacity,'/all')

farmland = api.namespace('api/farmland', description='farmland')
farmland.add_resource(Farmlandbvn,'/bvn=<bvn>')
farmland.add_resource(AllFarmland,'/all')

transfer = api.namespace('api/transfer', description='loan transfers')
transfer.add_resource(Transferbvn,'/bvn=<bvn>')
transfer.add_resource(Transferid,'/id=<id>')
transfer.add_resource(AllTransfer,'/all')

practice = api.namespace('api/practice', description='farm practice')
practice.add_resource(Practicebvn,'/bvn=<bvn>')
practice.add_resource(AllPractice,'/all')

scorecard = api.namespace('api/scorecard', description='scorecard')
scorecard.add_resource(Scorecardbvn,'/bvn=<bvn>')
scorecard.add_resource(AllScorecard,'/all')

cropcard = api.namespace('api/cropcard', description='cropcard')
cropcard.add_resource(Cropcardbvn,'/bvn=<bvn>')
cropcard.add_resource(Cropcardcrop_name,'/crop_name=<crop_name>')
cropcard.add_resource(AllCropcard,'/all')

scorehistory = api.namespace('api/scorehistory', description='scorehistory')
scorehistory.add_resource(ScoreHistorybvn,'/bvn=<bvn>')
scorehistory.add_resource(ScoreHistoryid,'/id=<id>')
scorehistory.add_resource(AllScoreHistory,'/all')

conditions = api.namespace('api/conditions', description='conditions')
conditions.add_resource(Conditionsbvn,'/bvn=<bvn>')
conditions.add_resource(AllConditions,'/all')

mobiledata = api.namespace('api/mobiledata', description='mobiledata')
mobiledata.add_resource(MobileDatabvn,'/bvn=<bvn>')
mobiledata.add_resource(AllMobileData,'/all')

cultivation = api.namespace('api/cultivation', description='cultivation')
cultivation.add_resource(Cultivationbvn,'/bvn=<bvn>')
cultivation.add_resource(AllCultivation,'/all')

creditaccess = api.namespace('api/creditaccess', description='credit access')
creditaccess.add_resource(CreditAccessbvn,'/bvn=<bvn>')
creditaccess.add_resource(AllCreditAccess,'/all')

productivity = api.namespace('api/productivity', description='productivity viability')
productivity.add_resource(Productivitybvn,'/bvn=<bvn>')
productivity.add_resource(AllProductivity,'/all')

credithistory = api.namespace('api/credithistory', description='credit history')
credithistory.add_resource(CreditHistorybvn,'/bvn=<bvn>')
credithistory.add_resource(AllCreditHistory,'/all')

mechanization = api.namespace('api/mechanization', description='mechanization')
mechanization.add_resource(Mechanizationbvn,'/bvn=<bvn>')
mechanization.add_resource(AllMechanization,'/all')

psychometrics = api.namespace('api/psychometrics', description='psychometrics')
psychometrics.add_resource(Psychometricsbvn,'/bvn=<bvn>')
psychometrics.add_resource(AllPsychometrics,'/all')

crop_info = api.namespace('api/crop_info', description='crop information traceability')
crop_info.add_resource(CropInfoTracing,'/tracing_id=<tracing_id>')
crop_info.add_resource(AllCropInfo,'/all')

crop_quality = api.namespace('api/crop_quality', description='crop quality traceability')
crop_quality.add_resource(CropQualityTracing,'/tracing_id=<tracing_id>')
crop_quality.add_resource(AllCropQuality,'/all')

shipment = api.namespace('api/shipment', description='shipment traceability')
shipment.add_resource(ShipmentTracing,'/tracing_id=<tracing_id>')
shipment.add_resource(AllShipment,'/all')

inputs_info = api.namespace('api/inputs_info', description='inputs_info traceability')
inputs_info.add_resource(InputsInfoTracing,'/tracing_id=<tracing_id>')
inputs_info.add_resource(AllInputsInfo,'/all')

recommendation = api.namespace('api/recommendation', description='recommendation traceability')
recommendation.add_resource(RecommendationTracing,'/tracing_id=<tracing_id>')
recommendation.add_resource(AllRecommendation,'/all')

loans = api.namespace('api/loan',description='load loans')
loans.add_resource(Loanloan_type,'/loan_type=<loan_type>')
loans.add_resource(AllLoans,'/all')

bulk = api.namespace('api/bulk', description='bulk files')
bulk.add_resource(AddBulkFarmer,'/farmer')

capital5c = api.namespace('api/5c_capital', description='farmer 5c_capital')
capital5c.add_resource(Capital5cbvn,'/bvn=<bvn>')
capital5c.add_resource(AllCapital5c,'/all')

character5c = api.namespace('api/5c_character', description='farmer 5c_character')
character5c.add_resource(Character5cbvn,'/bvn=<bvn>')
character5c.add_resource(AllCharacter5c,'/all')

collateral5c = api.namespace('api/5c_collateral', description='farmer 5c_collateral')
collateral5c.add_resource(Collateral5cbvn,'/bvn=<bvn>')
collateral5c.add_resource(AllCollateral5c,'/all')

capacity5c = api.namespace('api/5c_capacity', description='farmer 5c_capacity')
capacity5c.add_resource(Capacity5cbvn,'/bvn=<bvn>')
capacity5c.add_resource(AllCapacity5c,'/all')

conditions5c = api.namespace('api/5c_conditions', description='farmer 5c_conditions')
conditions5c.add_resource(Conditions5cbvn,'/bvn=<bvn>')
conditions5c.add_resource(AllConditions5c,'/all')

# Running app
if __name__ == '__main__':
    
    app.run(debug=True)
