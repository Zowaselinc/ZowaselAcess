from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *
import pickle
import pandas as pd
from modelExample import preprocess_df, bin_target
model = pickle.load(open('modelExample.pkl','rb'))

# add crop card
class AddCropCard(Resource):	
    def post(self):
        try:
            bvn=request.json['bvn']
            farmer = Cropcard.query.filter_by(bvn=bvn).all()
            if farmer:
                return {"error":True,"message":bvnexists}
            else:
                card = Cropcard(bvn=request.json['bvn'],farmer_name=request.json['farmer_name'],
        crop_name=request.json['crop_name'],fertilizer_cost=request.json['fertilizer_cost'],
        fertilizer=request.json['fertilizer'],mechanization_cost=request.json['mechanization_cost'],
        mechanization=request.json['mechanization'], labour_cost=request.json['labour_cost'],
        labour=request.json['labour'],harvest_cost=request.json['harvest_cost'],
        harvest=request.json['harvest'],other_cost=request.json['other_cost'],
        others=request.json['others'],date_filled=request.json['date_filled'])
                db.session.add(card)
                db.session.commit()
                # upload loan amount
                farmer = ScoreCard.query.filter_by(bvn=bvn).first()
                if farmer:
                    farmer.applyLoanAmount = applyLoan(bvn)   
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
                    tdf = tdf.rename({'number_of_land':'numberOfLand',
                'estimate_monthly_income':'estimateMonthlyIncome','years_cultivating':'yearsCultivating'},axis=1)
                    cols=['age', 'numberOfLand', 'owner_caretaker', 'crop','applyLoanAmount',
            'intercropping', 'machines', 'estimateMonthlyIncome','yearsCultivating']
                    tdf = preprocess_df(tdf[cols])
                    train_cols = ['number_of_land', 'owner_caretaker', 'intercropping', 'machines',
       'estimate_monthly_income', 'apply_loan_amount', 'years_cultivating',
       'crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
                    farmer.score = model.predict_proba(tdf[train_cols])[:,1].round(2)[0]
                    farmer.bin=bin_target([farmer.score])[0]
                    db.session.commit()
                return {"error":False,"message":f'cropcard{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}

# get crop card with bvn
class Cropcardbvn(Resource):
    def get(self, bvn):
        cards = Cropcard.query.filter_by(bvn=bvn).all()
        if cards:
            return {"error":False,"message":f'cropcard{retrieved}',"data":[card.json() for card in cards]}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        cards = Cropcard.query.filter_by(bvn=bvn).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
            return {"error":False,"message":f'cropcard{removed}'}
        else:
            return ({"error":True,"message":bvnnotfound})

# get cropcard with id  
class Cropcardid(Resource):
    def get(self, id):
        cards = Cropcard.query.filter_by(id=id).all()
        if cards:
            return {"error":False,"message":f'cropcard{retrieved}',"data":[card.json() for card in cards]}
        else:
            return {"error":True,"message":idnotfound}
    def delete(self, id):
        cards = Cropcard.query.filter_by(id=id).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
            return {"error":False,"message":f'cropcard{removed}'}
        else:
            return ({"error":True,"message":idnotfound})

# get cropcard with cropname    
class Cropcardcrop_name(Resource):
    def get(self, crop_name):
        cards = Cropcard.query.filter_by(crop_name=crop_name).all()
        if cards:
            return {"error":False,"message":f'cropcard{retrieved}',"data":[card.json() for card in cards]}
        else:
            return {"error":True,"message":cropnotfound}
    def delete(self, crop_name):
        cards = Cropcard.query.filter_by(crop_name=crop_name).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
            return {"error":False,"message":f'cropcard{removed}'}
        else:
            return ({"error":True,"message":cropnotfound})

# get allcropcard
class AllCropcard(Resource):
    def get(self):
        all_cards = Cropcard.query.all()
        all_cards = [farmer.json() for farmer in all_cards]
        return jsonify({"error":False,"message":f'cropcard{retrieved}',"data": all_cards})

# with pagination
class ListCropcard(Resource):
    def get(self, limit):
        all_cards = Cropcard.query.all()
        all_cards = [farmer.json() for farmer in all_cards]
        return jsonify(get_paginated_list(
        all_cards, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
