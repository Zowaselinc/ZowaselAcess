import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# Preprocessing
def preprocess_yearsCultivating(df):
    cleanup={"yearsCultivating":{'Less than 5 years':1,"below-5":1,"1-5":1,
                                 '5 to 10 years':2,"6-10":2,
                                "11-20":3,'10 to 15 years':3,'15 to 20 years':3,
                                "21-30":4,"31-40":4,"41-Above":4,'20 to 25 years':4,'25 years and more':4}}
    df=df.replace(cleanup)
    return(df)
def preprocess_estimateMonthlyIncome(df):
    cleanup={"estimateMonthlyIncome":{"below-50k":1,"50k-100k":1,"100k-250k":1,"250k-500k":1,'Less than 500,000':1,
                                      "500k-1m":2,'500,000 to 1,000,000':2,
                                      "1m-Above":3,'1,000,000 and more':3}}
    df=df.replace(cleanup)
    return(df)
#def preprocess_applyLoanAmount(df):
    #cleanup={"applyLoanAmount":{"below-50k":50,"50k-100k":100,"100k-250k":250,"250k-500k":500,"500k-1m":500,"1m-Above":1000}}
    #df=df.replace(cleanup)
    #return(df)
def preprocess_intercropping(df):
    cleanup={"intercropping":{"No":1,'Mixed cropping':1,
                              "Yes":2,'Intercropping':2}}
    df=df.replace(cleanup)
    return(df)
def preprocess_machines(df):
    cleanup={"machines":{"No":0,"Yes":2}}
    df=df.replace(cleanup)
    return(df)
def preprocess_owner_caretaker(df):
    cleanup={"owner_caretaker":{"Owner":3,
                                "Rental":1,"Lease":1,"Inherited":1,
                                "Caretaker":1}}
    df=df.replace(cleanup)
    return(df)

def preprocess_crop(df):
    cleanup={"crop":{"Cocoa":2,"sesame":2,"Sorghum":1,"Rice":1,'Food crops':1,'Cash crops':2,
                     "Millet":1,'Maize':1,'Tomato':1,'Oil Palm':2, 'Cassava':1}}
    df=df.replace(cleanup)
    crop=[1,2]
    for x in crop:
            df['crop'+str(x)]=(df.crop==x).astype('int')
    df.drop('crop',axis=1,inplace=True)
    return df

def preprocess_age(df):
    cleanup={"age":{"25-34":2,"25 or less":1,"35 to 45":3,"45 or more":4,'45-54':4,'65-Above':4,
                     "35-44":3,'55-64':4}}
    age=[1,2,3,4]
    for x in age:
            df['age'+str(x)]=(df.age==x).astype('int')
    df.drop('age',axis=1,inplace=True)
    return df
def preprocess_numberOfLand(df):
    df.numberOfLand[df.numberOfLand=='6-Above']=6
    df.numberOfLand[df.numberOfLand=='Less than 3 farms']=2
    df.numberOfLand[df.numberOfLand=='More than 3 farms']=3
    df.numberOfLand=df.numberOfLand.astype('int')
    df.numberOfLand=((df.numberOfLand>=3).astype('int'))+1
    return df

def preprocess_df(df):
    # Generate your features here!!!
    df.applyLoanAmount=df.applyLoanAmount.astype('int')
    df=preprocess_numberOfLand(df)
    df=preprocess_intercropping(preprocess_yearsCultivating(df))
    df=preprocess_machines(preprocess_estimateMonthlyIncome(df))
    df=preprocess_owner_caretaker(df)
    df=preprocess_crop(df)
    df=preprocess_age(df)
    return df
def bin_target(y):
    score_cardbin = np.concatenate(([0], [0.5,0.9,0.98], [1]))
    y = pd.cut(y,score_cardbin,labels=['D - Low Probability of Repayment','C - Average Probability of Repayment','B - Good Probability of Repayment','A - Highest Probability of Repayment'])
    return y
