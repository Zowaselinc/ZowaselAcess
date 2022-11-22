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
db = SQLAlchemy(app)


# Create Tables 

class Loan(db.Model):
    __tablename__ = 'loans'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    loan_type      = db.Column(db.String(200), unique=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    def __repr__(self):
        return '<Loan %r>' % self.loan_type

class ScoreCard(db.Model):
    __tablename__   = 'score_card'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    age = db.Column(db.String(200))
    number_of_land = db.Column(db.String(200))
    address = db.Column(db.String(200))
    owner_caretaker = db.Column(db.String(200))
    crop = db.Column(db.String(200))
    intercropping = db.Column(db.String(200))
    machines = db.Column(db.String(200))
    estimate_monthly_income = db.Column(db.String(200))
    years_cultivating = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    owns_a_bank_account = db.Column(db.String(200))
    size_of_farm = db.Column(db.String(200))
    number_of_crops = db.Column(db.String(200))
    is_in_a_cooperative = db.Column(db.String(200))
    no_of_agronomist_visits = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

class ScoreHistory(db.Model):
    __tablename__   = 'score_history'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    age = db.Column(db.String(200))
    number_of_land = db.Column(db.String(200))
    address = db.Column(db.String(200))
    owner_caretaker = db.Column(db.String(200))
    crop = db.Column(db.String(200))
    intercropping = db.Column(db.String(200))
    machines = db.Column(db.String(200))
    estimate_monthly_income = db.Column(db.String(200))
    years_cultivating = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    owns_a_bank_account = db.Column(db.String(200))
    size_of_farm = db.Column(db.String(200))
    number_of_crops = db.Column(db.String(200))
    is_in_a_cooperative = db.Column(db.String(200))
    no_of_agronomist_visits = db.Column(db.String(200))
    applyLoanAmount     = db.Column(db.String(200))
    term_months     = db.Column(db.String(200))
    score     = db.Column(db.String(200))
    bin     = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<ScoreCard %r>' % self.id


class LoanTransfer(db.Model):

    __tablename__   = 'loantransfers'
    id     = db.Column(db.String(200), primary_key=True)
    loan_type      = db.Column(db.String(200))
    amount             = db.Column(db.String(200))
    status      = db.Column(db.String(200))
    farmer_name     = db.Column(db.String(200))
    Bvn     = db.Column(db.String(200))
    transfer_date   = db.Column(db.String(200))
    due_date   = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<LoanTransfer %r>' % self.id


class FarmerTable(db.Model):
    __tablename__   = 'farmer_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    FirstName     = db.Column(db.String(200))
    Surname     = db.Column(db.String(200))
    Middlename     = db.Column(db.String(200))
    Telephone     = db.Column(db.String(200))
    Age     = db.Column(db.String(200))
    Gender     = db.Column(db.String(200))
    Language = db.Column(db.String(200))
    MaritalStatus     = db.Column(db.String(200))
    Bankname = db.Column(db.String(200))
    Accountno     = db.Column(db.String(200))
    Bvn     = db.Column(db.String(200))
    MeansofID     = db.Column(db.String(200))
    Issuedate     = db.Column(db.String(200))
    Expirydate     = db.Column(db.String(200))
    Nin     = db.Column(db.String(200))
    PermanentAddress     = db.Column(db.String(200))
    Landmark     = db.Column(db.String(200))
    Stateoforigin     = db.Column(db.String(200))
    IsinaGroup     = db.Column(db.String(200))
    ReasonNoGroup     = db.Column(db.String(200))
    Group     = db.Column(db.String(200))
    NumberofMembers     = db.Column(db.String(200))
    FirstNameNok     = db.Column(db.String(200))
    SurnameNok     = db.Column(db.String(200))
    MiddlenameNok     = db.Column(db.String(200))
    RelationshipNok     = db.Column(db.String(200))
    OccupationNok     = db.Column(db.String(200))
    TelephoneNok     = db.Column(db.String(200))
    PermanentAddressNok     = db.Column(db.String(200))
    LandmarkNok     = db.Column(db.String(200))
    NinNok     = db.Column(db.String(200))

    def json(self):
        return {column.name: str(getattr(self, column.name)) for column in self.__table__.columns}  
    def __repr__(self):
        return '<FarmerTable %r>' % self.id



class CapitalTable(db.Model):
    __tablename__   = 'capital_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    MainIncomeSource     = db.Column(db.String(200))
    OtherIncomeSource     = db.Column(db.String(200))
    NoOfIncomeEarners     = db.Column(db.String(200))
    HasBankAccount     = db.Column(db.String(200))
    FirstFundingOption     = db.Column(db.String(200))
    NeedsALoan     = db.Column(db.String(200))
    PayBackMonths     = db.Column(db.String(200))
    HarvestQtyChanged     = db.Column(db.String(200))
    PestExpenseChanged     = db.Column(db.String(200))

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}  
    def __repr__(self):
        return '<CapitalTable %r>' % self.id

class CreditAccessTable(db.Model):
    __tablename__   = 'credit_access_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    HasServedAsTreasurer     = db.Column(db.String(200))
    DurationAsTreasurer     = db.Column(db.String(200))
    SavesMoneyMonthly     = db.Column(db.String(200))
    SavingsAmount     = db.Column(db.String(200))
    HadDifficultyRepaying     = db.Column(db.String(200))
    DifficultLoanAmount     = db.Column(db.String(200))
    DifficultyReason     = db.Column(db.String(200))
    NoOfDifficultLoans     = db.Column(db.String(200))
    NoOfRepaidLoans     = db.Column(db.String(200))
    NoOfLoansOnTime     = db.Column(db.String(200))
    EstMonthlyIncome  = db.Column(db.String(200))
    CostOfCultivation     = db.Column(db.String(200))
    FarmProduceExchanged    = db.Column(db.String(200))
    NoOfTimesExchanged     = db.Column(db.String(200))
    Collateral    = db.Column(db.String(200))
    ApplyLoanAmount     = db.Column(db.String(200))
    YearsOfCultivating     = db.Column(db.String(200))
    AnnualTurnover     = db.Column(db.String(200))

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CreditAccessTable %r>' % self.id
class CreditHistoryTable(db.Model):
    __tablename__   = 'credit_history_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    HasTakenLoanBefore     = db.Column(db.String(200))
    SourceOfLoan     = db.Column(db.String(200))
    PastLoanAmount     = db.Column(db.String(200))
    HowLoanWasRepaid     = db.Column(db.String(200))
    IsReadyToPayInterest     = db.Column(db.String(200))
    CanProvideCollateral     = db.Column(db.String(200))
    WhyNoCollateral = db.Column(db.String(200))
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CreditHistoryTable %r>' % self.id

class ProductivityViabilityTable(db.Model):
    __tablename__   = 'productivity_viability_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    CropsCultivated     = db.Column(db.String(200))
    GrowsCrops     = db.Column(db.String(200))
    OilPalmFertilizers     = db.Column(db.String(200))
    CocoaFertilizers     = db.Column(db.String(200))
    FertilizerFrequency     = db.Column(db.String(200))
    PestFungHerbicides     = db.Column(db.String(200))
    StageChemicalApplied     = db.Column(db.String(200))
    NoOfOilDrums     = db.Column(db.String(200))
    NoOfBagsSesame     = db.Column(db.String(200))
    NoOfBagsSoyaBeans     = db.Column(db.String(200))
    NoOfBagsMaize     = db.Column(db.String(200))
    NoOfBagsSorghum    = db.Column(db.String(200))
    NoOfBagsCocoaBeans     = db.Column(db.String(200))
    CropTrainedOn     = db.Column(db.String(200))
    WhereWhenWhoTrained     = db.Column(db.String(200))
    NoOfTraining     = db.Column(db.String(200))
    PruningFrequency     = db.Column(db.String(200))
    CropBasedProblems     = db.Column(db.String(200))
    TooYoungCrops     = db.Column(db.String(200))
    YoungCropsAndStage     = db.Column(db.String(200))
    CultivationStartdate     = db.Column(db.String(200))
    IsIntensiveFarmingPractised     = db.Column(db.String(200))
    EconomicActivities     = db.Column(db.String(200))
    
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<ProductivityViabilityTable %r>' % self.id

class AgronomyServicesTable(db.Model):
    __tablename__   = 'agronomy_services_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
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
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
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
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    MobilePhoneType     = db.Column(db.String(200))
    Avweeklyphoneuse     = db.Column(db.String(200))
    Callsoutnumber     = db.Column(db.String(200))
    Callsoutminutes     = db.Column(db.String(200))
    Callsinnumber     = db.Column(db.String(200))
    Callinminutes     = db.Column(db.String(200))
    SMSsent     = db.Column(db.String(200))
    Dataprecedingplanswitch     = db.Column(db.String(200))
    Billpaymenthistory     = db.Column(db.String(200))
    Avweeklydatarefill     = db.Column(db.String(200))
    NoOfmobileapps     = db.Column(db.String(200))
    AvTimeSpentOnApp     = db.Column(db.String(200))
    MobileAppKinds     = db.Column(db.String(200))
    AppDeleteRate     = db.Column(db.String(200))
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<MobileDataTable %r>' % self.id
class FarmlandTable(db.Model):
    __tablename__   = 'farmland_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    NoOfFarmlands     = db.Column(db.String(200))
    OwnerOrCaretaker     = db.Column(db.String(200))
    FarmOwnerName     = db.Column(db.String(200))
    FarmOwnerPhoneNo     = db.Column(db.String(200))
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
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    HowLongBeenFarming     = db.Column(db.String(200))
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
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    SizeOfFarm     = db.Column(db.String(200))
    FarmIsRentedorLeased     = db.Column(db.String(200))
    NoOfYearsLeased     = db.Column(db.String(200))
    UsesMachines     = db.Column(db.String(200))
    RotatesCrops     = db.Column(db.String(200))
    NoOfHectaresProducedYearly     = db.Column(db.String(200))
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
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    MachinesUsed     = db.Column(db.String(200))
    MachineHasHelped     = db.Column(db.String(200))
    AdviseMachineOrLabour     = db.Column(db.String(200))
    OtherMachinesNeeded     = db.Column(db.String(200))
    CanAcquireMoreLands     = db.Column(db.String(200))
    PercentCostSaved     = db.Column(db.String(200)) 
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<MechanizationTable %r>' % self.id
class CultivationTable(db.Model):
    __tablename__   = 'cultivation_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    type_of_labor     = db.Column(db.String(200))
    pay_for_labor     = db.Column(db.String(200))
    how_many_housechildren_help     = db.Column(db.String(200))
    season_children_help     = db.Column(db.String(200))
    labor_children_do     = db.Column(db.String(200))
    household_vs_hire_cost     = db.Column(db.String(200))
    labor_women_do     = db.Column(db.String(200))
    percent_female_hired     = db.Column(db.String(200)) 
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CultivationTable %r>' % self.id
class HarvestTable(db.Model):
    __tablename__   = 'harvest_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    when_is_harvest_season     = db.Column(db.String(200))
    no_of_hired_workers     = db.Column(db.String(200))
    no_of_family_workers     = db.Column(db.String(200))
    no_of_permanent_workers    = db.Column(db.String(200))
    no_hired_constantly     = db.Column(db.String(200))
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<HarvestTable %r>' % self.id

class CareTable(db.Model):
    __tablename__ = 'care_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    HealthCentLoc= db.Column(db.String(200))
    HealthCentCount= db.Column(db.String(200))
    HealthCentDistance= db.Column(db.String(200))
    HealthCentFunctional= db.Column(db.String(200))
    Affordable= db.Column(db.String(200))
    FarmDistance= db.Column(db.String(200))
    InjuryEvent= db.Column(db.String(200))
    FirstAid= db.Column(db.String(200))
    LastCheck= db.Column(db.String(200))
    InSchool= db.Column(db.String(200))
    Level= db.Column(db.String(200))
    SchoolCount= db.Column(db.String(200))
    SchoolFunctional= db.Column(db.String(200))
    Qualification= db.Column(db.String(200))
    StudyTime= db.Column(db.String(200))
    StudyWhere= db.Column(db.String(200))
    AltIncomeSource= db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CareTable %r>' % self.id

class Planet(db.Model):
    __tablename__ = 'planet_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    PlanToExpand= db.Column(db.String(200))
    Crop= db.Column(db.String(200))
    Variety= db.Column(db.String(200))
    RaiseOrBuy= db.Column(db.String(200))
    BuyWhere= db.Column(db.String(200))
    SeedlingPrice= db.Column(db.String(200))
    QtyBought= db.Column(db.String(200))
    DegradedLand= db.Column(db.String(200))
    CropRotation= db.Column(db.String(200))
    Season= db.Column(db.String(200))
    Disaster= db.Column(db.String(200))
    Burning= db.Column(db.String(200))
    Mill= db.Column(db.String(200))
    EnergySource= db.Column(db.String(200))
    ReplacedTree= db.Column(db.String(200))
    Placement= db.Column(db.String(200))
    SourceOfWater= db.Column(db.String(200))
    CoverCrops= db.Column(db.String(200))
    Intercrop= db.Column(db.String(200))
    CropIntercropped= db.Column(db.String(200))
    WasteMgt= db.Column(db.String(200))
    WasteDisposal= db.Column(db.String(200))
    RecycleWaste= db.Column(db.String(200))
    Suffered= db.Column(db.String(200))
    WhenSuffered= db.Column(db.String(200))
    GreyWater= db.Column(db.String(200))
    RecycleGreyWater= db.Column(db.String(200))
    Pollution= db.Column(db.String(200))
    PollutionFreq= db.Column(db.String(200))
    Measures= db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<Planet %r>' % self.id

class Safety(db.Model):
    __tablename__ = 'safety_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    Ferment  = db.Column(db.String(200))
    FermentDays  = db.Column(db.String(200))
    FermentReason  = db.Column(db.String(200))
    BrokenQty  = db.Column(db.String(200))
    DoWithBroken  = db.Column(db.String(200))
    UnripeQty  = db.Column(db.String(200))
    DoWithUnripe  = db.Column(db.String(200))
    CocoaStore  = db.Column(db.String(200))
    FFBStore  = db.Column(db.String(200))
    Herbicide  = db.Column(db.String(200))
    HerbicideStore  = db.Column(db.String(200))
    AgroChemSource  = db.Column(db.String(200))
    HarvestTool  = db.Column(db.String(200))
    Wear  = db.Column(db.String(200))
    Disposal  = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<Safety %r>' % self.id

class LivingTable(db.Model):
    __tablename__ = 'living_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    HouseOwned = db.Column(db.String(200))
    StaysWithFamily = db.Column(db.String(200))
    RelationshipWithOwner = db.Column(db.String(200))
    HouseHoldEats = db.Column(db.String(200))
    MaleUnderAge = db.Column(db.String(200))
    FemaleUnderAge = db.Column(db.String(200))
    ChildrenUnderAge = db.Column(db.String(200))
    MaleAboveAge = db.Column(db.String(200))
    FemaleAboveAge = db.Column(db.String(200))
    ChildrenAboveAge = db.Column(db.String(200))
    LivesWith = db.Column(db.String(200))
    OwnOtherLands = db.Column(db.String(200))
    StandardofLiving = db.Column(db.String(200))
    SourceOfWater = db.Column(db.String(200))
    SourceEverytime = db.Column(db.String(200))
    CookingMethod = db.Column(db.String(200))
    HaveElectricity = db.Column(db.String(200))
    PowerPayment = db.Column(db.String(200))
    Typeoftoilet = db.Column(db.String(200))
    KitchenSink = db.Column(db.String(200))
    HasGroup = db.Column(db.String(200))
    Group = db.Column(db.String(200))
    Position = db.Column(db.String(200))
    HasAccessedInput = db.Column(db.String(200))
    Input = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<LivingTable %r>' % self.id

class ConditionsTable(db.Model):
    __tablename__   = 'conditions_table'
    id     = db.Column(db.String(200), unique=True, primary_key=True)
    Bvn     = db.Column(db.String(200))
    duration     = db.Column(db.String(200))
    seller     = db.Column(db.String(200))
    seller_mou     = db.Column(db.String(200))
    CropYieldPrediction     = db.Column(db.String(200), default='0')
    CropExpectedMarketValue      = db.Column(db.String(200), default='0')
    ZowaselMarketplacePriceOffers     = db.Column(db.String(200), default='0')
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<ConditionsTable %r>' % self.id

class CropInfo(db.Model):
    __tablename__   = 'crop_info'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    tracing_id     = db.Column(db.String(200))
    crop_type  = db.Column(db.String(200))
    sourcing_location  = db.Column(db.String(200))
    crop_origin  = db.Column(db.String(200))
    crop_qty  = db.Column(db.String(200))
    crop_variety  = db.Column(db.String(200))
    cooperative  = db.Column(db.String(200))
    no_of_farmer_group  = db.Column(db.String(200))
    female_to_male  = db.Column(db.String(200))
    farmer_name  = db.Column(db.String(200))
    gender  = db.Column(db.String(200))
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CropInfo %r>' % self.id

class CropQuality(db.Model):
    __tablename__   = 'crop_quality'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    tracing_id     = db.Column(db.String(200))
    moisture_content  = db.Column(db.String(200))
    foreign_matter  = db.Column(db.String(200))
    test_weight  = db.Column(db.String(200))
    quality  = db.Column(db.String(200))
    rotten_shriveled  = db.Column(db.String(200))
    hardness  = db.Column(db.String(200))
    splits  = db.Column(db.String(200))
    oil_content  = db.Column(db.String(200))
    infestation  = db.Column(db.String(200))
    hectoliter  = db.Column(db.String(200))
    total_defects  = db.Column(db.String(200))
    dockage  = db.Column(db.String(200))
    ash_content  = db.Column(db.String(200))
    insoluble_ash  = db.Column(db.String(200))
    volatile  = db.Column(db.String(200))
    mold_weight  = db.Column(db.String(200))
    drying_process  = db.Column(db.String(200))
    dead_insects  = db.Column(db.String(200))
    excreta  = db.Column(db.String(200))
    insect_defiled  = db.Column(db.String(200))
    curcumin  = db.Column(db.String(200))
    extraneous  = db.Column(db.String(200))

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CropQuality %r>' % self.id

class InputsInfo(db.Model):
    __tablename__   = 'inputs_info'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    tracing_id     = db.Column(db.String(200))
    Fertilizers  = db.Column(db.String(200))
    Herbicides  = db.Column(db.String(200))
    Fungicides  = db.Column(db.String(200))
    Insecticides  = db.Column(db.String(200))
    Seeds  = db.Column(db.String(200))
    

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<InputsInfo %r>' % self.id

class Warehouse(db.Model):
    __tablename__   = 'warehouse_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    tracing_id     = db.Column(db.String(200))
    location  = db.Column(db.String(200))
    warehouse_type  = db.Column(db.String(200))
    capacity  = db.Column(db.String(200))
    standard  = db.Column(db.String(200))
    insurance  = db.Column(db.String(200))
    duration  = db.Column(db.String(200))
    cost  = db.Column(db.String(200))

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<Warehouse %r>' % self.id

class Shipment(db.Model):
    __tablename__   = 'shipment_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    tracing_id     = db.Column(db.String(200))
    location  = db.Column(db.String(200))
    loading_date  = db.Column(db.String(200))
    no_of_people  = db.Column(db.String(200))
    vehicle_type  = db.Column(db.String(200))
    plate_no  = db.Column(db.String(200))
    vehicle_capacity  = db.Column(db.String(200))
    driver_name  = db.Column(db.String(200))
    driver_number  = db.Column(db.String(200))
    insurance  = db.Column(db.String(200))
    delivery_time  = db.Column(db.String(200))
    delivery_date  = db.Column(db.String(200))
    arrival_time  = db.Column(db.String(200))
    no_of_police  = db.Column(db.String(200))
    local_levy  = db.Column(db.String(200))
    state_levy  = db.Column(db.String(200))
    truck_levy  = db.Column(db.String(200))
    inter_state_levy  = db.Column(db.String(200))
    no_of_offloaders  = db.Column(db.String(200))
    quality_check  = db.Column(db.String(200))
    quality_checked  = db.Column(db.String(200))
    quality_accepted  = db.Column(db.String(200))
    quality_rejected  = db.Column(db.String(200))

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<Shipment %r>' % self.id


class Recommendation(db.Model):
    __tablename__   = 'recommendation_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    tracing_id     = db.Column(db.String(200))
    rec_one  = db.Column(db.String(200))
    rec_two  = db.Column(db.String(200))
    rec_three  = db.Column(db.String(200))

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<Recommendation %r>' % self.id

class ScoreAnalytics(db.Model):
    __tablename__   = 'score_analytics'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    Bvn     = db.Column(db.String(200))
    Scores  = db.Column(db.String(200))
    Conditions  = db.Column(db.String(200))
    Capital  = db.Column(db.String(200))
    Collateral  = db.Column(db.String(200))
    Capacity  = db.Column(db.String(200))
    Character  = db.Column(db.String(200))
    

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<ScoreAnalytics %r>' % self.id

db.init_app(app)
with app.app_context():
    db.create_all()



