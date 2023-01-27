from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *
import pickle
from io import StringIO
import pandas as pd
from modelExample import preprocess_df, bin_target
model = pickle.load(open('modelExample.pkl','rb'))

# add scorecard
class AddScoreCard(Resource):	
    def post(self):
        bvn=request.json['bvn']
        farmer = ScoreCard.query.filter_by(bvn=bvn).all()
        if farmer:
            return {"error":True,"message":bvnexists}
        else:
            farmer = pd.DataFrame([['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits']],columns=['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits'])
            for col in farmer.columns:
                farmer[col] = request.json[col]
            #print(farmer)
            farmer['applyLoanAmount'] = applyLoan(bvn)
            farmer = farmer.rename({'number_of_land':'numberOfLand',
            'estimate_monthly_income':'estimateMonthlyIncome','years_cultivating':'yearsCultivating'},axis=1)
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
        return jsonify({"error":False,"message":f'scorecard{added}'})

# get scorecard by bvn
class Scorecardbvn(Resource):
    def get(self, bvn):
        cards = ScoreCard.query.filter_by(bvn=bvn).all()
        if cards:
            return {"error":False,"message":f'scorecard{retrieved}',"data":[card.json() for card in cards]}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        cards = ScoreCard.query.filter_by(bvn=bvn).all()
        if cards:
            for card in cards:
                db.session.delete(card)
            db.session.commit()
            return {"error":False,"message":f'scorecard{removed}'}
        else:
            return ({"error":True,"message":bvnnotfound})
        
# get scorecard by id   
class Scorecardid(Resource):
    def get(self, id):
        farmer = ScoreCard.query.filter_by(id=id).first()
        if farmer:
            return {"error":False,"message":f'scorecard{retrieved}',"data":farmer.json()}
        else:
            return {"error":True,"message":idnotfound}
    def delete(self, id):
        farmer = ScoreCard.query.filter_by(id=id).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'scorecard{removed}'}
        else:
            return ({"error":True,"message":idnotfound})
        
# get all scorecard
class AllScorecard(Resource):
    def get(self):
        all_farmers = ScoreCard.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'scorecard{retrieved}','data': all_farmers})

# with pagination
class ListScorecard(Resource):
    def get(self,limit):
        all_farmers = ScoreCard.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
