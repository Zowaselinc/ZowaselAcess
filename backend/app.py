# Import flask 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api, fields
from flask_mysqldb import MySQL

from models import app, db,FarmerTable,ScoreCard, Loan, CapitalTable,CreditAccessTable,CreditHistoryTable,ProductivityViabilityTable,LoanTransfer
from models import AgronomyServicesTable, PsychometricsTable, MobileDataTable, FarmlandTable, CapacityTable, FarmPractice, MechanizationTable, CultivationTable, HarvestTable, ConditionsTable
from models import CareTable, Planet, Safety, LivingTable, CropInfo, CropQuality, InputsInfo, Warehouse, Shipment, Recommendation, ScoreAnalytics
from models import ScoreHistory
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

# Post Requests

# return {"error":True,"message":"Sorry your request can not be processed at the moment","data":""}


# Kyf

class AddFarmer(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = FarmerTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            message = {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmerkyf = FarmerTable(id=request.form['Bvn'],FirstName=request.form['FirstName'],Surname=request.form['Surname'],
        Middlename=request.form['Middlename'],Telephone=request.form['Telephone'],Age=request.form['Age'],
        Gender=request.form['Gender'],Language = request.form['Language'],MaritalStatus=request.form['MaritalStatus'],
        Bankname = request.form['Bankname'],Accountno = request.form['Accountno'],Bvn=request.form['Bvn'],
        MeansofID=request.form['MeansofID'],Issuedate=request.form['Issuedate'],Expirydate=request.form['Expirydate'],
        Nin=request.form['Nin'],PermanentAddress=request.form['PermanentAddress'],Landmark=request.form['Landmark'],
        Stateoforigin=request.form['Stateoforigin'],IsinaGroup = request.form['IsinaGroup'],
        ReasonNoGroup = request.form['ReasonNoGroup'],Group=request.form['Group'],
        NumberofMembers = request.form['NumberofMembers'],FirstNameNok = request.form['FirstNameNok'],
        SurnameNok = request.form['SurnameNok'],MiddlenameNok = request.form['MiddlenameNok'], 
        RelationshipNok = request.form['RelationshipNok'],OccupationNok     = request.form['OccupationNok'],
        TelephoneNok  = request.form['TelephoneNok'],PermanentAddressNok  = request.form['PermanentAddressNok'],
        LandmarkNok  = request.form['LandmarkNok'],NinNok  = request.form['NinNok'])
            db.session.add(farmerkyf)
            db.session.commit()
            message = {'message':'success'}
        return message

# -------------5cs of Credit Scoring-------------------------------------------------------------------------------------

# 1.Capital

class AddCapital(Resource):	
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CapitalTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmercapital = CapitalTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],MainIncomeSource=request.form['MainIncomeSource'],
        OtherIncomeSource=request.form['OtherIncomeSource'],NoOfIncomeEarners=request.form['NoOfIncomeEarners'],
        HasBankAccount=request.form['HasBankAccount'],FirstFundingOption=request.form['FirstFundingOption'],
        NeedsALoan=request.form['NeedsALoan'],PayBackMonths=request.form['PayBackMonths'],
        HarvestQtyChanged=request.form['HarvestQtyChanged'],PestExpenseChanged=request.form['PestExpenseChanged'])
            db.session.add(farmercapital)
            db.session.commit()
            return {'message':'success'}
        
class AddCreditAccess(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CreditAccessTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmercreditaccess = CreditAccessTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        HasServedAsTreasurer=request.form['HasServedAsTreasurer'],DurationAsTreasurer=request.form['DurationAsTreasurer'],
        SavesMoneyMonthly=request.form['SavesMoneyMonthly'],SavingsAmount=request.form['SavingsAmount'],
        HadDifficultyRepaying=request.form['HadDifficultyRepaying'],DifficultLoanAmount=request.form['DifficultLoanAmount'],
        DifficultyReason=request.form['DifficultyReason'],NoOfDifficultLoans=request.form['NoOfDifficultLoans'],
        NoOfRepaidLoans=request.form['NoOfRepaidLoans'],NoOfLoansOnTime=request.form['NoOfLoansOnTime'],
        EstMonthlyIncome=request.form['EstMonthlyIncome'],CostOfCultivation=request.form['CostOfCultivation'],
        FarmProduceExchanged=request.form['FarmProduceExchanged'],NoOfTimesExchanged=request.form['NoOfTimesExchanged'],
        Collateral=request.form['Collateral'],ApplyLoanAmount=request.form['ApplyLoanAmount'],
        YearsOfCultivating=request.form['Collateral'],AnnualTurnover=request.form['AnnualTurnover'])
            db.session.add(farmercreditaccess)
            db.session.commit()
            return {'message':'success'}


class AddCapital5c(Resource):	
    def post(self):
        farmercapital = CapitalTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],MainIncomeSource=request.form['MainIncomeSource'],
        OtherIncomeSource=request.form['OtherIncomeSource'],NoOfIncomeEarners=request.form['NoOfIncomeEarners'],
        HasBankAccount=request.form['HasBankAccount'],FirstFundingOption=request.form['FirstFundingOption'],
        NeedsALoan=request.form['NeedsALoan'],PayBackMonths=request.form['PayBackMonths'],
        HarvestQtyChanged=request.form['HarvestQtyChanged'],PestExpenseChanged=request.form['PestExpenseChanged'])
        farmercreditaccess = CreditAccessTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        HasServedAsTreasurer=request.form['HasServedAsTreasurer'],DurationAsTreasurer=request.form['DurationAsTreasurer'],
        SavesMoneyMonthly=request.form['SavesMoneyMonthly'],SavingsAmount=request.form['SavingsAmount'],
        HadDifficultyRepaying=request.form['HadDifficultyRepaying'],DifficultLoanAmount=request.form['DifficultLoanAmount'],
        DifficultyReason=request.form['DifficultyReason'],NoOfDifficultLoans=request.form['NoOfDifficultLoans'],
        NoOfRepaidLoans=request.form['NoOfRepaidLoans'],NoOfLoansOnTime=request.form['NoOfLoansOnTime'],
        EstMonthlyIncome=request.form['EstMonthlyIncome'],CostOfCultivation=request.form['CostOfCultivation'],
        FarmProduceExchanged=request.form['FarmProduceExchanged'],NoOfTimesExchanged=request.form['NoOfTimesExchanged'],
        Collateral=request.form['Collateral'],ApplyLoanAmount=request.form['ApplyLoanAmount'],
        YearsOfCultivating=request.form['Collateral'],AnnualTurnover=request.form['AnnualTurnover'])
        # Add data only if Id does not exist in database already
        farmer = CapitalTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists in Capital!"})     
        else:
            db.session.add(farmercapital)
            db.session.commit()
        # Add data only if Id does not exist in database already
        farmer = CreditAccessTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            print({"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists in Credit Access!"})
        else:
            db.session.add(farmercreditaccess)
            db.session.commit()
        return {'message':'success'}


# 2.Character

class AddCreditHistory(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = CreditHistoryTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmercredithistory = CreditHistoryTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        HasTakenLoanBefore=request.form['HasTakenLoanBefore'],SourceOfLoan=request.form['SourceOfLoan'],
        PastLoanAmount=request.form['PastLoanAmount'],HowLoanWasRepaid=request.form['HowLoanWasRepaid'],
        IsReadyToPayInterest=request.form['IsReadyToPayInterest'],CanProvideCollateral=request.form['CanProvideCollateral'],
        WhyNoCollateral=request.form['WhyNoCollateral'])
            db.session.add(farmercredithistory)
            db.session.commit()
            return farmercredithistory.json()

class AddProductivityViability(Resource):
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = ProductivityViabilityTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmerproductivity = ProductivityViabilityTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        CropsCultivated=request.form['CropsCultivated'],GrowsCrops=request.form['GrowsCrops'],
        OilPalmFertilizers=request.form['OilPalmFertilizers'],CocoaFertilizers=request.form['CocoaFertilizers'],
        FertilizerFrequency=request.form['FertilizerFrequency'],PestFungHerbicides=request.form['PestFungHerbicides'],
        StageChemicalApplied=request.form['StageChemicalApplied'],NoOfOilDrums=request.form['NoOfOilDrums'],
        NoOfBagsSesame=request.form['NoOfBagsSesame'],NoOfBagsSoyaBeans=request.form['NoOfBagsSoyaBeans'],
        NoOfBagsMaize=request.form['NoOfBagsMaize'],NoOfBagsSorghum=request.form['NoOfBagsSorghum'],
        NoOfBagsCocoaBeans=request.form['NoOfBagsCocoaBeans'],CropTrainedOn=request.form['CropTrainedOn'],
        WhereWhenWhoTrained=request.form['WhereWhenWhoTrained'],NoOfTraining=request.form['NoOfTraining'],
        PruningFrequency=request.form['PruningFrequency'],CropBasedProblems=request.form['CropBasedProblems'],
        TooYoungCrops=request.form['TooYoungCrops'],YoungCropsAndStage=request.form['YoungCropsAndStage'],
        CultivationStartdate=request.form['CultivationStartdate'],IsIntensiveFarmingPractised=request.form['IsIntensiveFarmingPractised'],
        EconomicActivities=request.form['EconomicActivities'])
            db.session.add(farmerproductivity)
            db.session.commit()
            return farmerproductivity.json()

class AddAgronomyServices(Resource):	
    def post(self):
        # Add data only if Id does not exist in database already
        farmer = AgronomyServicesTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmeragronomy = AgronomyServicesTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        KnowsAgriProcessed=request.form['KnowsAgriProcessed'],AgronomistThatTrainedYou=request.form['AgronomistThatTrainedYou'],
        CanManageEcosystem=request.form['CanManageEcosystem'],HowToManageEcosystem=request.form['HowToManageEcosystem'],
        IsTrainingBeneficial=request.form['IsTrainingBeneficial'],FieldRoutines=request.form['FieldRoutines'],
        HarvestingChanges=request.form['HarvestingChanges'],IsCropCalendarBeneficial=request.form['IsCropCalendarBeneficial'],
        CropCalendarBenefits=request.form['CropCalendarBenefits'],RecordKeepingBenefits=request.form['RecordKeepingBenefits'])
            db.session.add(farmeragronomy)
            db.session.commit()
            return farmeragronomy.json()
class AddPsychometrics(Resource):	
    def post(self):
        farmer = PsychometricsTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmerpsychometrics = PsychometricsTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],FluidIntelligence=request.form['FluidIntelligence'],
        AttitudesandBeliefs=request.form['AttitudesandBeliefs'],AgribusinessSkills=request.form['AgribusinessSkills'],
        EthicsandHonesty=request.form['EthicsandHonesty'],SavesEnough=request.form['SavesEnough'],
        HasLazyNeighbors=request.form['HasLazyNeighbors'])
            db.session.add(farmerpsychometrics)
            db.session.commit()
            return farmerpsychometrics.json()

class AddMobileData(Resource):	
    def post(self):
        farmer = MobileDataTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmermobiledata = MobileDataTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],MobilePhoneType=request.form['MobilePhoneType'],
        Avweeklyphoneuse=request.form['Avweeklyphoneuse'],Callsoutnumber=request.form['Callsoutnumber'],
        Callsoutminutes=request.form['Callsoutminutes'],Callsinnumber=request.form['Callsinnumber'],
        Callinminutes=request.form['Callinminutes'],SMSsent=request.form['SMSsent'],
        Dataprecedingplanswitch=request.form['Dataprecedingplanswitch'],Billpaymenthistory=request.form['Billpaymenthistory'],
        Avweeklydatarefill=request.form['Avweeklydatarefill'],NoOfmobileapps=request.form['NoOfmobileapps'],
        AvTimeSpentOnApp=request.form['AvTimeSpentOnApp'],MobileAppKinds=request.form['MobileAppKinds'],
        AppDeleteRate=request.form['AppDeleteRate'])
            db.session.add(farmermobiledata)
            db.session.commit()
            return farmermobiledata.json()


class AddCharacter5c(Resource):
    def post(self):
        farmercredithistory = CreditHistoryTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        HasTakenLoanBefore=request.form['HasTakenLoanBefore'],SourceOfLoan=request.form['SourceOfLoan'],
        PastLoanAmount=request.form['PastLoanAmount'],HowLoanWasRepaid=request.form['HowLoanWasRepaid'],
        IsReadyToPayInterest=request.form['IsReadyToPayInterest'],CanProvideCollateral=request.form['CanProvideCollateral'],
        WhyNoCollateral=request.form['WhyNoCollateral'])
        farmerproductivity = ProductivityViabilityTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        CropsCultivated=request.form['CropsCultivated'],GrowsCrops=request.form['GrowsCrops'],
        OilPalmFertilizers=request.form['OilPalmFertilizers'],CocoaFertilizers=request.form['CocoaFertilizers'],
        FertilizerFrequency=request.form['FertilizerFrequency'],PestFungHerbicides=request.form['PestFungHerbicides'],
        StageChemicalApplied=request.form['StageChemicalApplied'],NoOfOilDrums=request.form['NoOfOilDrums'],
        NoOfBagsSesame=request.form['NoOfBagsSesame'],NoOfBagsSoyaBeans=request.form['NoOfBagsSoyaBeans'],
        NoOfBagsMaize=request.form['NoOfBagsMaize'],NoOfBagsSorghum=request.form['NoOfBagsSorghum'],
        NoOfBagsCocoaBeans=request.form['NoOfBagsCocoaBeans'],CropTrainedOn=request.form['CropTrainedOn'],
        WhereWhenWhoTrained=request.form['WhereWhenWhoTrained'],NoOfTraining=request.form['NoOfTraining'],
        PruningFrequency=request.form['PruningFrequency'],CropBasedProblems=request.form['CropBasedProblems'],
        TooYoungCrops=request.form['TooYoungCrops'],YoungCropsAndStage=request.form['YoungCropsAndStage'],
        CultivationStartdate=request.form['CultivationStartdate'],IsIntensiveFarmingPractised=request.form['IsIntensiveFarmingPractised'],
        EconomicActivities=request.form['EconomicActivities'])
        farmeragronomy = AgronomyServicesTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        KnowsAgriProcessed=request.form['KnowsAgriProcessed'],AgronomistThatTrainedYou=request.form['AgronomistThatTrainedYou'],
        CanManageEcosystem=request.form['CanManageEcosystem'],HowToManageEcosystem=request.form['HowToManageEcosystem'],
        IsTrainingBeneficial=request.form['IsTrainingBeneficial'],FieldRoutines=request.form['FieldRoutines'],
        HarvestingChanges=request.form['HarvestingChanges'],IsCropCalendarBeneficial=request.form['IsCropCalendarBeneficial'],
        CropCalendarBenefits=request.form['CropCalendarBenefits'],RecordKeepingBenefits=request.form['RecordKeepingBenefits'])
        farmerpsychometrics = PsychometricsTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],FluidIntelligence=request.form['FluidIntelligence'],
        AttitudesandBeliefs=request.form['AttitudesandBeliefs'],AgribusinessSkills=request.form['AgribusinessSkills'],
        EthicsandHonesty=request.form['EthicsandHonesty'],SavesEnough=request.form['SavesEnough'],
        HasLazyNeighbors=request.form['HasLazyNeighbors'])
        farmermobiledata = MobileDataTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],MobilePhoneType=request.form['MobilePhoneType'],
        Avweeklyphoneuse=request.form['Avweeklyphoneuse'],Callsoutnumber=request.form['Callsoutnumber'],
        Callsoutminutes=request.form['Callsoutminutes'],Callsinnumber=request.form['Callsinnumber'],
        Callinminutes=request.form['Callinminutes'],SMSsent=request.form['SMSsent'],
        Dataprecedingplanswitch=request.form['Dataprecedingplanswitch'],Billpaymenthistory=request.form['Billpaymenthistory'],
        Avweeklydatarefill=request.form['Avweeklydatarefill'],NoOfmobileapps=request.form['NoOfmobileapps'],
        AvTimeSpentOnApp=request.form['AvTimeSpentOnApp'],MobileAppKinds=request.form['MobileAppKinds'],
        AppDeleteRate=request.form['AppDeleteRate'])
        # Add data only if Id does not exist in database already
        farmer = CreditHistoryTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercredithistory)
        farmer = ProductivityViabilityTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerproductivity)
        farmer = AgronomyServicesTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmeragronomy)
        farmer = PsychometricsTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerpsychometrics)
        farmer = MobileDataTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmermobiledata)
        db.session.commit()
        return {'message':'success'}


# 3.Collateral

class AddFarmlandData(Resource):	
    def post(self):
        farmer = FarmlandTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmerland = FarmlandTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],NoOfFarmlands=request.form['NoOfFarmlands'],
        OwnerOrCaretaker=request.form['OwnerOrCaretaker'],FarmOwnerName=request.form['FarmOwnerName'],
        FarmOwnerPhoneNo=request.form['FarmOwnerPhoneNo'],RelationshipWithOwner=request.form['RelationshipWithOwner'],
        InheritedFrom=request.form['InheritedFrom'],SizeOfFarm=request.form['SizeOfFarm'],
        FarmCoordinates=request.form['FarmCoordinates'],FarmAddress=request.form['FarmAddress'],
        KeepsAnimals=request.form['KeepsAnimals'],AnimalsFeedOn=request.form['AnimalsFeedOn'])
            db.session.add(farmerland)
            db.session.commit()
            return farmerland.json()

class AddCollateral5c(Resource):	
    def post(self):
        farmerland = FarmlandTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],NoOfFarmlands=request.form['NoOfFarmlands'],
        OwnerOrCaretaker=request.form['OwnerOrCaretaker'],FarmOwnerName=request.form['FarmOwnerName'],
        FarmOwnerPhoneNo=request.form['FarmOwnerPhoneNo'],RelationshipWithOwner=request.form['RelationshipWithOwner'],
        InheritedFrom=request.form['InheritedFrom'],SizeOfFarm=request.form['SizeOfFarm'],
        FarmCoordinates=request.form['FarmCoordinates'],FarmAddress=request.form['FarmAddress'],
        KeepsAnimals=request.form['KeepsAnimals'],AnimalsFeedOn=request.form['AnimalsFeedOn'])

        farmer = FarmlandTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerland)
            db.session.commit()
            return {'message':'success'}

#  4.Capacity

class AddCapacity(Resource):	
    def post(self):
        farmer = CapacityTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmercapacity = CapacityTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        HowLongBeenFarming=request.form['HowLongBeenFarming'],ParticipatedInTraining=request.form['ParticipatedInTraining'],
        FarmingPractice=request.form['FarmingPractice'],KeepsAnimals=request.form['KeepsAnimals'],
        HasCooperative=request.form['HasCooperative'],CooperativeName=request.form['CooperativeName'],
        EducationLevel=request.form['EducationLevel'])
            db.session.add(farmercapacity)
            db.session.commit()
            return farmercapacity.json()

class AddFarmPractice(Resource):	
    def post(self):
        farmer = FarmPractice.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmerpractice = FarmPractice(id=request.form['Bvn'],Bvn=request.form['Bvn'],SizeOfFarm=request.form['SizeOfFarm'],
        FarmIsRentedorLeased=request.form['FarmIsRentedorLeased'],NoOfYearsLeased=request.form['NoOfYearsLeased'],
        UsesMachines=request.form['UsesMachines'],RotatesCrops=request.form['RotatesCrops'],
        NoOfHectaresProducedYearly=request.form['NoOfHectaresProducedYearly'],ApproxFertilizerUse=request.form['ApproxFertilizerUse'],
        NoOfFertlizerApplications=request.form['NoOfFertlizerApplications'],DecisionForSpraying=request.form['DecisionForSpraying'],
        WeedControlPractice=request.form['WeedControlPractice'],EstimatedIncomePerCrop=request.form['EstimatedIncomePerCrop'],
        CropthatcanSellWell=request.form['CropthatcanSellWell'],HasFarmPlanOrProject=request.form['HasFarmPlanOrProject'],
        FarmProjectInfo=request.form['FarmProjectInfo'])
            db.session.add(farmerpractice)
            db.session.commit()
            return farmerpractice.json()

class AddMechanization(Resource):	
    def post(self):
        farmer = MechanizationTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmermechanization = MechanizationTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        MachinesUsed=request.form['MachinesUsed'],MachineHasHelped=request.form['MachineHasHelped'],
        AdviseMachineOrLabour=request.form['AdviseMachineOrLabour'],OtherMachinesNeeded=request.form['OtherMachinesNeeded'],
        CanAcquireMoreLands=request.form['CanAcquireMoreLands'],PercentCostSaved=request.form['PercentCostSaved'])
            db.session.add(farmermechanization)
            db.session.commit()
            return farmermechanization.json()

class AddCultivation(Resource):	
    def post(self):
        farmer = CultivationTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmercultivation = CultivationTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],type_of_labor=request.form['type_of_labor'],
        pay_for_labor=request.form['pay_for_labor'],how_many_housechildren_help=request.form['how_many_housechildren_help'],
        season_children_help=request.form['season_children_help'],labor_children_do=request.form['labor_children_do'],
        household_vs_hire_cost=request.form['household_vs_hire_cost'],labor_women_do=request.form['labor_women_do'],
        percent_female_hired=request.form['percent_female_hired'])
            db.session.add(farmercultivation)
            db.session.commit()
            return farmercultivation.json()

class AddHarvest(Resource):	
    def post(self):
        farmer = HarvestTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Record with Bvn already exists!"}
        else:
            farmerharvest = HarvestTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],when_is_harvest_season=request.form['when_is_harvest_season'],
        no_of_hired_workers=request.form['no_of_hired_workers'],no_of_family_workers=request.form['no_of_family_workers'],
        no_of_permanent_workers=request.form['no_of_permanent_workers'],no_hired_constantly=request.form['no_hired_constantly'])
            db.session.add(farmerharvest)
            db.session.commit()
            return farmerharvest.json()

class AddCapacity5c(Resource):	
    def post(self):
        farmercapacity = CapacityTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        HowLongBeenFarming=request.form['HowLongBeenFarming'],ParticipatedInTraining=request.form['ParticipatedInTraining'],
        FarmingPractice=request.form['FarmingPractice'],KeepsAnimals=request.form['KeepsAnimals'],
        HasCooperative=request.form['HasCooperative'],CooperativeName=request.form['CooperativeName'],
        EducationLevel=request.form['EducationLevel'])
        farmerpractice = FarmPractice(id=request.form['Bvn'],Bvn=request.form['Bvn'],SizeOfFarm=request.form['SizeOfFarm'],
        FarmIsRentedorLeased=request.form['FarmIsRentedorLeased'],NoOfYearsLeased=request.form['NoOfYearsLeased'],
        UsesMachines=request.form['UsesMachines'],RotatesCrops=request.form['RotatesCrops'],
        NoOfHectaresProducedYearly=request.form['NoOfHectaresProducedYearly'],ApproxFertilizerUse=request.form['ApproxFertilizerUse'],
        NoOfFertlizerApplications=request.form['NoOfFertlizerApplications'],DecisionForSpraying=request.form['DecisionForSpraying'],
        WeedControlPractice=request.form['WeedControlPractice'],EstimatedIncomePerCrop=request.form['EstimatedIncomePerCrop'],
        CropthatcanSellWell=request.form['CropthatcanSellWell'],HasFarmPlanOrProject=request.form['HasFarmPlanOrProject'],
        FarmProjectInfo=request.form['FarmProjectInfo'])
        farmermechanization = MechanizationTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        MachinesUsed=request.form['MachinesUsed'],MachineHasHelped=request.form['MachineHasHelped'],
        AdviseMachineOrLabour=request.form['AdviseMachineOrLabour'],OtherMachinesNeeded=request.form['OtherMachinesNeeded'],
        CanAcquireMoreLands=request.form['CanAcquireMoreLands'],PercentCostSaved=request.form['PercentCostSaved'])
        farmercultivation = CultivationTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],type_of_labor=request.form['type_of_labor'],
        pay_for_labor=request.form['pay_for_labor'],how_many_housechildren_help=request.form['how_many_housechildren_help'],
        season_children_help=request.form['season_children_help'],labor_children_do=request.form['labor_children_do'],
        household_vs_hire_cost=request.form['household_vs_hire_cost'],labor_women_do=request.form['labor_women_do'],
        percent_female_hired=request.form['percent_female_hired'])
        farmerharvest = HarvestTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],when_is_harvest_season=request.form['when_is_harvest_season'],
        no_of_hired_workers=request.form['no_of_hired_workers'],no_of_family_workers=request.form['no_of_family_workers'],
        no_of_permanent_workers=request.form['no_of_permanent_workers'],no_hired_constantly=request.form['no_hired_constantly'])

        farmer = CapacityTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercapacity)
        
        farmer = FarmPractice.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerpractice)
        
        farmer = MechanizationTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmermechanization)
        
        farmer = CultivationTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercultivation)
        
        farmer = HarvestTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmerharvest)
            db.session.commit()
            return {'message':'success'}



# 5.Condition
class AddConditions(Resource):	
    def post(self):
        farmercondition = ConditionsTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        duration=request.form['duration'],seller=request.form['seller'],seller_mou=request.form['seller_mou'])
        
        farmer = ConditionsTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercondition)
            db.session.commit()
            return farmercondition.json()

class AddConditions5c(Resource):	
    def post(self):
        farmercondition = ConditionsTable(id=request.form['Bvn'],Bvn=request.form['Bvn'],
        duration=request.form['duration'],seller=request.form['seller'],seller_mou=request.form['seller_mou'])
        
        farmer = ConditionsTable.query.filter_by(Bvn=request.form['Bvn']).first()
        if farmer:
            pass
        else:
            db.session.add(farmercondition)
            db.session.commit()
            return farmercondition.json()


class AddScoreAnalytics(Resource):	
    def post(self):
        new_data = ScoreAnalytics(Bvn=request.form['Bvn'],Scores=request.form['Scores'],
        Conditions=request.form['Conditions'],Capital=request.form['Capital'],Collateral=request.form['Collateral'],
        Capacity=request.form['Capacity'],Character=request.form['Character'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()



# Sustainability

class AddCareTable(Resource):	
    def post(self):
        new_data = CareTable(Bvn=request.form['Bvn'],HealthCentLoc=request.form['HealthCentLoc'],
        HealthCentCount=request.form['HealthCentCount'],HealthCentDistance=request.form['HealthCentDistance'],
        HealthCentFunctional=request.form['HealthCentFunctional'],Affordable=request.form['Affordable'],
        FarmDistance=request.form['FarmDistance'],InjuryEvent=request.form['InjuryEvent'],FirstAid=request.form['FirstAid'],
        LastCheck=request.form['LastCheck'],InSchool=request.form['InSchool'],Level=request.form['Level'],
        SchoolCount=request.form['SchoolCount'],SchoolFunctional=request.form['SchoolFunctional'],
        Qualification=request.form['Qualification'],StudyTime=request.form['StudyTime'],
        StudyWhere=request.form['StudyWhere'],AltIncomeSource=request.form['AltIncomeSource'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


class AddPlanet(Resource):	
    def post(self):
        new_data = Planet(Bvn=request.form['Bvn'],PlanToExpand=request.form['PlanToExpand'],Crop=request.form['Crop'],
        Variety=request.form['Variety'],RaiseOrBuy=request.form['RaiseOrBuy'],BuyWhere=request.form['BuyWhere'],
        SeedlingPrice=request.form['SeedlingPrice'],QtyBought=request.form['QtyBought'],DegradedLand=request.form['DegradedLand'],
        CropRotation=request.form['CropRotation'],Season=request.form['Season'],Disaster=request.form['Disaster'],
        Burning=request.form['Burning'],Mill=request.form['Mill'],EnergySource=request.form['EnergySource'],ReplacedTree=request.form['ReplacedTree'],
        Placement=request.form['Placement'],SourceOfWater=request.form['SourceOfWater'],CoverCrops=request.form['CoverCrops'],
        Intercrop=request.form['Intercrop'],CropIntercropped=request.form['CropIntercropped'],WasteMgt=request.form['WasteMgt'],
        WasteDisposal=request.form['WasteDisposal'],RecycleWaste=request.form['RecycleWaste'],Suffered=request.form['Suffered'],
        WhenSuffered=request.form['WhenSuffered'],GreyWater=request.form['GreyWater'],RecycleGreyWater=request.form['RecycleGreyWater'],
        Pollution=request.form['Pollution'],PollutionFreq=request.form['PollutionFreq'],Measures=request.form['Measures'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


class AddSafety(Resource):	
    def post(self):
        new_data = Safety(Bvn=request.form['Bvn'],Ferment=request.form['Ferment'],
        FermentDays=request.form['FermentDays'],FermentReason=request.form['FermentReason'],BrokenQty=request.form['BrokenQty'],
        DoWithBroken=request.form['DoWithBroken'],UnripeQty=request.form['UnripeQty'],DoWithUnripe=request.form['DoWithUnripe'],
        CocoaStore=request.form['CocoaStore'],FFBStore=request.form['FFBStore'],Herbicide=request.form['Herbicide'],
        HerbicideStore=request.form['HerbicideStore'],AgroChemSource=request.form['AgroChemSource'],HarvestTool=request.form['HarvestTool'],
        Wear=request.form['Wear'],Disposal=request.form['Disposal'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddLivingTable(Resource):	
    def post(self):
        new_data = LivingTable(Bvn=request.form['Bvn'],HouseOwned=request.form['HouseOwned'],
        StaysWithFamily=request.form['StaysWithFamily'],RelationshipWithOwner=request.form['RelationshipWithOwner'],
        HouseHoldEats=request.form['HouseHoldEats'],MaleUnderAge=request.form['MaleUnderAge'],
        FemaleUnderAge=request.form['FemaleUnderAge'],ChildrenUnderAge=request.form['ChildrenUnderAge'],
        MaleAboveAge=request.form['MaleAboveAge'],FemaleAboveAge=request.form['FemaleAboveAge'],
        ChildrenAboveAge=request.form['ChildrenAboveAge'],LivesWith=request.form['LivesWith'],OwnOtherLands=request.form['OwnOtherLands'],
        StandardofLiving=request.form['StandardofLiving'],SourceOfWater=request.form['SourceOfWater'],
        SourceEverytime=request.form['SourceEverytime'],CookingMethod=request.form['CookingMethod'],
        HaveElectricity=request.form['HaveElectricity'],PowerPayment=request.form['PowerPayment'],Typeoftoilet=request.form['Typeoftoilet'],
        KitchenSink=request.form['KitchenSink'],HasGroup=request.form['HasGroup'],Group=request.form['Group'],
        Position=request.form['Position'],HasAccessedInput=request.form['HasAccessedInput'],Input=request.form['Input'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

# Traceability

class AddCropInfo(Resource):	
    def post(self):
        new_data = CropInfo(tracing_id=request.form['tracing_id'],crop_type=request.form['crop_type'],sourcing_location=request.form['sourcing_location'],
        crop_origin=request.form['crop_origin'],crop_qty=request.form['crop_qty'],crop_variety=request.form['crop_variety'],
        cooperative=request.form['cooperative'],no_of_farmer_group=request.form['no_of_farmer_group'],
        female_to_male=request.form['female_to_male'],farmer_name=request.form['farmer_name'],gender=request.form['gender'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


class AddCropQuality(Resource):	
    def post(self):
        new_data = CropQuality(tracing_id=request.form['tracing_id'],moisture_content=request.form['moisture_content'],
        foreign_matter=request.form['foreign_matter'],test_weight=request.form['test_weight'],quality=request.form['quality'],
        rotten_shriveled=request.form['rotten_shriveled'],hardness=request.form['hardness'],splits=request.form['splits'],
        oil_content=request.form['oil_content'],infestation=request.form['infestation'],hectoliter=request.form['hectoliter'],
        total_defects=request.form['total_defects'],dockage=request.form['dockage'],ash_content=request.form['ash_content'],
        insoluble_ash=request.form['insoluble_ash'],volatile=request.form['volatile'],mold_weight=request.form['mold_weight'],
        drying_process=request.form['drying_process'],dead_insects=request.form['dead_insects'],excreta=request.form['excreta'],
        insect_defiled=request.form['insect_defiled'],curcumin=request.form['curcumin'],extraneous=request.form['extraneous'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


class AddInputsInfo(Resource):	
    def post(self):
        new_data = InputsInfo(tracing_id=request.form['tracing_id'],Fertilizers=request.form['Fertilizers'],Herbicides=request.form['Herbicides'],
        Fungicides=request.form['Fungicides'],Insecticides=request.form['Insecticides'],Seeds=request.form['Seeds'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()


class AddWarehouse(Resource):	
    def post(self):
        new_data = Warehouse(tracing_id=request.form['tracing_id'],location=request.form['location'],warehouse_type=request.form['warehouse_type'],
        capacity=request.form['capacity'],standard=request.form['standard'],insurance=request.form['insurance'],
        duration=request.form['duration'],cost=request.form['cost'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddShipment(Resource):	
    def post(self):
        new_data = Shipment(tracing_id=request.form['tracing_id'],location=request.form['location'],
        loading_date=request.form['loading_date'],no_of_people=request.form['no_of_people'],
        vehicle_type=request.form['vehicle_type'],plate_no=request.form['plate_no'],vehicle_capacity=request.form['vehicle_capacity'],
        driver_name=request.form['driver_name'],driver_number=request.form['driver_number'],insurance=request.form['insurance'],
        delivery_time=request.form['delivery_time'],delivery_date=request.form['delivery_date'],
        arrival_time=request.form['arrival_time'],no_of_police=request.form['no_of_police'],local_levy=request.form['local_levy'],
        state_levy=request.form['state_levy'],truck_levy=request.form['truck_levy'],
        inter_state_levy=request.form['inter_state_levy'],no_of_offloaders=request.form['no_of_offloaders'],
        quality_check=request.form['quality_check'],quality_checked=request.form['quality_checked'],
        quality_accepted=request.form['quality_accepted'],quality_rejected=request.form['quality_rejected'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddRecommendation(Resource):	
    def post(self):
        new_data = Recommendation(tracing_id=request.form['tracing_id'],rec_one=request.form['rec_one'],
        rec_two=request.form['rec_two'],rec_three=request.form['rec_three'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

# Credit Scoring
class AddScoreCard(Resource):	
    def post(self):
        card = ScoreCard(Bvn=request.form['Bvn'],age=request.form['age'],
        number_of_land=request.form['number_of_land'],address=request.form['address'],
        owner_caretaker=request.form['owner_caretaker'],crop=request.form['crop'],
        intercropping=request.form['intercropping'], machines=request.form['machines'],
        estimate_monthly_income=request.form['estimate_monthly_income'],
        years_cultivating=request.form['years_cultivating'],gender=request.form['gender'],
        owns_a_bank_account=request.form['owns_a_bank_account'],size_of_farm=request.form['size_of_farm'],
        number_of_crops=request.form['number_of_crops'],is_in_a_cooperative=request.form['is_in_a_cooperative'],
        no_of_agronomist_visits=request.form['no_of_agronomist_visits'])
        db.session.add(card)
        db.session.commit()
        return card.json()

class ScorecardBvn(Resource):
    def get(self, Bvn):
        farmer = ScoreCard.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = ScoreCard.query.filter_by(Bvn=Bvn).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'message':'success'}

class ScoreHistoryBvn(Resource):
    def get(self, Bvn):
        farmer = ScoreHistory.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = ScoreHistory.query.filter_by(Bvn=Bvn).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'message':'success'}

class ScoreFarmer(Resource):
    def post(self):
        Bvn=request.form['Bvn']
        applyLoanAmount=request.form['applyLoanAmount']
        #term_months=request.form['term_months']
        farmer = ScoreCard.query.filter_by(Bvn=Bvn).first()
        cols=['age', 'number_of_land', 'owner_caretaker', 'crop',
            'intercropping', 'machines', 'estimate_monthly_income','years_cultivating']
        if farmer:
            farmer=farmer.json()
            farmer = pd.DataFrame(farmer, index=[0])
            tdf = preprocess_df(farmer[cols])
            train_cols = ['number_of_land', 'owner_caretaker', 'intercropping', 'machines',
       'estimate_monthly_income', 'apply_loan_amount', 'years_cultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
            score = model.predict_proba(tdf[train_cols])[:,1]
            bin=bin_target(score)
            history = ScoreHistory(Bvn=farmer['Bvn'],age=farmer['age'],
        number_of_land=farmer['number_of_land'],address=farmer['address'],
        owner_caretaker=farmer['owner_caretaker'],crop=farmer['crop'],
        intercropping=request.form['intercropping'], machines=farmer['machines'],
        estimate_monthly_income=farmer['estimate_monthly_income'],
        years_cultivating=farmer['years_cultivating'],gender=farmer['gender'],
        owns_a_bank_account=farmer['owns_a_bank_account'],size_of_farm=farmer['size_of_farm'],
        number_of_crops=farmer['number_of_crops'],is_in_a_cooperative=farmer['is_in_a_cooperative'],
        no_of_agronomist_visits=farmer['no_of_agronomist_visits'],
        applyLoanAmount=request.form['applyLoanAmount'],
        term_months=request.form['term_months'],score=score, bin=bin)
            db.session.add(history)
            db.session.commit()
            return {'Bvn':Bvn, 'score':score, 'bin':bin }
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class ScoreFarmerDragAndDrop(Resource):
    def post(self):
        Bvn=request.form['Bvn']
        applyLoanAmount=request.form['applyLoanAmount']
        #term_months=request.form['term_months']
        features=request.form['features']
        features = list(features)
        farmer = ScoreCard.query.filter_by(Bvn=Bvn).first()
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
       'estimate_monthly_income', 'apply_loan_amount', 'years_cultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
            score = model.predict_proba(tdf[train_cols])[:,1]
            bin=bin_target(score)
            history = ScoreHistory(Bvn=farmer['Bvn'],age=farmer['age'],
        number_of_land=farmer['number_of_land'],address=farmer['address'],
        owner_caretaker=farmer['owner_caretaker'],crop=farmer['crop'],
        intercropping=request.form['intercropping'], machines=farmer['machines'],
        estimate_monthly_income=farmer['estimate_monthly_income'],
        years_cultivating=farmer['years_cultivating'],gender=farmer['gender'],
        owns_a_bank_account=farmer['owns_a_bank_account'],size_of_farm=farmer['size_of_farm'],
        number_of_crops=farmer['number_of_crops'],is_in_a_cooperative=farmer['is_in_a_cooperative'],
        no_of_agronomist_visits=farmer['no_of_agronomist_visits'],
        applyLoanAmount=request.form['applyLoanAmount'],
        term_months=request.form['term_months'],score=score, bin=bin)
            db.session.add(history)
            db.session.commit()
            return {'Bvn':Bvn, 'score':score, 'bin':bin }
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
# Loans

class AddLoan(Resource):	
    def post(self):
        new_data = Loan(
        loan_type=request.form['loan_type'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddLoanTransfer(Resource):	
    def post(self):
        new_data = LoanTransfer(loan_type=request.form['loan_type'],amount=request.form['amount'],
        status=request.form['status'],farmer_name=request.form['farmer_name'],Bvn=request.form['Bvn'],
        transfer_date=request.form['transfer_date'],due_date=request.form['due_date'])
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()



# -----------Traceability----------------------------------------------------------------------------------------

class CropInfoTracing(Resource):
    def get(self, tracing_id):
        farmer = CropInfo.query.filter_by(tracing_id=tracing_id).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
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
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
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
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
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
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
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
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, tracing_id):
        farmer = Recommendation.query.filter_by(tracing_id=tracing_id).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'message':'success'}

# ------------Get Requests-------------------------------------------------------------------------------------------------

class FarmerBvn(Resource):
    def get(self, Bvn):
        farmer = FarmerTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = FarmerTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            farmer = FarmerTable.query.filter_by(Bvn=Bvn).first()
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    

class AgronomyBvn(Resource):
    def get(self, Bvn):
        farmer = AgronomyServicesTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = AgronomyServicesTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    

class CapacityBvn(Resource):
    def get(self, Bvn):
        farmer = CapacityTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = CapacityTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class CapitalBvn(Resource):
    def get(self, Bvn):
        farmer = CapitalTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = CapitalTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class CareBvn(Resource):
    def get(self, Bvn):
        farmer = CareTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = CareTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class ConditionsBvn(Resource):
    def get(self, Bvn):
        farmer = ConditionsTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = ConditionsTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class CreditAccessBvn(Resource):
    def get(self, Bvn):
        farmer = CreditAccessTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = CreditAccessTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class Capital5cBvn(Resource):
    def get(self, Bvn):
        farmer1 = CapitalTable.query.filter_by(Bvn=Bvn).first()
        farmer2 = CreditAccessTable.query.filter_by(Bvn=Bvn).first()
        if not farmer1:
            farmer1='{"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"}'
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"}
        else:
            farmer2=farmer2.json()
        return {'capital':farmer1,'creditaccess':farmer2}
        '''
        if farmer1:
            if farmer2:
                return {'capital':farmer1.json(),'creditaccess':farmer2.json()}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
        '''
    def delete(self, Bvn):
        farmer1 = CapitalTable.query.filter_by(Bvn=Bvn).first()
        farmer2 = CreditAccessTable.query.filter_by(Bvn=Bvn).first()
        if farmer1:
            db.session.delete(farmer1)
            db.session.commit()
        if farmer2:
            db.session.delete(farmer2)
            db.session.commit()
        return {'message':'success'}
class CreditHistoryBvn(Resource):
    def get(self, Bvn):
        farmer = CreditHistoryTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = CreditHistoryTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    

class CultivationBvn(Resource):
    def get(self, Bvn):
        farmer = CultivationTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = CultivationTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class FarmlandBvn(Resource):
    def get(self, Bvn):
        farmer = FarmlandTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = FarmlandTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class HarvestBvn(Resource):
    def get(self, Bvn):
        farmer = HarvestTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = HarvestTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class LivingBvn(Resource):
    def get(self, Bvn):
        farmer = LivingTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = LivingTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class MechanizationBvn(Resource):
    def get(self, Bvn):
        farmer = MechanizationTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = MechanizationTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    

class MobileDataBvn(Resource):
    def get(self, Bvn):
        farmer = MobileDataTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = MobileDataTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    

class PlanetBvn(Resource):
    def get(self, Bvn):
        farmer = Planet.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = Planet.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class PracticeBvn(Resource):
    def get(self, Bvn):
        farmer = FarmPractice.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = FarmPractice.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    

class ProductivityBvn(Resource):
    def get(self, Bvn):
        farmer = ProductivityViabilityTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = ProductivityViabilityTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
    
class PsychometricsBvn(Resource):
    def get(self, Bvn):
        farmer = PsychometricsTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = PsychometricsTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
class SafetyBvn(Resource):
    def get(self, Bvn):
        farmer = Safety.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = Safety.query.filter_by(Bvn=Bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    

class TransferBvn(Resource):
    def get(self, Bvn):
        farmer = LoanTransfer.query.filter_by(Bvn=Bvn).all()
        if farmer:
            return [transfer.json() for transfer in farmer]
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    def delete(self, Bvn):
        farmer = LoanTransfer.query.filter_by(Bvn=Bvn).all()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {'message':'success'}
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"Bvn Not Found"},404
    
# All Loans, Farmers

class AllFarmers(Resource):
    def get(self):
        all_farmers = FarmerTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllAgronomy(Resource):
    def get(self):
        all_farmers = AgronomyServicesTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllCapacity(Resource):
    def get(self):
        all_farmers = CapacityTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllCapital(Resource):
    def get(self):
        all_farmers = CapitalTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllCare(Resource):
    def get(self):
        all_farmers = CareTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllConditions(Resource):
    def get(self):
        all_farmers = ConditionsTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllCreditAccess(Resource):
    def get(self):
        all_farmers = CreditAccessTable.query.all()
        return [farmer.json() for farmer in all_farmers]
class AllCapital5c(Resource):
    def get(self):
        all_farmer1 = CapitalTable.query.all()
        all_farmer1 = [farmer.json() for farmer in all_farmer1]
        all_farmer2 = CreditAccessTable.query.all()
        all_farmer2 = [farmer.json() for farmer in all_farmer2]
        return {'capital':all_farmer1,'creditaccess':all_farmer2}
class AllCreditHistory(Resource):
    def get(self):
        all_farmers = CreditHistoryTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllCropInfo(Resource):
    def get(self):
        all_farmers = CropInfo.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllCropQuality(Resource):
    def get(self):
        all_farmers = CropQuality.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllCultivation(Resource):
    def get(self):
        all_farmers = CultivationTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllFarmland(Resource):
    def get(self):
        all_farmers = FarmlandTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllHarvest(Resource):
    def get(self):
        all_farmers = HarvestTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllInputsInfo(Resource):
    def get(self):
        all_farmers = InputsInfo.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllLiving(Resource):
    def get(self):
        all_farmers = LivingTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllMechanization(Resource):
    def get(self):
        all_farmers = MechanizationTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllMobileData(Resource):
    def get(self):
        all_farmers = MobileDataTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllPlanet(Resource):
    def get(self):
        all_farmers = Planet.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllPractice(Resource):
    def get(self):
        all_farmers = FarmPractice.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllProductivity(Resource):
    def get(self):
        all_farmers = ProductivityViabilityTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllPsychometrics(Resource):
    def get(self):
        all_farmers = PsychometricsTable.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllRecommendation(Resource):
    def get(self):
        all_farmers = Recommendation.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllSafety(Resource):
    def get(self):
        all_farmers = Safety.query.all()
        return [farmer.json() for farmer in all_farmers]
class AllScorecard(Resource):
    def get(self):
        all_farmers = ScoreCard.query.all()
        return [farmer.json() for farmer in all_farmers]
class AllScoreHistory(Resource):
    def get(self):
        all_farmers = ScoreHistory.query.all()
        return [farmer.json() for farmer in all_farmers]


class AllShipment(Resource):
    def get(self):
        all_farmers = Shipment.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllTransfer(Resource):
    def get(self):
        all_farmers = LoanTransfer.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllWarehouse(Resource):
    def get(self):
        all_farmers = Warehouse.query.all()
        return [farmer.json() for farmer in all_farmers]

class AllLoans(Resource):
    def get(self):
        loans = db.session.query(Loan).all()
        return jsonify(loans=[loan.to_dict() for loan in loans])



# Bulk Files

class AddBulkFarmer(Resource):
    def post(self):
        #new_file = request.files['file']
        new_file = request.files.get("file")
        if new_file.ends_with('xls'|'xlsx'):
            df = pd.read_excel(new_file)
        elif new_file.ends_with('csv'):
            df = pd.read_csv(new_file)
        else:
            return {"error":True,"message":"Sorry your request can not be processed at the moment","data":"csv or excel file not found"}
            
        if df:
            for r in range(1,len(df)):
                dfr = df.iloc[r,:]
                farmerkyf = FarmerTable(id=dfr['Bvn'], FirstName=dfr['FirstName'], Surname = dfr['Surname'], Middlename=dfr['Middlename'],
        Telephone=dfr['Telephone'], Age=dfr['Age'], Gender=dfr['Gender'], Language = dfr['Language'], MaritalStatus=dfr['MaritalStatus'],
        Bankname = dfr['Bankname'], Accountno = dfr['Accountno'], Bvn=dfr['Bvn'], MeansofID=dfr['MeansofID'], Issuedate=dfr['Issuedate'],
        Expirydate=dfr['Expirydate'], Nin=dfr['Nin'], PermanentAddress=dfr['PermanentAddress'], Landmark=dfr['Landmark'],
        Stateoforigin=dfr['Stateoforigin'], IsinaGroup = dfr['IsinaGroup'], ReasonNoGroup = dfr['ReasonNoGroup'], Group=dfr['Group'],
        NumberofMembers = dfr['NumberofMembers'], FirstNameNok = dfr['FirstNameNok'], SurnameNok = dfr['SurnameNok'],
        MiddlenameNok = dfr['MiddlenameNok'], RelationshipNok = dfr['RelationshipNok'], OccupationNok = dfr['OccupationNok'],
        TelephoneNok  = dfr['TelephoneNok'], PermanentAddressNok = dfr['PermanentAddressNok'], LandmarkNok  = dfr['LandmarkNok'],
        NinNok  = dfr['NinNok'])
                db.session.add(farmerkyf)
            db.session.commit()
            return {'message':'Upload success'}


add = api.namespace('api/add',description='Add New Data')
add.add_resource(AddFarmer,'/farmer')
add.add_resource(AddScoreCard,'/scorecard')
add.add_resource(AddCapital,'/capital')
add.add_resource(AddCreditAccess,'/creditaccess')
add.add_resource(AddCreditHistory,'/credithistory')
add.add_resource(AddProductivityViability,'/productivity')
add.add_resource(AddCapacity,'/capacity')
add.add_resource(AddAgronomyServices,'/agronomy')
add.add_resource(AddConditions,'/conditions')
add.add_resource(AddCultivation,'/cultivation')
add.add_resource(AddFarmlandData,'/farmland')
add.add_resource(AddFarmPractice,'/practice')
add.add_resource(AddPsychometrics,'/psychometrics')
add.add_resource(AddMechanization,'/mechanization')
add.add_resource(AddMobileData,'/mobiledata')
add.add_resource(AddHarvest,'/harvest')
add.add_resource(AddLoan,'/loan')
add.add_resource(AddLoanTransfer,'/transfer')
add.add_resource(AddLivingTable,'/living')
add.add_resource(AddCareTable,'/care')
add.add_resource(AddCropInfo,'/crop_info')
add.add_resource(AddCropQuality,'/crop_quality')
add.add_resource(AddInputsInfo,'/inputs_info')
add.add_resource(AddPlanet,'/planet')
add.add_resource(AddRecommendation,'/recommendation')
add.add_resource(AddShipment,'/shipment')
add.add_resource(AddSafety,'/safety')
add.add_resource(AddWarehouse,'/warehouse')
add.add_resource(AddScoreAnalytics,'/score_analytics')
# 5c API Routes
add.add_resource(AddCapital5c,'/5c/capital')
add.add_resource(AddCapacity5c,'/5c/capacity')
add.add_resource(AddCharacter5c,'/5c/character')
add.add_resource(AddCollateral5c,'/5c/collateral')
add.add_resource(AddConditions5c,'/5c/conditions')


scorefarmer = api.namespace('api/score', description='credit scoring')
scorefarmer.add_resource(ScoreFarmer,'/')
scorefarmer.add_resource(ScoreFarmerDragAndDrop,'/filter')

farmer = api.namespace('api/farmer', description='know your farmer')
farmer.add_resource(FarmerBvn,'/Bvn=<Bvn>')
farmer.add_resource(AllFarmers,'/all')

care = api.namespace('api/care', description='access to healthcare and education')
care.add_resource(CareBvn,'/Bvn=<Bvn>')
care.add_resource(AllCare,'/all')

living = api.namespace('api/living', description='how farmer has been living')
living.add_resource(LivingBvn,'/Bvn=<Bvn>')
living.add_resource(AllLiving,'/all')

planet = api.namespace('api/planet', description='nature of crops and lands')
planet.add_resource(PlanetBvn,'/Bvn=<Bvn>')
planet.add_resource(AllPlanet,'/all')

safety = api.namespace('api/safety', description='food safety and quality')
safety.add_resource(SafetyBvn,'/Bvn=<Bvn>')
safety.add_resource(AllSafety,'/all')

capital = api.namespace('api/capital', description='farmer capital')
capital.add_resource(CapitalBvn,'/Bvn=<Bvn>')
capital.add_resource(AllCapital,'/all')

harvest = api.namespace('api/harvest', description='farmer harvest')
harvest.add_resource(HarvestBvn,'/Bvn=<Bvn>')
harvest.add_resource(AllHarvest,'/all')

agronomy = api.namespace('api/agronomy', description='farmer agronomy')
agronomy.add_resource(AgronomyBvn,'/Bvn=<Bvn>')
agronomy.add_resource(AllAgronomy,'/all')

capacity = api.namespace('api/capacity', description='farmer capacity')
capacity.add_resource(CapacityBvn,'/Bvn=<Bvn>')
capacity.add_resource(AllCapacity,'/all')

farmland = api.namespace('api/farmland', description='farmland')
farmland.add_resource(FarmlandBvn,'/Bvn=<Bvn>')
farmland.add_resource(AllFarmland,'/all')

transfer = api.namespace('api/transfer', description='loan transfers')
transfer.add_resource(TransferBvn,'/Bvn=<Bvn>')
transfer.add_resource(AllTransfer,'/all')

practice = api.namespace('api/practice', description='farm practice')
practice.add_resource(PracticeBvn,'/Bvn=<Bvn>')
practice.add_resource(AllPractice,'/all')

scorecard = api.namespace('api/scorecard', description='scorecard')
scorecard.add_resource(ScorecardBvn,'/Bvn=<Bvn>')
scorecard.add_resource(AllScorecard,'/all')

scorehistory = api.namespace('api/scorehistory', description='scorehistory')
scorehistory.add_resource(ScoreHistoryBvn,'/Bvn=<Bvn>')
scorehistory.add_resource(AllScoreHistory,'/all')

conditions = api.namespace('api/conditions', description='conditions')
conditions.add_resource(ConditionsBvn,'/Bvn=<Bvn>')
conditions.add_resource(AllConditions,'/all')

mobiledata = api.namespace('api/mobiledata', description='mobiledata')
mobiledata.add_resource(MobileDataBvn,'/Bvn=<Bvn>')
mobiledata.add_resource(AllMobileData,'/all')

cultivation = api.namespace('api/cultivation', description='cultivation')
cultivation.add_resource(CultivationBvn,'/Bvn=<Bvn>')
cultivation.add_resource(AllCultivation,'/all')

creditaccess = api.namespace('api/creditaccess', description='credit access')
creditaccess.add_resource(CreditAccessBvn,'/Bvn=<Bvn>')
creditaccess.add_resource(AllCreditAccess,'/all')

productivity = api.namespace('api/productivity', description='productivity viability')
productivity.add_resource(ProductivityBvn,'/Bvn=<Bvn>')
productivity.add_resource(AllProductivity,'/all')

credithistory = api.namespace('api/credithistory', description='credit history')
credithistory.add_resource(CreditHistoryBvn,'/Bvn=<Bvn>')
credithistory.add_resource(AllCreditHistory,'/all')

mechanization = api.namespace('api/mechanization', description='mechanization')
mechanization.add_resource(MechanizationBvn,'/Bvn=<Bvn>')
mechanization.add_resource(AllMechanization,'/all')

psychometrics = api.namespace('api/psychometrics', description='psychometrics')
psychometrics.add_resource(PsychometricsBvn,'/Bvn=<Bvn>')
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

loans = api.namespace('api/loans',description='load loans')
loans.add_resource(AllLoans,'/all')

bulk = api.namespace('api/bulk', description='bulk files')
bulk.add_resource(AddBulkFarmer,'/farmer')

capital5c = api.namespace('api/5c/capital', description='farmer 5c/capital')
capital5c.add_resource(Capital5cBvn,'/Bvn=<Bvn>')
capital5c.add_resource(AllCapital5c,'/all')

# Running app
if __name__ == '__main__':
    
    app.run(debug=True)
