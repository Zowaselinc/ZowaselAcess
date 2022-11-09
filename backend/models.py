from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api, fields
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


class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False)
    phone_number = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    pack_size = db.Column(db.String(250), nullable=False)
    pack_price = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return '<Crop %r>' % self.id
        
class Product(db.Model):

    __tablename__ = 'products'
    product_id      = db.Column(db.String(200), primary_key=True)
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.product_id

class Location(db.Model):
    __tablename__   = 'locations'
    location_id     = db.Column(db.String(200), primary_key=True)
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Location %r>' % self.location_id


class Loan(db.Model):

    __tablename__ = 'loans'
    loan_id      = db.Column(db.String(200), primary_key=True)
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Loan %r>' % self.loan_id

class ScoreCard(db.Model):
    __tablename__   = 'score_card'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer, unique=True)
    age = db.Column(db.String(200))
    number_of_land = db.Column(db.String(200))
    address = db.Column(db.String(200))
    owner_caretaker = db.Column(db.String(200))
    crop = db.Column(db.String(200))
    intercropping = db.Column(db.String(200))
    machines = db.Column(db.String(200))
    estimate_monthly_income = db.Column(db.String(200))
    years_cultivating = db.Column(db.String(200))
    apply_loan_amount = db.Column(db.Integer)
    gender = db.Column(db.String(200))
    owns_a_bank_account = db.Column(db.String(200))
    size_of_farm = db.Column(db.String(200))
    grows_more_than_one_crop = db.Column(db.String(200))
    is_in_a_cooperative = db.Column(db.String(200))
    no_of_agronomist_visits = db.Column(db.Integer)
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,id,Bvn,age,number_of_land,address,owner_caretaker,crop,
    intercropping,machines,estimate_monthly_income,years_cultivating):
        self.id = id
        self.Bvn = Bvn
        self.age = age
        self.number_of_land = number_of_land
        self.address = address
        self.owner_caretaker = owner_caretaker
        self.crop = crop
        self.intercropping = intercropping
        self.machines = machines
        self.estimate_monthly_income = estimate_monthly_income
        self.years_cultivating = years_cultivating

    def __repr__(self):
        return '<ScoreCard %r>' % self.id


class LoanTransfer(db.Model):

    __tablename__   = 'loantransfers'
    transfer_id     = db.Column(db.Integer, primary_key=True)
    loan_name      = db.Column(db.String(200))
    amount             = db.Column(db.Integer)
    to_farmer     = db.Column(db.String(200))
    transfer_time   = db.Column(db.DateTime, default=datetime.utcnow)

    
    
    def __repr__(self):
        return '<LoanTransfer %r>' % self.transfer_id


class MovementTable(db.Model):
    __tablename__   = 'movement_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    product         = db.Column(db.String(200))
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
    Bvn     = db.Column(db.Integer)
    MeansofID     = db.Column(db.String(200))
    YearofIssue     = db.Column(db.String(200))
    ExpiryYear     = db.Column(db.String(200))
    Nin     = db.Column(db.String(200))
    PermanentAddress     = db.Column(db.String(200))
    Landmark     = db.Column(db.String(200))
    Stateoforigin     = db.Column(db.String(200))
    Lga     = db.Column(db.String(200))
    Group     = db.Column(db.String(200))

    def __init__(self,id,FirstName,Surname,Telephone,Email,Age,Gender,MaritalStatus,Bvn,MeansofID,
	YearofIssue,ExpiryYear,Nin,PermanentAddress,Landmark,Stateoforigin,Lga,Group):
        self.id = id
        self.FirstName = FirstName
        self.Surname = Surname
        self.Telephone = Telephone
        self.Email = Email
        self.Age = Age
        self.Gender = Gender
        self.MaritalStatus = MaritalStatus
        self.Bvn = Bvn
        self.MeansofID = MeansofID
        self.YearofIssue = YearofIssue
        self.ExpiryYear = ExpiryYear
        self.Nin = Nin
        self.PermanentAddress = PermanentAddress
        self.Landmark = Landmark
        self.Stateoforigin = Stateoforigin
        self.Lga = Lga
        self.Group = Group
    def json(self):
        return {'id':self.id,'FirstName':self.FirstName,'Surname':self.Surname,'Telephone':self.Telephone,'Email':self.Email,
        'Age':self.Age,'Gender':self.Gender,'MaritalStatus':self.MaritalStatus,'Bvn':self.Bvn,'MeansofID':self.MeansofID,
        'YearofIssue':self.YearofIssue,'ExpiryYear':self.ExpiryYear,'Nin':self.Nin,'PermanentAddress':self.PermanentAddress,
        'Landmark':self.Landmark,'Stateoforigin':self.Stateoforigin,'Lga':self.Lga,'Group':self.Group}  
    def __repr__(self):
        return '<FarmerTable %r>' % self.id

class CapitalTable(db.Model):
    __tablename__   = 'capital_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    MainIncomeSource     = db.Column(db.String(200))
    OtherIncomeSource     = db.Column(db.String(200))
    NoOfIncomeEarners     = db.Column(db.Integer)
    HasBankAccount     = db.Column(db.String(200))
    FirstFundingOption     = db.Column(db.String(200))
    NeedsALoan     = db.Column(db.String(200))
    PayBackMonths     = db.Column(db.Integer)
    HarvestQtyChanged     = db.Column(db.String(200))
    PestExpenseChanged     = db.Column(db.String(200))

    def __init__(self,id,Bvn,MainIncomeSource,OtherIncomeSource,NoOfIncomeEarners,HasBankAccount,FirstFundingOption,NeedsALoan,
    PayBackMonths,HarvestQtyChanged,PestExpenseChanged):
        self.id = id
        self.Bvn = Bvn
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
        return {'id':self.id,'Bvn':self.Bvn, 'MainIncomeSource':self.MainIncomeSource,
        'OtherIncomeSource':self.OtherIncomeSource,'NoOfIncomeEarners':self.NoOfIncomeEarners,
        'HasBankAccount':self.HasBankAccount,'FirstFundingOption':self.FirstFundingOption,
        'NeedsALoan':self.NeedsALoan,'PayBackMonths':self.PayBackMonths,
        'HarvestQtyChanged':self.HarvestQtyChanged,'PestExpenseChanged':self.PestExpenseChanged}  
    def __repr__(self):
        return '<CapitalTable %r>' % self.id

class CreditAccessTable(db.Model):
    __tablename__   = 'credit_access_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
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

    def __init__(self,id,Bvn,HasServedAsTreasurer,DurationAsTreasurer,SavesMoneyMonthly,SavingsAmount, HadDifficultyRepaying,
    DifficultLoanAmount,DifficultyReason,NoOfDifficultLoans,NoOfRepaidLoans,NoOfLoansOnTime,EstMonthlyIncome,
    CostOfCultivation,FarmProduceExchanged,NoOfTimesExchanged,Collateral,ApplyLoanAmount,YearsOfCultivating,AnnualTurnover):
        self.id = id
        self.Bvn = Bvn
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
        return {'id':self.id,'Bvn':self.Bvn,'HasServedAsTreasurer':self.HasServedAsTreasurer,
        'DurationAsTreasurer':self.DurationAsTreasurer,'SavesMoneyMonthly':self.SavesMoneyMonthly,
        'SavingsAmount':self.SavingsAmount,'HadDifficultyRepaying':self.HadDifficultyRepaying,
        'DifficultLoanAmount':self.DifficultLoanAmount,'DifficultyReason':self.DifficultyReason,
        'NoOfDifficultLoans':self.NoOfDifficultLoans,'NoOfRepaidLoans':self.NoOfRepaidLoans,
        'NoOfLoansOnTime':self.NoOfLoansOnTime,'EstMonthlyIncome':self.EstMonthlyIncome,
        'CostOfCultivation':self.CostOfCultivation, 'FarmProduceExchanged':self.FarmProduceExchanged,
        'NoOfTimesExchanged':self.NoOfTimesExchanged, 'Collateral':self.Collateral,
        'ApplyLoanAmount':self.ApplyLoanAmount, 'YearsOfCultivating':self.YearsOfCultivating,
        'AnnualTurnover':self.AnnualTurnover}  
    def __repr__(self):
        return '<CreditAccessTable %r>' % self.id
class CreditHistoryTable(db.Model):
    __tablename__   = 'credit_history_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    HasTakenLoanBefore     = db.Column(db.String(200))
    SourceOfLoan     = db.Column(db.String(200))
    PastLoanAmount     = db.Column(db.Integer)
    HowLoanWasRepaid     = db.Column(db.Integer)
    IsReadyToPayInterest     = db.Column(db.String(200))
    CanProvideCollateral     = db.Column(db.String(200))
    WhyNoCollateral = db.Column(db.String(200))
    def __init__(self,id,Bvn,HasTakenLoanBefore,SourceOfLoan,PastLoanAmount,HowLoanWasRepaid,IsReadyToPayInterest,
    CanProvideCollateral,WhyNoCollateral):
        self.id = id
        self.Bvn = Bvn
        self.HasTakenLoanBefore = HasTakenLoanBefore
        self.SourceOfLoan = SourceOfLoan
        self.PastLoanAmount = PastLoanAmount
        self.HowLoanWasRepaid = HowLoanWasRepaid
        self.IsReadyToPayInterest = IsReadyToPayInterest
        self.CanProvideCollateral = CanProvideCollateral
        self.WhyNoCollateral = WhyNoCollateral
    def json(self):
        return {'id':self.id,'Bvn':self.Bvn,'HasTakenLoanBefore':self.HasTakenLoanBefore,'SourceOfLoan':self.SourceOfLoan,'PastLoanAmount':self.PastLoanAmount,
        'HowLoanWasRepaid':self.HowLoanWasRepaid,'IsReadyToPayInterest':self.IsReadyToPayInterest,'CanProvideCollateral':self.CanProvideCollateral,'WhyNoCollateral':self.WhyNoCollateral}  
    def __repr__(self):
        return '<CreditHistoryTable %r>' % self.id

class ProductivityViabilityTable(db.Model):
    __tablename__   = 'productivity_viability_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    CropsCultivated     = db.Column(db.String(200))
    GrowsCrops     = db.Column(db.String(200))
    OilPalmFertilizers     = db.Column(db.String(200))
    CocoaFertilizers     = db.Column(db.String(200))
    FertilizerFrequency     = db.Column(db.String(200))
    PestFungHerbicides     = db.Column(db.String(200))
    StageChemicalApplied     = db.Column(db.String(200))
    NoOfOilDrums     = db.Column(db.Integer)
    NoOfBagsSesame     = db.Column(db.Integer)
    NoOfBagsSoyaBeans     = db.Column(db.Integer)
    NoOfBagsMaize     = db.Column(db.Integer)
    NoOfBagsSorghum    = db.Column(db.Integer)
    NoOfBagsCocoaBeans     = db.Column(db.Integer)
    CropTrainedOn     = db.Column(db.String(200))
    WhereWhenWhoTrained     = db.Column(db.String(200))
    NoOfTraining     = db.Column(db.Integer)
    PruningFrequency     = db.Column(db.String(200))
    CropBasedProblems     = db.Column(db.String(200))
    TooYoungCrops     = db.Column(db.String(200))
    YoungCropsAndStage     = db.Column(db.String(200))
    CultivationStartdate     = db.Column(db.String(200))
    IsIntensiveFarmingPractised     = db.Column(db.String(200))
    EconomicActivities     = db.Column(db.String(200))
    
    
    def __init__(self,id,Bvn,CropsCultivated,GrowsCrops,OilPalmFertilizers,CocoaFertilizers,FertilizerFrequency,PestFungHerbicides,
    StageChemicalApplied,NoOfOilDrums,NoOfBagsSesame,NoOfBagsSoyaBeans,NoOfBagsMaize,NoOfBagsSorghum,NoOfBagsCocoaBeans,CropTrainedOn,
    WhereWhenWhoTrained,NoOfTraining,PruningFrequency,CropBasedProblems,TooYoungCrops,YoungCropsAndStage,CultivationStartdate,
    IsIntensiveFarmingPractised,EconomicActivities):
        self.id = id
        self.Bvn = Bvn
        self.CropsCultivated = CropsCultivated
        self.GrowsCrops = GrowsCrops
        self.OilPalmFertilizers = OilPalmFertilizers
        self.CocoaFertilizers = CocoaFertilizers
        self.FertilizerFrequency = FertilizerFrequency
        self.PestFungHerbicides = PestFungHerbicides
        self.StageChemicalApplied = StageChemicalApplied
        self.NoOfOilDrums = NoOfOilDrums
        self.NoOfBagsSesame = NoOfBagsSesame
        self.NoOfBagsSoyaBeans = NoOfBagsSoyaBeans
        self.NoOfBagsMaize = NoOfBagsMaize
        self.NoOfBagsSorghum = NoOfBagsSorghum
        self.NoOfBagsCocoaBeans = NoOfBagsCocoaBeans
        self.CropTrainedOn = CropTrainedOn
        self.WhereWhenWhoTrained = WhereWhenWhoTrained
        self.NoOfTraining = NoOfTraining
        self.PruningFrequency = PruningFrequency
        self.CropBasedProblems = CropBasedProblems
        self.TooYoungCrops = TooYoungCrops
        self.YoungCropsAndStage = YoungCropsAndStage
        self.CultivationStartdate = CultivationStartdate
        self.IsIntensiveFarmingPractised = IsIntensiveFarmingPractised
        self.EconomicActivities = EconomicActivities
    def json(self):
        return {'id':self.id,'Bvn':self.Bvn,'CropsCultivated':self.CropsCultivated,'GrowsCrops':self.GrowsCrops,'OilPalmFertilizers':self.OilPalmFertilizers,
        'CocoaFertilizers':self.CocoaFertilizers,'FertilizerFrequency':self.FertilizerFrequency,'PestFungHerbicides':self.PestFungHerbicides,
        'StageChemicalApplied':self.StageChemicalApplied,'NoOfOilDrums':self.NoOfOilDrums,'NoOfBagsSesame':self.NoOfBagsSesame,'NoOfBagsSoyaBeans':self.NoOfBagsSoyaBeans,
        'NoOfBagsMaize':self.NoOfBagsMaize,'NoOfBagsSorghum':self.NoOfBagsSorghum,'NoOfBagsCocoaBeans':self.NoOfBagsCocoaBeans,'CropTrainedOn':self.CropTrainedOn,
        'WhereWhenWhoTrained':self.WhereWhenWhoTrained,'NoOfTraining':self.NoOfTraining,'PruningFrequency':self.PruningFrequency,'CropBasedProblems':self.CropBasedProblems,
        'TooYoungCrops':self.TooYoungCrops,'YoungCropsAndStage':self.YoungCropsAndStage,'CultivationStartdate':self.CultivationStartdate,'IsIntensiveFarmingPractised':self.IsIntensiveFarmingPractised,
        'EconomicActivities':self.EconomicActivities}  
    def __repr__(self):
        return '<ProductivityViabilityTable %r>' % self.id

class AgronomyServicesTable(db.Model):
    __tablename__   = 'agronomy_services_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    KnowsAgriProcessed     = db.Column(db.String(200))
    AgronomistThatTrainedYou     = db.Column(db.String(200))
    CanManageEcosystem    = db.Column(db.String(200))
    HowToManageEcosystem     = db.Column(db.String(200))
    IsTrainingBeneficial     = db.Column(db.String(200))
    FieldRoutines     = db.Column(db.String(200))
    HarvestingChanges     = db.Column(db.String(200))
    IsCropCalendarBeneficial     = db.Column(db.String(200))
    CropCalendarBenefits     = db.Column(db.String(200))
    RecordKeepingBenefits     = db.Column(db.String(200))
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<AgronomyServicesTable %r>' % self.id

class PsychometricsTable(db.Model):
    __tablename__   = 'psychometrics_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    FluidIntelligence     = db.Column(db.String(200))
    AttitudesandBeliefs     = db.Column(db.String(200))
    AgribusinessSkills     = db.Column(db.String(200))
    EthicsandHonesty     = db.Column(db.String(200))
    SavesEnough     = db.Column(db.String(200))
    HasLazyNeighbors     = db.Column(db.String(200))
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<PsychometricsTable %r>' % self.id
class MobileDataTable(db.Model):
    __tablename__   = 'mobile_data_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    MobilePhoneType     = db.Column(db.String(200))
    Avweeklyphoneuse     = db.Column(db.Integer)
    Callsoutnumber     = db.Column(db.Integer)
    Callsoutminutes     = db.Column(db.Integer)
    Callsinnumber     = db.Column(db.Integer)
    Callinminutes     = db.Column(db.Integer)
    SMSsent     = db.Column(db.Integer)
    Dataprecedingplanswitch     = db.Column(db.Integer)
    Billpaymenthistory     = db.Column(db.Integer)
    Avweeklydatarefill     = db.Column(db.Integer)
    NoOfmobileapps     = db.Column(db.Integer)
    AvTimeSpentOnApp     = db.Column(db.Integer)
    MobileAppKinds     = db.Column(db.String(200))
    AppDeleteRate     = db.Column(db.String(200))
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<MobileDataTable %r>' % self.id
class FarmlandTable(db.Model):
    __tablename__   = 'farmland_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    NoOfFarmlands     = db.Column(db.Integer)
    OwnerOrCaretaker     = db.Column(db.String(200))
    FarmOwnerName     = db.Column(db.String(200))
    FarmOwnerPhoneNo     = db.Column(db.Integer)
    RelationshipWithOwner     = db.Column(db.String(200))
    InheritedFrom     = db.Column(db.String(200))
    SizeOfFarm     = db.Column(db.String(200))
    FarmCoordinates     = db.Column(db.String(200))
    FarmAddress     = db.Column(db.String(200))
    KeepsAnimals     = db.Column(db.String(200))
    AnimalsFeedOn     = db.Column(db.String(200))
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<FarmlandTable %r>' % self.id
class CapacityTable(db.Model):
    __tablename__   = 'capacity_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    HowLongBeenFarming     = db.Column(db.Integer)
    ParticipatedInTraining     = db.Column(db.String(200))
    FarmingPractice     = db.Column(db.String(200))
    KeepsAnimals     = db.Column(db.String(200))
    HasCooperative     = db.Column(db.String(200))
    CooperativeName     = db.Column(db.String(200))
    EducationLevel     = db.Column(db.String(200))
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CapacityTable %r>' % self.id

class FarmPractice(db.Model):
    __tablename__   = 'farm_practice_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    SizeOfFarm     = db.Column(db.Integer)
    FarmIsRentedorLeased     = db.Column(db.String(200))
    NoOfYearsLeased     = db.Column(db.Integer)
    UsesMachines     = db.Column(db.String(200))
    RotatesCrops     = db.Column(db.String(200))
    NoOfHectaresProducedYearly     = db.Column(db.Integer)
    ApproxFertilizerUse     = db.Column(db.String(200))
    NoOfFertlizerApplications     = db.Column(db.String(200))
    DecisionForSpraying     = db.Column(db.String(200))
    WeedControlPractice     = db.Column(db.String(200))
    EstimatedIncomePerCrop     = db.Column(db.String(200))
    CropthatcanSellWell     = db.Column(db.String(200))
    HasFarmPlanOrProject     = db.Column(db.String(200))
    FarmProjectInfo     = db.Column(db.String(200))
    
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<FarmPractice %r>' % self.id
class MechanizationTable(db.Model):
    __tablename__   = 'mechanization_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    MachinesUsed     = db.Column(db.String(200))
    MachineHasHelped     = db.Column(db.String(200))
    AdviseMachineOrLabour     = db.Column(db.String(200))
    OtherMachinesNeeded     = db.Column(db.String(200))
    CanAcquireMoreLands     = db.Column(db.String(200))
    PercentCostSaved     = db.Column(db.Integer) 
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<MechanizationTable %r>' % self.id
class CultivationTable(db.Model):
    __tablename__   = 'cultivation_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    type_of_labor     = db.Column(db.String(200))
    pay_for_labor     = db.Column(db.Integer)
    how_many_housechildren_help     = db.Column(db.String(200))
    season_children_help     = db.Column(db.String(200))
    labor_children_do     = db.Column(db.String(200))
    household_vs_hire_cost     = db.Column(db.Integer)
    labor_women_do     = db.Column(db.String(200))
    percent_female_hired     = db.Column(db.Integer) 
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CultivationTable %r>' % self.id
class HarvestTable(db.Model):
    __tablename__   = 'harvest_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    when_is_harvest_season     = db.Column(db.String(200))
    no_of_hired_workers     = db.Column(db.Integer)
    no_of_family_workers     = db.Column(db.Integer)
    no_of_permanent_workers    = db.Column(db.Integer)
    no_hired_constantly     = db.Column(db.Integer)
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<HarvestTable %r>' % self.id
class ConditionsTable(db.Model):
    __tablename__   = 'conditions_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.Integer)
    LengthOfHarvestChanged     = db.Column(db.String(200))
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<ConditionsTable %r>' % self.id
db.init_app(app)
with app.app_context():
    db.create_all()



