from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api
#from flask_migrate import Migrate
from datetime import datetime
from flask_mysqldb import MySQL
import pymysql
from sqlalchemy import create_engine, exc



import os



# Initializing flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zowasel:Zowaseladmin@1234!@mydb.touchofcloud.com.ng:59714/zowasel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()

class MovementTable(db.Model):
    __tablename__   = 'movement_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    product         = db.Column(db.String(200))
    qty             = db.Column(db.Integer)
    from_location   = db.Column(db.String(200))
    to_location     = db.Column(db.String(200))
    movement_time   = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self,id,product,qty,from_location,to_location,movement_time):
        self.id = id
        self.product = product
        self.qty = qty
        self.from_location = from_location
        self.to_location = to_location
        self.movement_time = movement_time
    def json(self):
        return {'id':self.id,'product':self.product,'qty':self.qty,
        'from_location':self.from_location,'to_location':self.to_location,'movement_time':self.movement_time}
    def __repr__(self):
        return '<MovementTable %r>' % self.id

class FarmerTable(db.Model):
    __tablename__   = 'farmer_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    FirstName     = db.Column(db.String(200))
    Surname     = db.Column(db.String(200))
    Telephone     = db.Column(db.Integer)
    Email = db.Column(db.String(200))
    Age     = db.Column(db.String(200))
    Gender     = db.Column(db.String(200))
    MaritalStatus     = db.Column(db.String(200))
    BVN     = db.Column(db.Integer)
    MeansofID     = db.Column(db.String(200))
    YearofIssue     = db.Column(db.String(200))
    ExpiryYear     = db.Column(db.String(200))
    NIN     = db.Column(db.String(200))
    PermanentAddress     = db.Column(db.String(200))
    Landmark     = db.Column(db.String(200))
    Stateoforigin     = db.Column(db.String(200))
    LGA     = db.Column(db.String(200))
    Group     = db.Column(db.String(200))

    def __init__(self,id,FirstName,Surname,Telephone,Email,Age,Gender,MaritalStatus,BVN,MeansofID,
	YearofIssue,ExpiryYear,NIN,PermanentAddress,Landmark,Stateoforigin,LGA,Group):
        self.id = id
        self.FirstName = FirstName
        self.Surname = Surname
        self.Telephone = Telephone
        self.Email = Email
        self.Age = Age
        self.Gender = Gender
        self.MaritalStatus = MaritalStatus
        self.BVN = BVN
        self.MeansofID = MeansofID
        self.YearofIssue = YearofIssue
        self.ExpiryYear = ExpiryYear
        self.NIN = NIN
        self.PermanentAddress = PermanentAddress
        self.Landmark = Landmark
        self.Stateoforigin = Stateoforigin
        self.LGA = LGA
        self.Group = Group
    def json(self):
        return {'id':self.id,'FirstName':self.FirstName,'Surname':self.Surname,'Telephone':self.Telephone,'Email':self.Email,
        'Age':self.Age,'Gender':self.Gender,'MaritalStatus':self.MaritalStatus,'BVN':self.BVN,'MeansofID':self.MeansofID,
        'YearofIssue':self.YearofIssue,'ExpiryYear':self.ExpiryYear,'NIN':self.NIN,'PermanentAddress':self.PermanentAddress,
        'Landmark':self.Landmark,'Stateoforigin':self.Stateoforigin,'LGA':self.LGA,'Group':self.Group}  
    def __repr__(self):
        return '<FarmerTable %r>' % self.id

class CapitalTable(db.Model):
    __tablename__   = 'capital_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    BVN     = db.Column(db.Integer)
    MainIncomeSource     = db.Column(db.String(200))
    OtherIncomeSource     = db.Column(db.String(200))
    NoOfIncomeEarners     = db.Column(db.Integer)
    HasBankAccount     = db.Column(db.String(200))
    FirstFundingOption     = db.Column(db.String(200))
    NeedsALoan     = db.Column(db.String(200))
    PayBackMonths     = db.Column(db.Integer)
    HarvestQtyChanged     = db.Column(db.String(200))
    PestExpenseChanged     = db.Column(db.String(200))

    def __init__(self,id,BVN,MainIncomeSource,OtherIncomeSource,NoOfIncomeEarners,HasBankAccount,FirstFundingOption,NeedsALoan,
    PayBackMonths,HarvestQtyChanged,PestExpenseChanged):
        self.id = id
        self.BVN = BVN
        self.MainIncomeSource = MainIncomeSource
        self.OtherIncomeSource = OtherIncomeSource
        self.NoOfIncomeEarners = NoOfIncomeEarners
        self.HasBankAccount = HasBankAccount
        self.FirstFundingOption = FirstFundingOption
        self.NeedsALoan = NeedsALoan
        self.PayBackMonths = PayBackMonths
        self.HarvestQtyChanged = HarvestQtyChanged
        self.PestExpenseChanged = PestExpenseChanged
    def json(self):
        return {'id':self.id,'BVN':self.BVN,
        'MainIncomeSource':self.MainIncomeSource,
        'OtherIncomeSource':self.OtherIncomeSource,
        'NoOfIncomeEarners':self.NoOfIncomeEarners,
        'HasBankAccount':self.HasBankAccount,
        'FirstFundingOption':self.FirstFundingOption,
        'NeedsALoan':self.NeedsALoan,
        'PayBackMonths':self.PayBackMonths,
        'HarvestQtyChanged':self.HarvestQtyChanged,
        'PestExpenseChanged':self.PestExpenseChanged}  
    def __repr__(self):
        return '<CapitalTable %r>' % self.id

class CreditAccessTable(db.Model):
    __tablename__   = 'credit_access_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    BVN     = db.Column(db.Integer)
    HasServedAsTreasurer     = db.Column(db.String(200))
    DurationAsTreasurer     = db.Column(db.Integer)
    SavesMoneyMonthly     = db.Column(db.String(200))
    SavingsAmount     = db.Column(db.Integer)
    HadDifficultyRepaying     = db.Column(db.String(200))
    DifficultLoanAmount     = db.Column(db.Integer)
    DifficultyReason     = db.Column(db.String(200))
    NoOfDifficultLoans     = db.Column(db.Integer)
    NoOfRepaidLoans     = db.Column(db.Integer)
    NoOfLoansOnTime     = db.Column(db.Integer)
    EstMonthlyIncome  = db.Column(db.Integer)
    CostOfCultivation     = db.Column(db.Integer)
    FarmProduceExchanged    = db.Column(db.String(200))
    NoOfTimesExchanged     = db.Column(db.Integer)
    Collateral    = db.Column(db.String(200))
    ApplyLoanAmount     = db.Column(db.Integer)
    YearsOfCultivating     = db.Column(db.Integer)
    AnnualTurnover     = db.Column(db.Integer)

    def __init__(self,id,BVN,HasServedAsTreasurer,DurationAsTreasurer,SavesMoneyMonthly,SavingsAmount, HadDifficultyRepaying,
    DifficultLoanAmount,DifficultyReason,NoOfDifficultLoans,NoOfRepaidLoans,NoOfLoansOnTime,EstMonthlyIncome,
    CostOfCultivation,FarmProduceExchanged,NoOfTimesExchanged,Collateral,ApplyLoanAmount,YearsOfCultivating,AnnualTurnover):
        self.id = id
        self.BVN = BVN
        self.HasServedAsTreasurer = HasServedAsTreasurer
        self.DurationAsTreasurer = DurationAsTreasurer
        self.SavesMoneyMonthly = SavesMoneyMonthly
        self.SavingsAmount = SavingsAmount
        self.HadDifficultyRepaying = HadDifficultyRepaying
        self.DifficultLoanAmount = DifficultLoanAmount
        self.DifficultyReason = DifficultyReason
        self.NoOfDifficultLoans = NoOfDifficultLoans
        self.NoOfRepaidLoans = NoOfRepaidLoans
        self.NoOfLoansOnTime = NoOfLoansOnTime
        self.EstMonthlyIncome = EstMonthlyIncome
        self.CostOfCultivation = CostOfCultivation
        self.FarmProduceExchanged = FarmProduceExchanged
        self.NoOfTimesExchanged = NoOfTimesExchanged
        self.Collateral = Collateral
        self.ApplyLoanAmount = ApplyLoanAmount
        self.YearsOfCultivating = YearsOfCultivating
        self.AnnualTurnover = AnnualTurnover
    def json(self):
        return {'id':self.id,'BVN':self.BVN,
        'HasServedAsTreasurer':self.HasServedAsTreasurer,
        'DurationAsTreasurer':self.DurationAsTreasurer,
        'SavesMoneyMonthly':self.SavesMoneyMonthly,
        'SavingsAmount':self.SavingsAmount,
        'HadDifficultyRepaying':self.HadDifficultyRepaying,
        'DifficultLoanAmount':self.DifficultLoanAmount,
        'DifficultyReason':self.DifficultyReason,
        'NoOfDifficultLoans':self.NoOfDifficultLoans,
        'NoOfRepaidLoans':self.NoOfRepaidLoans,
        'NoOfLoansOnTime':self.NoOfLoansOnTime,
        'EstMonthlyIncome':self.EstMonthlyIncome,
        'CostOfCultivation':self.CostOfCultivation,
        'FarmProduceExchanged':self.FarmProduceExchanged,
        'NoOfTimesExchanged':self.NoOfTimesExchanged,
        'Collateral':self.Collateral,
        'ApplyLoanAmount':self.ApplyLoanAmount,
        'YearsOfCultivating':self.YearsOfCultivating,
        'AnnualTurnover':self.AnnualTurnover
        }  
    def __repr__(self):
        return '<CreditAccessTable %r>' % self.id

db.init_app(app)
with app.app_context():
    db.create_all()
    #db.session.commit()