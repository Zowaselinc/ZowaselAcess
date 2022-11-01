# Import flask 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api
from flask_mysqldb import MySQL

from models import app,FarmerTable, MovementTable, CapitalTable,CreditAccessTable
#from flasgger import Swagger
import os
from datetime import datetime
from flask_migrate import Migrate
db= SQLAlchemy()
api = Api(app, title='Zowasel')
Migrate(app,db)


# Add Farmer
class AddFarmer(Resource):
	def post(self,FirstName,Surname,Telephone,Email,Age,Gender,MaritalStatus,BVN,MeansofID,
	YearofIssue,ExpiryYear,NIN,PermanentAddress,Landmark,Stateoforigin,LGA,Group ):
		farmer = FarmerTable(id=BVN,FirstName=FirstName,Surname=Surname,Telephone=Telephone,Email=Email,Age=Age,Gender=Gender,
MaritalStatus=MaritalStatus,BVN=BVN,MeansofID=MeansofID,YearofIssue=YearofIssue,
ExpiryYear=ExpiryYear,NIN=NIN,PermanentAddress=PermanentAddress,Landmark=Landmark,Stateoforigin=Stateoforigin,
LGA=LGA,Group=Group)
		db.session.add(farmer)
		db.session.commit()
		return farmer.json()
class AddCapital(Resource):
	def post(self,BVN,MainIncomeSource,OtherIncomeSource,NoOfIncomeEarners, HasBankAccount,FirstFundingOption,NeedsALoan,
    PayBackMonths,HarvestQtyChanged,PestExpenseChanged):
		capital = CapitalTable(id=BVN,BVN=BVN,MainIncomeSource=MainIncomeSource,OtherIncomeSource=OtherIncomeSource,
		NoOfIncomeEarners=NoOfIncomeEarners,HasBankAccount=HasBankAccount,FirstFundingOption=FirstFundingOption,
		NeedsALoan=NeedsALoan,PayBackMonths=PayBackMonths,HarvestQtyChanged=HarvestQtyChanged,
		PestExpenseChanged=PestExpenseChanged)
		db.session.add(capital)
		db.session.commit()
		return capital.json()

class AddCreditAccess(Resource):
	def post(self,BVN,HasServedAsTreasurer,DurationAsTreasurer,SavesMoneyMonthly,SavingsAmount, HadDifficultyRepaying,DifficultLoanAmount,DifficultyReason,NoOfDifficultLoans,
    NoOfRepaidLoans,NoOfLoansOnTime,EstMonthlyIncome,CostOfCultivation,FarmProduceExchanged,NoOfTimesExchanged,
    Collateral,ApplyLoanAmount,YearsOfCultivating,AnnualTurnover):
		creditaccess = CreditAccessTable(id=BVN,BVN=BVN,HasServedAsTreasurer = HasServedAsTreasurer,DurationAsTreasurer = DurationAsTreasurer,
        SavesMoneyMonthly = SavesMoneyMonthly,SavingsAmount = SavingsAmount,HadDifficultyRepaying = HadDifficultyRepaying,
        DifficultLoanAmount = DifficultLoanAmount,DifficultyReason = DifficultyReason,NoOfDifficultLoans = NoOfDifficultLoans,
		NoOfRepaidLoans = NoOfRepaidLoans,NoOfLoansOnTime = NoOfLoansOnTime,EstMonthlyIncome = EstMonthlyIncome,
        CostOfCultivation = CostOfCultivation,FarmProduceExchanged = FarmProduceExchanged,NoOfTimesExchanged = NoOfTimesExchanged,
        Collateral = Collateral,ApplyLoanAmount = ApplyLoanAmount,YearsOfCultivating = YearsOfCultivating,AnnualTurnover = AnnualTurnover)
		db.session.add(creditaccess)
		db.session.commit()
		return creditaccess.json()
# BVN
class FarmerBVN(Resource):
	def get(self, BVN):
		farmer = FarmerTable.query.filter_by(BVN=BVN).first()
		if farmer:
			return farmer.json()
		else:
			return {'BVN':None},404
	def delete(self, BVN):
		farmer = FarmerTable.query.filter_by(BVN=BVN).first()
		db.session.delete(farmer)
		db.session.commit()
		return {'note':'delete success'}
# All Farmers
class AllFarmers(Resource):
	def get(self):
		all_farmers = FarmerTable.query.all()
		return [farmer.json() for farmer in all_farmers]


addfarmer = api.namespace('addfarmer',description='create new farmer')
addfarmer.add_resource(AddFarmer,'/<FirstName>&<Surname>&<int:Telephone>&<Email>&<int:Age>&<Gender>&<MaritalStatus>&<int:BVN>&<MeansofID>&<int:YearofIssue>&<int:ExpiryYear>&<int:NIN>&<PermanentAddress>&<Landmark>&<Stateoforigin>&<LGA>&<Group>')
addcapital = api.namespace('addcapital',description='farmer capital')
addcapital.add_resource(AddCapital,'/<int:BVN>&<MainIncomeSource>&<OtherIncomeSource>&<int:NoOfIncomeEarners>&<HasBankAccount>&<FirstFundingOption>&<NeedsALoan>&<int:PayBackMonths>&<HarvestQtyChanged>&<PestExpenseChanged>')
addcreditaccess = api.namespace('addcreditaccess',description='farmer addcredit_access')
addcreditaccess.add_resource(AddCreditAccess,'/<int:BVN>&<HasServedAsTreasurer>&<int:DurationAsTreasurer>&<SavesMoneyMonthly>&<int:SavingsAmount>&<HadDifficultyRepaying>&<int:DifficultLoanAmount>&<DifficultyReason>&<int:NoOfDifficultLoans>&<int:NoOfRepaidLoans>&<int:NoOfLoansOnTime>&<int:EstMonthlyIncome>&<int:CostOfCultivation>&<FarmProduceExchanged>&<int:NoOfTimesExchanged>&<Collateral>&<int:ApplyLoanAmount>&<int:YearsOfCultivating>&<int:AnnualTurnover>')

farmer = api.namespace('farmer', description='load farmer')
farmer.add_resource(FarmerBVN,'/BVN=<int:BVN>')
farmer.add_resource(AllFarmers,'/all')



# Running app
if __name__ == '__main__':
	
	app.run(debug=True)
