from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_restplus import Resource, Api, fields
#from flask_migrate import Migrate
from datetime import datetime
from flask_mysqldb import MySQL
import pymysql
from sqlalchemy import create_engine, exc
from flask_cors import CORS
#from sqlalchemy.orm import *
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates

import uuid

import os

def generate_uuid():
    return "ZOWASEL-"+str(uuid.uuid4())
def generate_tid():
    return "T"+str(uuid.uuid4())

# Initializing flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# connect to the database
basedir = os.path.abspath(os.path.dirname(__file__)) 
forbidden = ("", " ")
USER = "zowasekadmin" #os.getenv('USER')
PASSWORD = "zowasel1234!A" #os.environ.get('PASSWORD')
URLDB = "zowaselaidb.celbaavi1fuh.us-east-1.rds.amazonaws.com/zowaselai"#os.environ.get('URLDB')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USER}:{PASSWORD}@{URLDB}'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://zowasekadmin:zowasel1234!A@zowaselaidb.celbaavi1fuh.us-east-1.rds.amazonaws.com/zowaselai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app, resources={r'/*': {'origins': '*'}})
#CORS(app, resources=r'/api/*', headers='Content-Type')


# Create Tables 

class Loan(db.Model):
    __tablename__ = 'loans'
    
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    type      = db.Column(db.String(200), unique=True)
    company      = db.Column(db.String(200))
    repayment_months      = db.Column(db.Integer)
    interest_rate_per_annum      = db.Column(db.Integer)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    @validates('type','company','repayment_months','interest_rate_per_annum')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    @validates('repayment_months','interest_rate_per_annum')
    def check_input(self, key, value):
        try:
            int(value)
        except ValueError:
            raise ValueError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<Loan %r>' % self.id

class BuyersDailyPrice(db.Model):
    __tablename__ = 'buyers_daily_price'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    crop      = db.Column(db.String(200))
    location      = db.Column(db.String(200))
    classification      = db.Column(db.String(200))
    min_price      = db.Column(db.Integer)
    ave_price      = db.Column(db.Integer)
    max_price      = db.Column(db.Integer)
    date_filled = db.Column(db.String(200))
    quality_spec = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    @validates('crop','location','classification','min_price','ave_price','max_price',
    'date_filled','quality_spec')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<BuyersDailyPrice %r>' % self.id

class BuyersOffers(db.Model):
    __tablename__ = 'buyers_offers'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    crop      = db.Column(db.String(200))
    location      = db.Column(db.String(200))
    classification      = db.Column(db.String(200))
    min_price      = db.Column(db.Integer)
    ave_price      = db.Column(db.Integer)
    max_price      = db.Column(db.Integer)
    date_filled = db.Column(db.String(200))
    quality_spec = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    @validates('crop','location','classification','min_price','ave_price','max_price',
    'date_filled','quality_spec')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<BuyersOffers %r>' % self.id

class FarmGatePrices(db.Model):
    __tablename__ = 'farmgate_prices'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    crop      = db.Column(db.String(200))
    location      = db.Column(db.String(200))
    classification      = db.Column(db.String(200))
    min_price      = db.Column(db.Integer)
    ave_price      = db.Column(db.Integer)
    max_price      = db.Column(db.Integer)
    date_filled = db.Column(db.String(200))
    quality_spec = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    @validates('crop','location','classification','min_price','ave_price','max_price',
    'date_filled','quality_spec')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<FarmGatePrices %r>' % self.id

class MarketPrices(db.Model):
    __tablename__ = 'market_prices'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    crop      = db.Column(db.String(200))
    location      = db.Column(db.String(200))
    classification      = db.Column(db.String(200))
    min_price      = db.Column(db.Integer)
    ave_price      = db.Column(db.Integer)
    max_price      = db.Column(db.Integer)
    date_filled = db.Column(db.String(200))
    quality_spec = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    @validates('crop','location','classification','min_price','ave_price','max_price',
    'date_filled','quality_spec')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<MarketPrices %r>' % self.id

class Cropcard(db.Model):
    __tablename__ = 'crop_card'
    
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    farmer_name = db.Column(db.String(200))
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    crop_name = db.Column(db.String(200))
    fertilizer_cost      = db.Column(db.String(200))
    fertilizer      = db.Column(db.String(200))
    mechanization_cost      = db.Column(db.String(200))
    mechanization      = db.Column(db.String(200))
    labour_cost      = db.Column(db.String(200))
    labour      = db.Column(db.String(200))
    harvest_cost      = db.Column(db.String(200))
    harvest      = db.Column(db.String(200))
    other_cost      = db.Column(db.String(200))
    others      = db.Column(db.String(200))
    date_filled      = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)    

    @validates('farmer_name','bvn','mobile','crop_name','fertilizer_cost','fertilizer','mechanization_cost',
    'mechanization','labour_cost','labour','harvest_cost','other_cost','others','date_filled')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    @validates('fertilizer_cost','mechanization_cost','labour_cost','harvest_cost','other_cost')
    def check_input(self, key, value):
        try:
            int(value)
        except ValueError:
            raise ValueError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<Loan %r>' % self.type

class ScoreCard(db.Model):
    __tablename__   = 'score_card'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
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
    score     = db.Column(db.String(200))
    bin     = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    @validates('bvn','mobile','age','number_of_land','address','owner_caretaker','crop','intercropping',
    'machines','estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm',
    'number_of_crops','is_in_a_cooperative','no_of_agronomist_visits')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<ScoreCard %r>' % self.id


class LoanTransfer(db.Model):

    __tablename__   = 'loantransfers'
    
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    tag = db.Column(db.String(200), default=generate_tid, unique=True)
    type      = db.Column(db.String(200))
    company      = db.Column(db.String(200))
    amount             = db.Column(db.String(200))
    repayment_amount = db.Column(db.String(200))
    repayment_months = db.Column(db.String(200))
    status      = db.Column(db.String(200))
    group     = db.Column(db.String(200))
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200))
    score     = db.Column(db.String(200))
    bin     = db.Column(db.String(200))
    transfer_date   = db.Column(db.String(200))
    due_date   = db.Column(db.String(200))
    repaid = db.Column(db.String(200))
    balance = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)

    @validates('type','bvn','mobile','amount')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    @validates('amount')
    def check_input(self, key, value):
        try:
            int(value)
        except ValueError:
            raise ValueError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 

    def __repr__(self):
        return '<LoanTransfer %r>' % self.id


class FarmerTable(db.Model):
    __tablename__   = 'farmer_table'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    tag = db.Column(db.String(200), default=generate_uuid, unique=True)
    firstname     = db.Column(db.String(200))
    surname     = db.Column(db.String(200))
    middlename     = db.Column(db.String(200))
    email     = db.Column(db.String(200), unique=True)
    telephone     = db.Column(db.String(200),unique=True)
    age     = db.Column(db.String(200))
    gender     = db.Column(db.String(200))
    language = db.Column(db.String(200))
    maritalstatus     = db.Column(db.String(200))
    bankname = db.Column(db.String(200))
    accountno     = db.Column(db.String(200))
    bvn     = db.Column(db.String(200))
    meansofid     = db.Column(db.String(200))
    issuedate     = db.Column(db.String(200))
    expirydate     = db.Column(db.String(200))
    nin     = db.Column(db.String(200))
    permanentaddress     = db.Column(db.String(200))
    landmark     = db.Column(db.String(200))
    stateoforigin     = db.Column(db.String(200))
    isinagroup     = db.Column(db.String(200))
    reasonnogroup     = db.Column(db.String(200))
    group     = db.Column(db.String(200))
    numberofmembers     = db.Column(db.String(200))
    firstnamenok     = db.Column(db.String(200))
    surnamenok     = db.Column(db.String(200))
    middlenamenok     = db.Column(db.String(200))
    relationshipnok     = db.Column(db.String(200))
    occupationnok     = db.Column(db.String(200))
    telephonenok     = db.Column(db.String(200))
    permanentaddressnok     = db.Column(db.String(200))
    landmarknok     = db.Column(db.String(200))
    ninnok     = db.Column(db.String(200))

    @validates('firstname','surname','middlename','email','telephone',
    'age','gender','language','maritalstatus',
    'bankname','accountno','bvn','meansofid','issuedate','expirydate',
    'nin','permanentaddress','landmark','stateoforigin','isinagroup',
    'reasonnogroup','group','numberofmembers','firstnamenok','surnamenok','middlenamenok',
    'relationshipnok','occupationnok','telephonenok','permanentaddressnok','landmarknok','ninnok')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}  
    
    def __repr__(self):
        return '<FarmerTable %r>' % self.id



class CapitalTable(db.Model):
    __tablename__   = 'capital_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    mainincomesource     = db.Column(db.String(200))
    otherincomesource     = db.Column(db.String(200))
    noofincomeearners     = db.Column(db.String(200))
    hasbankaccount     = db.Column(db.String(200))
    firstfundingoption     = db.Column(db.String(200))
    needsaloan     = db.Column(db.String(200))
    paybackmonths     = db.Column(db.String(200))
    harvestqtychanged     = db.Column(db.String(200))
    pestexpensechanged     = db.Column(db.String(200))

    @validates('bvn','mobile','mainincomesource','otherincomesource','noofincomeearners',
    'hasbankaccount','firstfundingoption','needsaloan','paybackmonths','harvestqtychanged',
    'pestexpensechanged')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}  
    def __repr__(self):
        return '<CapitalTable %r>' % self.id

class CreditAccessTable(db.Model):
    __tablename__   = 'credit_access_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    hasservedastreasurer     = db.Column(db.String(200))
    durationastreasurer     = db.Column(db.String(200))
    savesmoneymonthly     = db.Column(db.String(200))
    savingsamount     = db.Column(db.String(200))
    haddifficultyrepaying     = db.Column(db.String(200))
    difficultloanamount     = db.Column(db.String(200))
    difficultyreason     = db.Column(db.String(200))
    noofdifficultloans     = db.Column(db.String(200))
    noofrepaidloans     = db.Column(db.String(200))
    noofloansontime     = db.Column(db.String(200))
    estmonthlyincome  = db.Column(db.String(200))
    costofcultivation     = db.Column(db.String(200))
    farmproduceexchanged    = db.Column(db.String(200))
    nooftimesexchanged     = db.Column(db.String(200))
    collateral    = db.Column(db.String(200))
    applyloanamount     = db.Column(db.String(200))
    yearsofcultivating     = db.Column(db.String(200))
    annualturnover     = db.Column(db.String(200))
    
    @validates('bvn','mobile','hasservedastreasurer','durationastreasurer','savesmoneymonthly',
    'savingsamount','haddifficultyrepaying','difficultloanamount','difficultyreason',
    'noofdifficultloans','noofrepaidloans','noofloansontime','estmonthlyincome','costofcultivation',
    'farmproduceexchanged','nooftimesexchanged','collateral','applyloanamount','yearsofcultivating',
    'annualturnover')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CreditAccessTable %r>' % self.id
class CreditHistoryTable(db.Model):
    __tablename__   = 'credit_history_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    hastakenloanbefore     = db.Column(db.String(200))
    sourceofloan     = db.Column(db.String(200))
    pastloanamount     = db.Column(db.String(200))
    howloanwasrepaid     = db.Column(db.String(200))
    isreadytopayinterest     = db.Column(db.String(200))
    canprovidecollateral     = db.Column(db.String(200))
    whynocollateral = db.Column(db.String(200))
    
    @validates('bvn','mobile','hastakenloanbefore','sourceofloan','pastloanamount','howloanwasrepaid',
    'isreadytopayinterest','canprovidecollateral','whynocollateral')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CreditHistoryTable %r>' % self.id

class ProductivityViabilityTable(db.Model):
    __tablename__   = 'productivity_viability_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    cropscultivated     = db.Column(db.String(200))
    growscrops     = db.Column(db.String(200))
    oilpalmfertilizers     = db.Column(db.String(200))
    cocoafertilizers     = db.Column(db.String(200))
    fertilizerfrequency     = db.Column(db.String(200))
    pestfungherbicides     = db.Column(db.String(200))
    stagechemicalapplied     = db.Column(db.String(200))
    noofoildrums     = db.Column(db.String(200))
    noofbagssesame     = db.Column(db.String(200))
    noofbagssoyabeans     = db.Column(db.String(200))
    noofbagsmaize     = db.Column(db.String(200))
    noofbagssorghum    = db.Column(db.String(200))
    noofbagscocoabeans     = db.Column(db.String(200))
    croptrainedon     = db.Column(db.String(200))
    wherewhenwhotrained     = db.Column(db.String(200))
    nooftraining     = db.Column(db.String(200))
    pruningfrequency     = db.Column(db.String(200))
    cropbasedproblems     = db.Column(db.String(200))
    tooyoungcrops     = db.Column(db.String(200))
    youngcropsandstage     = db.Column(db.String(200))
    cultivationstartdate     = db.Column(db.String(200))
    isintensivefarmingpractised     = db.Column(db.String(200))
    economicactivities     = db.Column(db.String(200))
    
    @validates('bvn','mobile','cropscultivated','growscrops','oilpalmfertilizers','cocoafertilizers',
    'fertilizerfrequency','pestfungherbicides','stagechemicalapplied','noofoildrums',
    'noofbagssesame','noofbagssoyabeans','noofbagsmaize','noofbagssorghum','noofbagscocoabeans',
    'croptrainedon','wherewhenwhotrained','nooftraining','pruningfrequency','cropbasedproblems',
    'tooyoungcrops','youngcropsandstage','cultivationstartdate','isintensivefarmingpractised',
    'economicactivities')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<ProductivityViabilityTable %r>' % self.id

class AgronomyServicesTable(db.Model):
    __tablename__   = 'agronomy_services_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    knowsagriprocessed     = db.Column(db.String(200))
    agronomistthattrainedyou     = db.Column(db.String(200))
    canmanageecosystem    = db.Column(db.String(200))
    howtomanageecosystem     = db.Column(db.String(200))
    istrainingbeneficial     = db.Column(db.String(200))
    fieldroutines     = db.Column(db.String(200))
    harvestingchanges     = db.Column(db.String(200))
    iscropcalendarbeneficial     = db.Column(db.String(200))
    cropcalendarbenefits     = db.Column(db.String(200))
    recordkeepingbenefits     = db.Column(db.String(200))
    
    @validates('bvn','mobile','knowsagriprocessed','agronomistthattrainedyou','canmanageecosystem',
    'howtomanageecosystem','istrainingbeneficial','fieldroutines','harvestingchanges',
    'iscropcalendarbeneficial','cropcalendarbenefits','recordkeepingbenefits')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<AgronomyServicesTable %r>' % self.id

class PsychometricsTable(db.Model):
    __tablename__   = 'psychometrics_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    fluidintelligence     = db.Column(db.String(200))
    attitudesandbeliefs     = db.Column(db.String(200))
    agribusinessskills     = db.Column(db.String(200))
    ethicsandhonesty     = db.Column(db.String(200))
    savesenough     = db.Column(db.String(200))
    haslazyneighbors     = db.Column(db.String(200))

    @validates('bvn','mobile','fluidintelligence','attitudesandbeliefs','agribusinessskills','ethicsandhonesty',
    'savesenough','haslazyneighbors')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<PsychometricsTable %r>' % self.id
class MobileDataTable(db.Model):
    __tablename__   = 'mobile_data_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    mobilephonetype     = db.Column(db.String(200))
    avweeklyphoneuse     = db.Column(db.String(200))
    callsoutnumber     = db.Column(db.String(200))
    callsoutminutes     = db.Column(db.String(200))
    callsinnumber     = db.Column(db.String(200))
    callinminutes     = db.Column(db.String(200))
    smssent     = db.Column(db.String(200))
    dataprecedingplanswitch     = db.Column(db.String(200))
    billpaymenthistory     = db.Column(db.String(200))
    avweeklydatarefill     = db.Column(db.String(200))
    noOfmobileapps     = db.Column(db.String(200))
    avtimespentonapp     = db.Column(db.String(200))
    mobileappkinds     = db.Column(db.String(200))
    appdeleterate     = db.Column(db.String(200))
    
    @validates('bvn','mobile','mobilephonetype','avweeklyphoneuse','callsoutnumber','callsoutminutes',
    'callsinnumber','callinminutes','smssent','dataprecedingplanswitch','billpaymenthistory',
    'avweeklydatarefill','noOfmobileapps','avtimespentonapp','mobileappkinds','appdeleterate')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<MobileDataTable %r>' % self.id
class FarmlandTable(db.Model):
    __tablename__   = 'farmland_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    nooffarmlands     = db.Column(db.String(200))
    ownerorcaretaker     = db.Column(db.String(200))
    farmownername     = db.Column(db.String(200))
    farmownerphoneno     = db.Column(db.String(200))
    relationshipwithowner     = db.Column(db.String(200))
    inheritedfrom     = db.Column(db.String(200))
    sizeoffarm     = db.Column(db.String(200))
    farmcoordinates     = db.Column(db.String(200))
    farmaddress     = db.Column(db.String(200))
    keepsanimals     = db.Column(db.String(200))
    animalsfeedon     = db.Column(db.String(200))
    
    @validates('bvn','mobile','nooffarmlands','ownerorcaretaker','farmownername','farmownerphoneno',
    'relationshipwithowner','inheritedfrom','sizeoffarm','farmcoordinates','farmaddress',
    'keepsanimals','animalsfeedon')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<FarmlandTable %r>' % self.id
class CapacityTable(db.Model):
    __tablename__   = 'capacity_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    howlongbeenfarming     = db.Column(db.String(200))
    participatedintraining     = db.Column(db.String(200))
    farmingpractice     = db.Column(db.String(200))
    keepsanimals     = db.Column(db.String(200))
    hascooperative     = db.Column(db.String(200))
    cooperativename     = db.Column(db.String(200))
    educationlevel     = db.Column(db.String(200))
    
    @validates('bvn','mobile','howlongbeenfarming','participatedintraining','farmingpractice',
    'keepsanimals','hascooperative','cooperativename','educationlevel')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CapacityTable %r>' % self.id

class FarmPractice(db.Model):
    __tablename__   = 'farm_practice_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    sizeoffarm     = db.Column(db.String(200))
    farmisrentedorleased     = db.Column(db.String(200))
    noofyearsleased     = db.Column(db.String(200))
    usesmachines     = db.Column(db.String(200))
    rotatescrops     = db.Column(db.String(200))
    noOfhectaresproducedyearly     = db.Column(db.String(200))
    approxfertilizeruse     = db.Column(db.String(200))
    nooffertlizerapplications     = db.Column(db.String(200))
    decisionforspraying     = db.Column(db.String(200))
    weedcontrolpractice     = db.Column(db.String(200))
    estimatedincomepercrop     = db.Column(db.String(200))
    cropthatcansellwell     = db.Column(db.String(200))
    hasfarmplanorproject     = db.Column(db.String(200))
    farmprojectinfo     = db.Column(db.String(200))
    
    @validates('bvn','mobile','sizeoffarm','farmisrentedorleased','noofyearsleased','usesmachines',
    'rotatescrops','noOfhectaresproducedyearly','approxfertilizeruse',
    'nooffertlizerapplications','decisionforspraying','weedcontrolpractice',
    'estimatedincomepercrop','cropthatcansellwell','hasfarmplanorproject','farmprojectinfo')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<FarmPractice %r>' % self.id
class MechanizationTable(db.Model):
    __tablename__   = 'mechanization_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    machinesused     = db.Column(db.String(200))
    machinehashelped     = db.Column(db.String(200))
    advisemachineorlabour     = db.Column(db.String(200))
    othermachinesneeded     = db.Column(db.String(200))
    canacquiremorelands     = db.Column(db.String(200))
    percentcostsaved     = db.Column(db.String(200)) 
    
    @validates('bvn','mobile','machinesused','machinehashelped','advisemachineorlabour','othermachinesneeded',
    'canacquiremorelands','percentcostsaved')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<MechanizationTable %r>' % self.id
class CultivationTable(db.Model):
    __tablename__   = 'cultivation_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    type_of_labor     = db.Column(db.String(200))
    pay_for_labor     = db.Column(db.String(200))
    how_many_housechildren_help     = db.Column(db.String(200))
    season_children_help     = db.Column(db.String(200))
    labor_children_do     = db.Column(db.String(200))
    household_vs_hire_cost     = db.Column(db.String(200))
    labor_women_do     = db.Column(db.String(200))
    percent_female_hired     = db.Column(db.String(200)) 
    
    @validates('bvn','mobile','type_of_labor','pay_for_labor','how_many_housechildren_help','season_children_help',
    'labor_children_do','household_vs_hire_cost','labor_women_do','percent_female_hired')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CultivationTable %r>' % self.id
class HarvestTable(db.Model):
    __tablename__   = 'harvest_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    when_is_harvest_season     = db.Column(db.String(200))
    no_of_hired_workers     = db.Column(db.String(200))
    no_of_family_workers     = db.Column(db.String(200))
    no_of_permanent_workers    = db.Column(db.String(200))
    no_hired_constantly     = db.Column(db.String(200))
    
    @validates('bvn','mobile','when_is_harvest_season','no_of_hired_workers','no_of_family_workers',
    'no_of_permanent_workers','no_hired_constantly')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<HarvestTable %r>' % self.id

class CareTable(db.Model):
    __tablename__ = 'care_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    healthcentloc= db.Column(db.String(200))
    healthcentcount= db.Column(db.String(200))
    healthcentdistance= db.Column(db.String(200))
    healthcentfunctional= db.Column(db.String(200))
    affordable= db.Column(db.String(200))
    farmdistance= db.Column(db.String(200))
    injuryevent= db.Column(db.String(200))
    firstaid= db.Column(db.String(200))
    lastcheck= db.Column(db.String(200))
    inschool= db.Column(db.String(200))
    level= db.Column(db.String(200))
    schoolcount= db.Column(db.String(200))
    schoolfunctional= db.Column(db.String(200))
    qualification= db.Column(db.String(200))
    studytime= db.Column(db.String(200))
    studywhere= db.Column(db.String(200))
    altIncomesource= db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    
    @validates('bvn','mobile','healthcentloc','healthcentcount','healthcentdistance','healthcentfunctional','affordable',
    'farmdistance','injuryevent','firstaid','lastcheck','inschool','level','schoolcount','schoolfunctional',
    'qualification','studytime','studywhere','altIncomesource')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CareTable %r>' % self.id

class Planet(db.Model):
    __tablename__ = 'planet_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    plantoexpand= db.Column(db.String(200))
    crop= db.Column(db.String(200))
    variety= db.Column(db.String(200))
    raiseorbuy= db.Column(db.String(200))
    buywhere= db.Column(db.String(200))
    seedlingprice= db.Column(db.String(200))
    qtybought= db.Column(db.String(200))
    degradedland= db.Column(db.String(200))
    croprotation= db.Column(db.String(200))
    season= db.Column(db.String(200))
    disaster= db.Column(db.String(200))
    burning= db.Column(db.String(200))
    mill= db.Column(db.String(200))
    energysource= db.Column(db.String(200))
    replacedtree= db.Column(db.String(200))
    placement= db.Column(db.String(200))
    sourceofwater= db.Column(db.String(200))
    covercrops= db.Column(db.String(200))
    intercrop= db.Column(db.String(200))
    cropintercropped= db.Column(db.String(200))
    wastemgt= db.Column(db.String(200))
    wastedisposal= db.Column(db.String(200))
    recyclewaste= db.Column(db.String(200))
    suffered= db.Column(db.String(200))
    whensuffered= db.Column(db.String(200))
    greywater= db.Column(db.String(200))
    recyclegreywater= db.Column(db.String(200))
    pollution= db.Column(db.String(200))
    pollutionfreq= db.Column(db.String(200))
    measures= db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    
    @validates('bvn','mobile','plantoexpand','crop','variety','raiseorbuy','buywhere',
    'seedlingprice','qtybought','degradedland','croprotation','season','disaster',
    'burning','mill','energysource','replacedtree','placement','sourceofwater',
    'covercrops','intercrop','cropintercropped','wastemgt','wastedisposal','recyclewaste',
    'suffered','whensuffered','greywater','recyclegreywater','pollution','pollutionfreq','measures')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<Planet %r>' % self.id

class Safety(db.Model):
    __tablename__ = 'safety_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    ferment  = db.Column(db.String(200))
    fermentdays  = db.Column(db.String(200))
    fermentreason  = db.Column(db.String(200))
    brokenqty  = db.Column(db.String(200))
    dowithbroken  = db.Column(db.String(200))
    unripeqty  = db.Column(db.String(200))
    dowithunripe  = db.Column(db.String(200))
    cocoastore  = db.Column(db.String(200))
    ffbstore  = db.Column(db.String(200))
    herbicide  = db.Column(db.String(200))
    herbicidestore  = db.Column(db.String(200))
    agrochemsource  = db.Column(db.String(200))
    harvesttool  = db.Column(db.String(200))
    wear  = db.Column(db.String(200))
    disposal  = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    
    @validates('bvn','mobile','ferment','fermentdays','fermentreason','brokenqty','dowithbroken',
    'unripeqty','dowithunripe','cocoastore','ffbstore','herbicide','herbicidestore',
    'agrochemsource','harvesttool','wear','disposal')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<Safety %r>' % self.id

class LivingTable(db.Model):
    __tablename__ = 'living_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    houseowned = db.Column(db.String(200))
    stayswithfamily = db.Column(db.String(200))
    relationshipwithowner = db.Column(db.String(200))
    householdeats = db.Column(db.String(200))
    maleunderage = db.Column(db.String(200))
    femaleunderage = db.Column(db.String(200))
    childrenunderage = db.Column(db.String(200))
    maleaboveage = db.Column(db.String(200))
    femaleaboveage = db.Column(db.String(200))
    childrenaboveage = db.Column(db.String(200))
    liveswith = db.Column(db.String(200))
    ownotherlands = db.Column(db.String(200))
    standardofliving = db.Column(db.String(200))
    sourceofwater = db.Column(db.String(200))
    sourceeverytime = db.Column(db.String(200))
    cookingmethod = db.Column(db.String(200))
    haveelectricity = db.Column(db.String(200))
    powerpayment = db.Column(db.String(200))
    typeoftoilet = db.Column(db.String(200))
    kitchensink = db.Column(db.String(200))
    hasgroup = db.Column(db.String(200))
    group = db.Column(db.String(200))
    position = db.Column(db.String(200))
    hasaccessedInput = db.Column(db.String(200))
    input = db.Column(db.String(200))
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    
    @validates('bvn','mobile','houseowned','stayswithfamily','relationshipwithowner','householdeats','maleunderage',
    'femaleunderage','childrenunderage','maleaboveage','femaleaboveage','childrenaboveage','liveswith',
    'ownotherlands','standardofliving','sourceofwater','sourceeverytime','cookingmethod','haveelectricity',
    'powerpayment','typeoftoilet','kitchensink','hasgroup','group','position','hasaccessedInput','input')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<LivingTable %r>' % self.id

class ConditionsTable(db.Model):
    __tablename__   = 'conditions_table'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    duration     = db.Column(db.String(200))
    seller     = db.Column(db.String(200))
    seller_mou     = db.Column(db.String(200))
    cropyieldprediction     = db.Column(db.String(200))
    cropexpectedmarketvalue      = db.Column(db.String(200))
    zowaselmarketplacepriceoffers     = db.Column(db.String(200))
    
    @validates('bvn','mobile','duration','seller','seller_mou')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

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

    @validates('tracing_id','crop_type','sourcing_location','crop_origin','crop_qty','crop_variety',
    'cooperative','no_of_farmer_group','female_to_male','farmer_name','gender')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

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

    @validates('tracing_id','moisture_content','foreign_matter','test_weight','quality','rotten_shriveled',
    'hardness','splits','oil_content','infestation','hectoliter','total_defects',
    'dockage','ash_content','insoluble_ash','volatile','mold_weight','drying_process',
    'dead_insects','excreta','insect_defiled','curcumin','extraneous')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<CropQuality %r>' % self.id

class InputsInfo(db.Model):
    __tablename__   = 'inputs_info'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    tracing_id     = db.Column(db.String(200))
    fertilizers  = db.Column(db.String(200))
    herbicides  = db.Column(db.String(200))
    fungicides  = db.Column(db.String(200))
    insecticides  = db.Column(db.String(200))
    seeds  = db.Column(db.String(200))
    
    @validates('tracing_id','fertilizers','herbicides','fungicides','insecticides','seeds')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

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

    @validates('tracing_id','location','warehouse_type','capacity','standard','insurance','duration','cost')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

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

    @validates('tracing_id','location','loading_date','no_of_people','vehicle_type','plate_no',
    'vehicle_capacity','driver_name','driver_number','insurance','delivery_time','delivery_date',
    'arrival_time','no_of_police','local_levy','state_levy','truck_levy','inter_state_levy',
    'no_of_offloaders','quality_check','quality_checked','quality_accepted','quality_rejected')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

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

    @validates('tracing_id','rec_one','rec_two','rec_three')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value
    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<Recommendation %r>' % self.id

class ScoreAnalytics(db.Model):
    __tablename__   = 'score_analytics'
    id     = db.Column(db.Integer, unique=True, primary_key=True)
    date_created    = db.Column(db.String(200), default=datetime.utcnow)
    bvn     = db.Column(db.String(200))
    mobile     = db.Column(db.String(200),unique=True)
    scores  = db.Column(db.String(200))
    conditions  = db.Column(db.String(200))
    capital  = db.Column(db.String(200))
    collateral  = db.Column(db.String(200))
    capacity  = db.Column(db.String(200))
    character  = db.Column(db.String(200))
    
    @validates('bvn','mobile','scores','conditions','capital','collateral','capacity','character')
    def check_input(self, key, value):
        if value in forbidden:
            raise AssertionError('invalid input')
        return value

    def json(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns} 
    def __repr__(self):
        return '<ScoreAnalytics %r>' % self.id

db.init_app(app)
with app.app_context():
    db.create_all()



