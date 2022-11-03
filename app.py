# Import flask 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api, fields
from flask_mysqldb import MySQL

from models import app,FarmerTable, MovementTable, CapitalTable,CreditAccessTable,CreditHistoryTable,ProductivityViabilityTable
#from flasgger import Swagger
import os
from datetime import datetime
from flask_migrate import Migrate
db= SQLAlchemy()
api = Api(app, title='Zowasel')
Migrate(app,db)


# Add Farmer
class AddFarmer(Resource):
    def post(self):
        FirstName=request.form['FirstName']
        Surname=request.form['Surname']
        Telephone=request.form['Telephone']
        Email=request.form['Email']
        Age=request.form['Age']
        Gender=request.form['Gender']
        MaritalStatus=request.form['MaritalStatus']
        Bvn=request.form['Bvn']
        MeansofID=request.form['MeansofID']
        YearofIssue=request.form['YearofIssue']
        ExpiryYear=request.form['ExpiryYear']
        Nin=request.form['Nin']
        PermanentAddress=request.form['PermanentAddress']
        Landmark=request.form['Landmark']
        Stateoforigin=request.form['Stateoforigin']
        Lga=request.form['Lga']
        Group=request.form['Group']
        farmer = FarmerTable(id=Bvn,FirstName=FirstName,Surname=Surname,Telephone=Telephone,Email=Email,Age=Age,Gender=Gender,
MaritalStatus=MaritalStatus,Bvn=Bvn,MeansofID=MeansofID,YearofIssue=YearofIssue,
ExpiryYear=ExpiryYear,Nin=Nin,PermanentAddress=PermanentAddress,Landmark=Landmark,Stateoforigin=Stateoforigin,
Lga=Lga,Group=Group)
        db.session.add(farmer)
        db.session.commit()
        return farmer.json()
class AddCapital(Resource):	
    def post(self):
        Bvn=request.form['Bvn']
        MainIncomeSource=request.form['MainIncomeSource']
        OtherIncomeSource=request.form['OtherIncomeSource']
        NoOfIncomeEarners=request.form['NoOfIncomeEarners']
        HasBankAccount=request.form['HasBankAccount']
        FirstFundingOption=request.form['FirstFundingOption']
        NeedsALoan=request.form['NeedsALoan']
        PayBackMonths=request.form['PayBackMonths']
        HarvestQtyChanged=request.form['HarvestQtyChanged']
        PestExpenseChanged=request.form['PestExpenseChanged']
        capital = CapitalTable(id=Bvn,Bvn=Bvn,MainIncomeSource=MainIncomeSource,OtherIncomeSource=OtherIncomeSource,
        NoOfIncomeEarners=NoOfIncomeEarners,HasBankAccount=HasBankAccount,FirstFundingOption=FirstFundingOption,
        NeedsALoan=NeedsALoan,PayBackMonths=PayBackMonths,HarvestQtyChanged=HarvestQtyChanged,
        PestExpenseChanged=PestExpenseChanged)
        db.session.add(capital)
        db.session.commit()
        #return capital.json()

class AddCreditAccess(Resource):
    def post(self):
        Bvn=request.form['Bvn']
        HasServedAsTreasurer=request.form['HasServedAsTreasurer']
        DurationAsTreasurer=request.form['DurationAsTreasurer']
        SavesMoneyMonthly=request.form['SavesMoneyMonthly']
        SavingsAmount=request.form['SavingsAmount']
        HadDifficultyRepaying=request.form['HadDifficultyRepaying']
        DifficultLoanAmount=request.form['DifficultLoanAmount']
        DifficultyReason=request.form['DifficultyReason']
        NoOfDifficultLoans=request.form['NoOfDifficultLoans']
        NoOfRepaidLoans=request.form['NoOfRepaidLoans']
        NoOfLoansOnTime=request.form['NoOfLoansOnTime']
        EstMonthlyIncome=request.form['EstMonthlyIncome']
        CostOfCultivation=request.form['CostOfCultivation']
        FarmProduceExchanged=request.form['FarmProduceExchanged']
        NoOfTimesExchanged=request.form['NoOfTimesExchanged']
        Collateral=request.form['Collateral']
        ApplyLoanAmount=request.form['ApplyLoanAmount']
        YearsOfCultivating=request.form['Collateral']
        AnnualTurnover=request.form['AnnualTurnover']
        creditaccess = CreditAccessTable(id=Bvn,Bvn=Bvn,HasServedAsTreasurer = HasServedAsTreasurer,DurationAsTreasurer = DurationAsTreasurer,
        SavesMoneyMonthly = SavesMoneyMonthly,SavingsAmount = SavingsAmount,HadDifficultyRepaying = HadDifficultyRepaying,
        DifficultLoanAmount = DifficultLoanAmount,DifficultyReason = DifficultyReason,NoOfDifficultLoans = NoOfDifficultLoans,
        NoOfRepaidLoans = NoOfRepaidLoans,NoOfLoansOnTime = NoOfLoansOnTime,EstMonthlyIncome = EstMonthlyIncome,
        CostOfCultivation = CostOfCultivation,FarmProduceExchanged = FarmProduceExchanged,NoOfTimesExchanged = NoOfTimesExchanged,
        Collateral = Collateral,ApplyLoanAmount = ApplyLoanAmount,YearsOfCultivating = YearsOfCultivating,AnnualTurnover = AnnualTurnover)
        db.session.add(creditaccess)
        db.session.commit()
        #return creditaccess.json()
class AddCreditHistory(Resource):
    def post(self):
        Bvn=request.form['Bvn']
        HasTakenLoanBefore=request.form['HasTakenLoanBefore']
        SourceOfLoan=request.form['SourceOfLoan']
        PastLoanAmount=request.form['PastLoanAmount']
        HowLoanWasRepaid=request.form['HowLoanWasRepaid']
        IsReadyToPayInterest=request.form['IsReadyToPayInterest']
        CanProvideCollateral=request.form['CanProvideCollateral']
        WhyNoCollateral=request.form['WhyNoCollateral']
        credithistory = CreditHistoryTable(id=Bvn,Bvn=Bvn,HasTakenLoanBefore=HasTakenLoanBefore,SourceOfLoan=SourceOfLoan,
        PastLoanAmount=PastLoanAmount,HowLoanWasRepaid=HowLoanWasRepaid,IsReadyToPayInterest=IsReadyToPayInterest,
        CanProvideCollateral=CanProvideCollateral,WhyNoCollateral=WhyNoCollateral)
        db.session.add(credithistory)
        db.session.commit()
        #return credithistory.json()

class AddProductivityViability(Resource):
    def post(self):
        Bvn=request.form['Bvn']
        CropsCultivated=request.form['CropsCultivated']
        GrowsCrops=request.form['GrowsCrops']
        OilPalmFertilizers=request.form['OilPalmFertilizers']
        CocoaFertilizers=request.form['CocoaFertilizers']
        FertilizerFrequency=request.form['FertilizerFrequency']
        PestFungHerbicides=request.form['PestFungHerbicides']
        StageChemicalApplied=request.form['StageChemicalApplied']
        NoOfOilDrums=request.form['NoOfOilDrums']
        NoOfBagsSesame=request.form['NoOfBagsSesame']
        NoOfBagsSoyaBeans=request.form['NoOfBagsSoyaBeans']
        NoOfBagsMaize=request.form['NoOfBagsMaize']
        NoOfBagsSorghum=request.form['NoOfBagsSorghum']
        NoOfBagsCocoaBeans=request.form['NoOfBagsCocoaBeans']
        CropTrainedOn=request.form['CropTrainedOn']
        WhereWhenWhoTrained=request.form['WhereWhenWhoTrained']
        NoOfTraining=request.form['NoOfTraining']
        PruningFrequency=request.form['PruningFrequency']
        CropBasedProblems=request.form['CropBasedProblems']
        TooYoungCrops=request.form['TooYoungCrops']
        YoungCropsAndStage=request.form['YoungCropsAndStage']
        CultivationStartdate=request.form['CultivationStartdate']
        IsIntensiveFarmingPractised=request.form['IsIntensiveFarmingPractised']
        EconomicActivities=request.form['EconomicActivities']
        Bvn=request.form['Bvn']
        productivityviability = ProductivityViabilityTable(id=Bvn,Bvn=Bvn,CropsCultivated=CropsCultivated,GrowsCrops=GrowsCrops,
        OilPalmFertilizers=OilPalmFertilizers,CocoaFertilizers=CocoaFertilizers,FertilizerFrequency=FertilizerFrequency,
        PestFungHerbicides=PestFungHerbicides,
    StageChemicalApplied=StageChemicalApplied,NoOfOilDrums=NoOfOilDrums,NoOfBagsSesame=NoOfBagsSesame,
    NoOfBagsSoyaBeans=NoOfBagsSoyaBeans,NoOfBagsMaize=NoOfBagsMaize,NoOfBagsSorghum=NoOfBagsSorghum,
    NoOfBagsCocoaBeans=NoOfBagsCocoaBeans,CropTrainedOn=CropTrainedOn,
    WhereWhenWhoTrain=WhereWhenWhoTrained,NoOfTraining=NoOfTraining,PruningFrequency=PruningFrequency,
    CropBasedProblems=CropBasedProblems,TooYoungCrops=TooYoungCrops,YoungCropsAndStage=YoungCropsAndStage,
    CultivationStartdate=CultivationStartdate,
    IsIntensiveFarmingPractised=IsIntensiveFarmingPractised,EconomicActivities=EconomicActivities)
        db.session.add(productivityviability)
        db.session.commit()
        #return productivityviability.json()
class FarmerBvn(Resource):
    def get(self, Bvn):
        farmer = FarmerTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {'Bvn':None},404
    def delete(self, Bvn):
        farmer = FarmerTable.query.filter_by(Bvn=Bvn).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'note':'delete success'}
# All Farmers
class AllFarmers(Resource):
    def get(self):
        all_farmers = FarmerTable.query.all()
        return [farmer.json() for farmer in all_farmers]
class AllBulkFarmer(Resource):
    def post(self):
        farmerslist = request.files.get("file")
        newfarmers = FarmerTable(newfarmers)
        db.session.add_all(newfarmers)
        db.session.commit()


add = api.namespace('add',description='Add New Farmer')
add.add_resource(AddFarmer,'/farmer')
add.add_resource(AddCapital,'/capital')
add.add_resource(AddCreditAccess,'/creditaccess')
add.add_resource(AddCreditHistory,'/credithistory')
add.add_resource(AddProductivityViability,'/productivity')

farmer = api.namespace('farmer', description='load farmer')
farmer.add_resource(FarmerBvn,'/Bvn=<int:Bvn>')
farmer.add_resource(AllFarmers,'/all')

bulk = api.namespace('bulk', description='bulk files')
bulk.add_resource(AllBulkFarmer,'/farmer')

# Running app
if __name__ == '__main__':
    
    app.run(debug=True)
