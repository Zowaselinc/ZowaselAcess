from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *
import pickle
from io import StringIO
import pandas as pd
from modelExample import preprocess_df, bin_target
model = pickle.load(open('modelExample.pkl','rb'))



# add bulk farmers
class AddBulkFarmerKyf(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("kyf_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
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
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = ScoreCard.query.filter_by(bvn=dfr['bvn']).all()
                    if not farmer:
                        farmer = ScoreCard.query.filter_by(mobile=dfr['mobile']).all()
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        farmer = pd.DataFrame([['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits']],columns=['bvn','age','number_of_land','address','owner_caretaker','crop','intercropping', 'machines',
        'estimate_monthly_income','years_cultivating','gender','owns_a_bank_account','size_of_farm','number_of_crops','is_in_a_cooperative',
        'no_of_agronomist_visits'])
                        for col in farmer.columns:
                            farmer[col] = dfr[col]
                        farmer['applyLoanAmount'] = applyLoanMobile(dfr['mobile'])
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
                        history = ScoreCard(bvn=dfr['bvn'],mobile=dfr['mobile'],age=dfr['age'],number_of_land=dfr['number_of_land'],address=dfr['address'],
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

# add bulk agronomy
class AddBulkFarmerAgronomy(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("agronomy_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = AgronomyServicesTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = AgronomyServicesTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
        knowsagriprocessed=dfr['knowsagriprocessed'],agronomistthattrainedyou=dfr['agronomistthattrainedyou'],
        canmanageecosystem=dfr['canmanageecosystem'],howtomanageecosystem=dfr['howtomanageecosystem'],
        istrainingbeneficial=dfr['istrainingbeneficial'],fieldroutines=dfr['fieldroutines'],
        harvestingchanges=dfr['harvestingchanges'],iscropcalendarbeneficial=dfr['iscropcalendarbeneficial'],
        cropcalendarbenefits=dfr['cropcalendarbenefits'],recordkeepingbenefits=dfr['recordkeepingbenefits'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerCapacityTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("capacity_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = CapacityTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = CapacityTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
        howlongbeenfarming=dfr['howlongbeenfarming'],participatedintraining=dfr['participatedintraining'],
        farmingpractice=dfr['farmingpractice'],keepsanimals=dfr['keepsanimals'],
        hascooperative=dfr['hascooperative'],cooperativename=dfr['cooperativename'],
        educationlevel=dfr['educationlevel'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

    
# add bulk farmers
class AddBulkFarmerCapitalTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("capital_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = CapitalTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = CapitalTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        mainincomesource=dfr['mainincomesource'],
        otherincomesource=dfr['otherincomesource'],noofincomeearners=dfr['noofincomeearners'],
        hasbankaccount=dfr['hasbankaccount'],firstfundingoption=dfr['firstfundingoption'],
        needsaloan=dfr['needsaloan'],paybackmonths=dfr['paybackmonths'],
        harvestqtychanged=dfr['harvestqtychanged'],pestexpensechanged=dfr['pestexpensechanged'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerCareTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("care_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = CareTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = CareTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        healthcentloc=dfr['healthcentloc'],
        healthcentcount=dfr['healthcentcount'],healthcentdistance=dfr['healthcentdistance'],
        healthcentfunctional=dfr['healthcentfunctional'],affordable=dfr['affordable'],
        farmdistance=dfr['farmdistance'],injuryevent=dfr['injuryevent'],firstaid=dfr['firstaid'],
        lastcheck=dfr['lastcheck'],inschool=dfr['inschool'],level=dfr['level'],
        schoolcount=dfr['schoolcount'],schoolfunctional=dfr['schoolfunctional'],
        qualification=dfr['qualification'],studytime=dfr['studytime'],
        studywhere=dfr['studywhere'],altIncomesource=dfr['altIncomesource'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerConditionsTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("conditions_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = ConditionsTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = ConditionsTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        duration=dfr['duration'],
        seller=dfr['seller'],seller_mou=dfr['seller_mou'],cropyieldprediction=0,
        cropexpectedmarketvalue=0,zowaselmarketplacepriceoffers=0)
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  
# add bulk farmers
class AddBulkFarmerCreditAccessTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("creditaccess_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = CreditAccessTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = CreditAccessTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
        hasservedastreasurer=dfr['hasservedastreasurer'],durationastreasurer=dfr['durationastreasurer'],
        savesmoneymonthly=dfr['savesmoneymonthly'],savingsamount=dfr['savingsamount'],
        haddifficultyrepaying=dfr['haddifficultyrepaying'],difficultloanamount=dfr['difficultloanamount'],
        difficultyreason=dfr['difficultyreason'],noofdifficultloans=dfr['noofdifficultloans'],
        noofrepaidloans=dfr['noofrepaidloans'],noofloansontime=dfr['noofloansontime'],
        estmonthlyincome=dfr['estmonthlyincome'],costofcultivation=dfr['costofcultivation'],
        farmproduceexchanged=dfr['farmproduceexchanged'],nooftimesexchanged=dfr['nooftimesexchanged'],
        collateral=dfr['collateral'],applyloanamount=dfr['applyloanamount'],
        yearsofcultivating=dfr['collateral'],annualturnover=dfr['annualturnover'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerCreditHistoryTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("credithistory_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = CreditHistoryTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = CreditHistoryTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
        hastakenloanbefore=dfr['hastakenloanbefore'],sourceofloan=dfr['sourceofloan'],
        pastloanamount=dfr['pastloanamount'],howloanwasrepaid=dfr['howloanwasrepaid'],
        isreadytopayinterest=dfr['isreadytopayinterest'],canprovidecollateral=dfr['canprovidecollateral'],
        whynocollateral=dfr['whynocollateral'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

    
# add bulk farmers
class AddBulkFarmerCultivationTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("cultivation_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = CultivationTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = CultivationTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        type_of_labor=dfr['type_of_labor'],
        pay_for_labor=dfr['pay_for_labor'],how_many_housechildren_help=dfr['how_many_housechildren_help'],
        season_children_help=dfr['season_children_help'],labor_children_do=dfr['labor_children_do'],
        household_vs_hire_cost=dfr['household_vs_hire_cost'],labor_women_do=dfr['labor_women_do'],
        percent_female_hired=dfr['percent_female_hired'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerFarmlandTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("farmland_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = FarmlandTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = FarmlandTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        nooffarmlands=dfr['nooffarmlands'],
        ownerorcaretaker=dfr['ownerorcaretaker'],farmownername=dfr['farmownername'],
        farmownerphoneno=dfr['farmownerphoneno'],relationshipwithowner=dfr['relationshipwithowner'],
        inheritedfrom=dfr['inheritedfrom'],sizeoffarm=dfr['sizeoffarm'],
        farmcoordinates=dfr['farmcoordinates'],farmaddress=dfr['farmaddress'],
        keepsanimals=dfr['keepsanimals'],animalsfeedon=dfr['animalsfeedon'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  
# add bulk farmers
class AddBulkFarmerHarvestTable(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("harvest_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = HarvestTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = HarvestTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        when_is_harvest_season=dfr['when_is_harvest_season'],
        no_of_hired_workers=dfr['no_of_hired_workers'],no_of_family_workers=dfr['no_of_family_workers'],
        no_of_permanent_workers=dfr['no_of_permanent_workers'],no_hired_constantly=dfr['no_hired_constantly'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerLiving(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("living_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = LivingTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = LivingTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        houseowned=dfr['houseowned'],
        stayswithfamily=dfr['stayswithfamily'],relationshipwithowner=dfr['relationshipwithowner'],
        householdeats=dfr['householdeats'],maleunderage=dfr['maleunderage'],
        femaleunderage=dfr['femaleunderage'],childrenunderage=dfr['childrenunderage'],
        maleaboveage=dfr['maleaboveage'],femaleaboveage=dfr['femaleaboveage'],
        childrenaboveage=dfr['childrenaboveage'],liveswith=dfr['liveswith'],ownotherlands=dfr['ownotherlands'],
        standardofliving=dfr['standardofliving'],sourceofwater=dfr['sourceofwater'],
        sourceeverytime=dfr['sourceeverytime'],cookingmethod=dfr['cookingmethod'],
        haveelectricity=dfr['haveelectricity'],powerpayment=dfr['powerpayment'],typeoftoilet=dfr['typeoftoilet'],
        kitchensink=dfr['kitchensink'],hasgroup=dfr['hasgroup'],group=dfr['group'],
        position=dfr['position'],hasaccessedInput=dfr['hasaccessedInput'],input=dfr['input'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

    
# add bulk farmers
class AddBulkFarmerMechanization(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("mechanization_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = MechanizationTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = MechanizationTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
        machinesused=dfr['machinesused'],machinehashelped=dfr['machinehashelped'],
        advisemachineorlabour=dfr['advisemachineorlabour'],othermachinesneeded=dfr['othermachinesneeded'],
        canacquiremorelands=dfr['canacquiremorelands'],percentcostsaved=dfr['percentcostsaved'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerMobileData(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("mobiledata_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = MobileDataTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = MobileDataTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        mobilephonetype=dfr['mobilephonetype'],
        avweeklyphoneuse=dfr['avweeklyphoneuse'],callsoutnumber=dfr['callsoutnumber'],
        callsoutminutes=dfr['callsoutminutes'],callsinnumber=dfr['callsinnumber'],
        callinminutes=dfr['callinminutes'],smssent=dfr['smssent'],
        dataprecedingplanswitch=dfr['dataprecedingplanswitch'],billpaymenthistory=dfr['billpaymenthistory'],
        avweeklydatarefill=dfr['avweeklydatarefill'],noOfmobileapps=dfr['noOfmobileapps'],
        avtimespentonapp=dfr['avtimespentonapp'],mobileappkinds=dfr['mobileappkinds'],
        appdeleterate=dfr['appdeleterate'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  
# add bulk farmers
class AddBulkFarmerPlanet(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("planet_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = Planet.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = Planet(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        plantoexpand=dfr['plantoexpand'],crop=dfr['crop'],
        variety=dfr['variety'],raiseorbuy=dfr['raiseorbuy'],buywhere=dfr['buywhere'],
        seedlingprice=dfr['seedlingprice'],qtybought=dfr['qtybought'],degradedland=dfr['degradedland'],
        croprotation=dfr['croprotation'],season=dfr['season'],disaster=dfr['disaster'],
        burning=dfr['burning'],mill=dfr['mill'],energysource=dfr['energysource'],replacedtree=dfr['replacedtree'],
        placement=dfr['placement'],sourceofwater=dfr['sourceofwater'],covercrops=dfr['covercrops'],
        intercrop=dfr['intercrop'],cropintercropped=dfr['cropintercropped'],wastemgt=dfr['wastemgt'],
        wastedisposal=dfr['wastedisposal'],recyclewaste=dfr['recyclewaste'],suffered=dfr['suffered'],
        whensuffered=dfr['whensuffered'],greywater=dfr['greywater'],recyclegreywater=dfr['recyclegreywater'],
        pollution=dfr['pollution'],pollutionfreq=dfr['pollutionfreq'],measures=dfr['measures'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerFarmPractice(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("practice_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = FarmPractice.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = FarmPractice(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        sizeoffarm=dfr['sizeoffarm'],
        farmisrentedorleased=dfr['farmisrentedorleased'],noofyearsleased=dfr['noofyearsleased'],
        usesmachines=dfr['usesmachines'],rotatescrops=dfr['rotatescrops'],
        noOfhectaresproducedyearly=dfr['noOfhectaresproducedyearly'],approxfertilizeruse=dfr['approxfertilizeruse'],
        nooffertlizerapplications=dfr['nooffertlizerapplications'],decisionforspraying=dfr['decisionforspraying'],
        weedcontrolpractice=dfr['weedcontrolpractice'],estimatedincomepercrop=dfr['estimatedincomepercrop'],
        cropthatcansellwell=dfr['cropthatcansellwell'],hasfarmplanorproject=dfr['hasfarmplanorproject'],
        farmprojectinfo=dfr['farmprojectinfo'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

    
# add bulk farmers
class AddBulkFarmerProductivity(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("productivity_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = ProductivityViabilityTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = ProductivityViabilityTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
        cropscultivated=dfr['cropscultivated'],growscrops=dfr['growscrops'],
        oilpalmfertilizers=dfr['oilpalmfertilizers'],cocoafertilizers=dfr['cocoafertilizers'],
        fertilizerfrequency=dfr['fertilizerfrequency'],pestfungherbicides=dfr['pestfungherbicides'],
        stagechemicalapplied=dfr['stagechemicalapplied'],noofoildrums=dfr['noofoildrums'],
        noofbagssesame=dfr['noofbagssesame'],noofbagssoyabeans=dfr['noofbagssoyabeans'],
        noofbagsmaize=dfr['noofbagsmaize'],noofbagssorghum=dfr['noofbagssorghum'],
        noofbagscocoabeans=dfr['noofbagscocoabeans'],croptrainedon=dfr['croptrainedon'],
        wherewhenwhotrained=dfr['wherewhenwhotrained'],nooftraining=dfr['nooftraining'],
        pruningfrequency=dfr['pruningfrequency'],cropbasedproblems=dfr['cropbasedproblems'],
        tooyoungcrops=dfr['tooyoungcrops'],youngcropsandstage=dfr['youngcropsandstage'],
        cultivationstartdate=dfr['cultivationstartdate'],isintensivefarmingpractised=dfr['isintensivefarmingpractised'],
        economicactivities=dfr['economicactivities'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers
class AddBulkFarmerPsychometrics(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("psychometrics_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = PsychometricsTable.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = PsychometricsTable(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        fluidintelligence=dfr['fluidintelligence'],
        attitudesandbeliefs=dfr['attitudesandbeliefs'],agribusinessskills=dfr['agribusinessskills'],
        ethicsandhonesty=dfr['ethicsandhonesty'],savesenough=dfr['savesenough'],
        haslazyneighbors=dfr['haslazyneighbors'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  
# add bulk farmers
class AddBulkFarmerSafety(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("safety_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = Safety.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = Safety(bvn=dfr['bvn'],mobile=dfr['mobile'],ferment=dfr['ferment'],
        fermentdays=dfr['fermentdays'],fermentreason=dfr['fermentreason'],brokenqty=dfr['brokenqty'],
        dowithbroken=dfr['dowithbroken'],unripeqty=dfr['unripeqty'],dowithunripe=dfr['dowithunripe'],
        cocoastore=dfr['cocoastore'],ffbstore=dfr['ffbstore'],herbicide=dfr['herbicide'],
        herbicidestore=dfr['herbicidestore'],agrochemsource=dfr['agrochemsource'],harvesttool=dfr['harvesttool'],
        wear=dfr['wear'],disposal=dfr['disposal'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

# add bulk farmers Farmer
class AddBulkFarmerScoreAnalytics(Resource):
    def post(self):
        try:
            csv_raw = request.files.get("analysis_file").read().decode("utf-8")
            csv = StringIO(csv_raw)
            df = pd.read_csv(csv)
            if len(df)>0:
                for r in range(len(df)):
                    dfr = df.iloc[r,:]
                    farmer = ScoreAnalytics.query.filter_by(bvn=dfr['bvn'])
                    if ((not farmer) or (pd.isna(dfr['bvn']))):
                        dfr = dfr.astype(str)
                        farmerkyf = ScoreAnalytics(bvn=dfr['bvn'],mobile=dfr['mobile'],
                        scores=dfr['scores'],
        conditions=dfr['conditions'],capital=dfr['capital'],collateral=dfr['collateral'],
        capacity=dfr['capacity'],character=dfr['character'])
                        db.session.add(farmerkyf)
                        db.session.commit()
                    return {"error":False,"message":f'farmers{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  

