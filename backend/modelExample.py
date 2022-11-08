import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# Preprocessing
def preprocess_yearsCultivating(df):
    cleanup={"years_cultivating":{"below-5":1,"6-10":10,"11-20":20,"21-30":30,"31-40":40,"41-Above":50}}
    df=df.replace(cleanup)
    return(df)
def preprocess_estimateMonthlyIncome(df):
    cleanup={"estimate_monthly_income":{"below-50k":50,"50k-100k":100,"100k-250k":250,"250k-500k":500,"500k-1m":500,"1m-Above":1000}}
    df=df.replace(cleanup)
    return(df)
def preprocess_applyLoanAmount(df):
    cleanup={"apply_loan_amount":{"below-50k":50,"50k-100k":100,"100k-250k":250,"250k-500k":500,"500k-1m":500,"1m-Above":1000}}
    df=df.replace(cleanup)
    return(df)
def preprocess_intercropping(df):
    cleanup={"intercropping":{"No":0,"Yes":1}}
    df=df.replace(cleanup)
    return(df)
def preprocess_machines(df):
    cleanup={"machines":{"No":0,"Yes":1}}
    df=df.replace(cleanup)
    return(df)
def preprocess_owner_caretaker(df):
    cleanup={"owner_caretaker":{"Owner":0,"Inherited":1,"Caretaker":2}}
    df=df.replace(cleanup)
    return(df)
crop=['Cocoa', 'sesame', 'Sorghum', 'Rice', 'Millet', 'Maize', 'Tomato','Oil Palm', 'Cassava']
def preprocess_crop(df):
    for x in crop:
            df[x]=(df.crop==x).astype('int')
    df.drop('crop',axis=1,inplace=True)
    return df
age=['55-64', '35-44', '65-Above', '45-54', '25-34']
def preprocess_age(df):
    for x in age:
            df[x]=(df.age==x).astype('int')
    df.drop('age',axis=1,inplace=True)
    return df

address=['Bamikemo', 'taura', 'majia', 'Akasan gidan kuka',
       'Ibadan', 'wasai', 'garki', 'Gurjawa Kwalam', 'Kwatau Pampaida',
       'Ofatura']
def preprocess_address(df):
    for x in address:
            df[x]=(df.address==x).astype('int')
    df.drop('address',axis=1,inplace=True)
    return df


def preprocess_df(df):
    # Generate your features here!!!
    df.number_of_land[df.number_of_land=='6-Above']=6
    df.number_of_land=df.number_of_land.astype('int')
    df=preprocess_intercropping(preprocess_yearsCultivating(df))
    df=preprocess_machines(preprocess_estimateMonthlyIncome(df))
    df=preprocess_owner_caretaker(preprocess_applyLoanAmount(df))
    df=preprocess_crop(df)
    df=preprocess_age(df)
    df=preprocess_address(df)
    return df
def bin_target(y):
    score_cardbin = np.concatenate(([0], [0.5,0.9,0.98], [1]))
    y = pd.cut(y,score_cardbin,labels=['D - Low Probability of Repayment','C - Average Probability of Repayment','B - Good Probability of Repayment','A - Highest Probability of Repayment'])
    return y
