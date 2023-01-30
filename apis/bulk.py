from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *
import pickle
from io import StringIO
import pandas as pd
from modelExample import preprocess_df, bin_target
model = pickle.load(open('modelExample.pkl','rb'))



# add bulk kyf
class AddBulkFarmer(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("kyf_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(1,len(df)):
                    dfr = df.iloc[r,:]
                    farmer = FarmerTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
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
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}    

# add bulk scorecard
class AddBulkScorecard(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("scorecard_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(1,len(df)):
                    dfr = df.iloc[r,:]
                    farmer = ScoreCard.query.filter_by(bvn=dfr['bvn']).all()
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        farmer = pd.DataFrame([['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits']],columns=['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits'])
                        for col in farmer.columns:
                            farmer[col] = dfr[col]
                        farmer['applyLoanAmount'] = applyLoan(farmer['bvn'])
                        farmer = farmer.rename({'number_of_land':'numberOfLand','estimate_monthly_income':'estimateMonthlyIncome',
                     'years_cultivating':'yearsCultivating'},axis=1)
                        cols=['age', 'numberOfLand', 'owner_caretaker', 'crop','applyLoanAmount','intercropping', 'machines', 'estimateMonthlyIncome','yearsCultivating']
                        tdf = preprocess_df(farmer[cols])
                        train_cols = ['number_of_land', 'owner_caretaker', 'intercropping', 'machines',
       'estimate_monthly_income', 'apply_loan_amount', 'years_cultivating','crop1', 'crop2', 'age1', 'age2', 'age3', 'age4']
                        score = model.predict_proba(tdf[train_cols])[:,1].round(2)
                        bin=bin_target(score)
                        dfr = dfr.astype(str)
                        farmer = farmer.astype(str)
                        history = ScoreCard(bvn=dfr['bvn'],age=dfr['age'],number_of_land=dfr['number_of_land'],address=dfr['address'],
        owner_caretaker=dfr['owner_caretaker'],crop=dfr['crop'],intercropping=dfr['intercropping'], machines=dfr['machines'],
        estimate_monthly_income=dfr['estimate_monthly_income'],years_cultivating=dfr['years_cultivating'],gender=dfr['gender'],
        owns_a_bank_account=dfr['owns_a_bank_account'],size_of_farm=dfr['size_of_farm'],number_of_crops=dfr['number_of_crops'],is_in_a_cooperative=dfr['is_in_a_cooperative'],
        no_of_agronomist_visits=dfr['no_of_agronomist_visits'],applyLoanAmount=farmer['applyLoanAmount'][0],score=score[0], bin=bin[0])
                        db.session.add(history)
                        db.session.commit()
            return jsonify({"error":False,"message":f'scorecards{added}'})
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

