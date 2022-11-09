# Import flask 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api, fields
from flask_mysqldb import MySQL

from models import app, Crop,FarmerTable,ScoreCard, Product, Loan,Location, MovementTable, CapitalTable,CreditAccessTable,CreditHistoryTable,ProductivityViabilityTable
from models import AgronomyServicesTable, PsychometricsTable, MobileDataTable, FarmlandTable, CapacityTable, FarmPractice, MechanizationTable, CultivationTable, HarvestTable, ConditionsTable
#from flasgger import Swagger
import os
from datetime import datetime
from flask_migrate import Migrate
db= SQLAlchemy()
api = Api(app, title='Zowasel')
Migrate(app,db)

class AddScoreCard(Resource):	
    def post(self):
        card = ScoreCard(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        age=request.form['age'],
        number_of_land=request.form['number_of_land'],
        address=request.form['address'],
        owner_caretaker=request.form['owner_caretaker'],
        crop=request.form['crop'],
        intercropping=request.form['intercropping'],
        machines=request.form['machines'],
        estimate_monthly_income=request.form['estimate_monthly_income'],
        years_cultivating=request.form['years_cultivating'],
        apply_loan_amount = request.form['apply_loan_amount'],
        gender=request.form['gender'],
        owns_a_bank_account=request.form['owns_a_bank_account'],
        size_of_farm=request.form['size_of_farm'],
        grows_more_than_one_crop=request.form['grows_more_than_one_crop'],
        is_in_a_cooperative=request.form['is_in_a_cooperative'],
        no_of_agronomist_visits=request.form['no_of_agronomist_visits'],
        
    )
        db.session.add(card)
        db.session.commit()
        return card.json()
class AllCrops(Resource):
    def get(self):
        crops = db.session.query(Crop).all()
        return jsonify(crops=[crop.to_dict() for crop in crops])


class Crop(Resource):
    def get(self, id):
        crop = Crop.query.get(id)   
        return jsonify(crop=crop.to_dict())
    def delete(self,id):
        crop = Crop.query.get(id)
        if crop:
            db.session.delete(crop)
            db.session.commit()
            return {'Message':'Deleted'}
        else:
            return {'Message':'Error'}

class AddCrop(Resource):
    def post(self):
        new_crop = Crop(
            id = request.form.get("id"),
            name=request.form.get("name"),
            phone_number=request.form.get("phone_number"),
            location=request.form.get("location"),
            pack_size=request.form.get("pack_size"),
            pack_price=request.form.get("pack_price"),
        )

        db.session.add(new_crop)
        db.session.commit()
        return new_crop.json
    


# Add Farmer
class AddFarmer(Resource):
    def post(self):
        new_farmer = FarmerTable(
        id=request.form['Bvn'],
        FirstName=request.form['FirstName'],
        Surname=request.form['Surname'],
        Telephone=request.form['Telephone'],
        Email=request.form['Email'],
        Age=request.form['Age'],
        Gender=request.form['Gender'],
        MaritalStatus=request.form['MaritalStatus'],
        Bvn=request.form['Bvn'],
        MeansofID=request.form['MeansofID'],
        YearofIssue=request.form['YearofIssue'],
        ExpiryYear=request.form['ExpiryYear'],
        Nin=request.form['Nin'],
        PermanentAddress=request.form['PermanentAddress'],
        Landmark=request.form['Landmark'],
        Stateoforigin=request.form['Stateoforigin'],
        Lga=request.form['Lga'],
        Group=request.form['Group']
    )
        db.session.add(new_farmer)
        db.session.commit()
        return new_farmer.json()
class AddCapital(Resource):	
    def post(self):
        capital = CapitalTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        MainIncomeSource=request.form['MainIncomeSource'],
        OtherIncomeSource=request.form['OtherIncomeSource'],
        NoOfIncomeEarners=request.form['NoOfIncomeEarners'],
        HasBankAccount=request.form['HasBankAccount'],
        FirstFundingOption=request.form['FirstFundingOption'],
        NeedsALoan=request.form['NeedsALoan'],
        PayBackMonths=request.form['PayBackMonths'],
        HarvestQtyChanged=request.form['HarvestQtyChanged'],
        PestExpenseChanged=request.form['PestExpenseChanged']
    )
        db.session.add(capital)
        db.session.commit()
        return capital.json()

class AddCreditAccess(Resource):
    def post(self):
        creditaccess = CreditAccessTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        HasServedAsTreasurer=request.form['HasServedAsTreasurer'],
        DurationAsTreasurer=request.form['DurationAsTreasurer'],
        SavesMoneyMonthly=request.form['SavesMoneyMonthly'],
        SavingsAmount=request.form['SavingsAmount'],
        HadDifficultyRepaying=request.form['HadDifficultyRepaying'],
        DifficultLoanAmount=request.form['DifficultLoanAmount'],
        DifficultyReason=request.form['DifficultyReason'],
        NoOfDifficultLoans=request.form['NoOfDifficultLoans'],
        NoOfRepaidLoans=request.form['NoOfRepaidLoans'],
        NoOfLoansOnTime=request.form['NoOfLoansOnTime'],
        EstMonthlyIncome=request.form['EstMonthlyIncome'],
        CostOfCultivation=request.form['CostOfCultivation'],
        FarmProduceExchanged=request.form['FarmProduceExchanged'],
        NoOfTimesExchanged=request.form['NoOfTimesExchanged'],
        Collateral=request.form['Collateral'],
        ApplyLoanAmount=request.form['ApplyLoanAmount'],
        YearsOfCultivating=request.form['Collateral'],
        AnnualTurnover=request.form['AnnualTurnover']
    )
        db.session.commit()
        return creditaccess.json()
class AddCreditHistory(Resource):
    def post(self):
        credithistory = CreditHistoryTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        HasTakenLoanBefore=request.form['HasTakenLoanBefore'],
        SourceOfLoan=request.form['SourceOfLoan'],
        PastLoanAmount=request.form['PastLoanAmount'],
        HowLoanWasRepaid=request.form['HowLoanWasRepaid'],
        IsReadyToPayInterest=request.form['IsReadyToPayInterest'],
        CanProvideCollateral=request.form['CanProvideCollateral'],
        WhyNoCollateral=request.form['WhyNoCollateral']
    )
        db.session.add(credithistory)
        db.session.commit()
        return credithistory.json()

class AddProductivityViability(Resource):
    def post(self):
        productivityviability = ProductivityViabilityTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        CropsCultivated=request.form['CropsCultivated'],
        GrowsCrops=request.form['GrowsCrops'],
        OilPalmFertilizers=request.form['OilPalmFertilizers'],
        CocoaFertilizers=request.form['CocoaFertilizers'],
        FertilizerFrequency=request.form['FertilizerFrequency'],
        PestFungHerbicides=request.form['PestFungHerbicides'],
        StageChemicalApplied=request.form['StageChemicalApplied'],
        NoOfOilDrums=request.form['NoOfOilDrums'],
        NoOfBagsSesame=request.form['NoOfBagsSesame'],
        NoOfBagsSoyaBeans=request.form['NoOfBagsSoyaBeans'],
        NoOfBagsMaize=request.form['NoOfBagsMaize'],
        NoOfBagsSorghum=request.form['NoOfBagsSorghum'],
        NoOfBagsCocoaBeans=request.form['NoOfBagsCocoaBeans'],
        CropTrainedOn=request.form['CropTrainedOn'],
        WhereWhenWhoTrained=request.form['WhereWhenWhoTrained'],
        NoOfTraining=request.form['NoOfTraining'],
        PruningFrequency=request.form['PruningFrequency'],
        CropBasedProblems=request.form['CropBasedProblems'],
        TooYoungCrops=request.form['TooYoungCrops'],
        YoungCropsAndStage=request.form['YoungCropsAndStage'],
        CultivationStartdate=request.form['CultivationStartdate'],
        IsIntensiveFarmingPractised=request.form['IsIntensiveFarmingPractised'],
        EconomicActivities=request.form['EconomicActivities']
    )
        db.session.add(productivityviability)
        db.session.commit()
        return productivityviability.json()

class AddAgronomyServices(Resource):	
    def post(self):
        new_data = AgronomyServicesTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        KnowsAgriProcessed=request.form['KnowsAgriProcessed'],
        AgronomistThatTrainedYou=request.form['AgronomistThatTrainedYou'],
        CanManageEcosystem=request.form['CanManageEcosystem'],
        HowToManageEcosystem=request.form['HowToManageEcosystem'],
        IsTrainingBeneficial=request.form['IsTrainingBeneficial'],
        FieldRoutines=request.form['FieldRoutines'],
        HarvestingChanges=request.form['HarvestingChanges'],
        IsCropCalendarBeneficial=request.form['IsCropCalendarBeneficial'],
        CropCalendarBenefits=request.form['CropCalendarBenefits'],
        RecordKeepingBenefits=request.form['RecordKeepingBenefits']
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()
class AddPsychometrics(Resource):	
    def post(self):
        new_data = PsychometricsTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        FluidIntelligence=request.form['FluidIntelligence'],
        AttitudesandBeliefs=request.form['AttitudesandBeliefs'],
        AgribusinessSkills=request.form['AgribusinessSkills'],
        EthicsandHonesty=request.form['EthicsandHonesty'],
        SavesEnough=request.form['SavesEnough'],
        HasLazyNeighbors=request.form['HasLazyNeighbors'],
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddMobileData(Resource):	
    def post(self):
        new_data = MobileDataTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        MobilePhoneType=request.form['MobilePhoneType'],
        Avweeklyphoneuse=request.form['Avweeklyphoneuse'],
        Callsoutnumber=request.form['Callsoutnumber'],
        Callsoutminutes=request.form['Callsoutminutes'],
        Callsinnumber=request.form['Callsinnumber'],
        Callinminutes=request.form['Callinminutes'],
        SMSsent=request.form['SMSsent'],
        Dataprecedingplanswitch=request.form['Dataprecedingplanswitch'],
        Billpaymenthistory=request.form['Billpaymenthistory'],
        Avweeklydatarefill=request.form['Avweeklydatarefill'],
        NoOfmobileapps=request.form['NoOfmobileapps'],
        AvTimeSpentOnApp=request.form['AvTimeSpentOnApp'],
        MobileAppKinds=request.form['MobileAppKinds'],
        AppDeleteRate=request.form['AppDeleteRate']
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddFarmlandData(Resource):	
    def post(self):
        new_data = FarmlandTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        NoOfFarmlands=request.form['NoOfFarmlands'],
        OwnerOrCaretaker=request.form['OwnerOrCaretaker'],
        FarmOwnerName=request.form['FarmOwnerName'],
        FarmOwnerPhoneNo=request.form['FarmOwnerPhoneNo'],
        RelationshipWithOwner=request.form['RelationshipWithOwner'],
        InheritedFrom=request.form['InheritedFrom'],
        SizeOfFarm=request.form['SizeOfFarm'],
        FarmCoordinates=request.form['FarmCoordinates'],
        FarmAddress=request.form['FarmAddress'],
        KeepsAnimals=request.form['KeepsAnimals'],
        AnimalsFeedOn=request.form['AnimalsFeedOn']
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddCapacity(Resource):	
    def post(self):
        new_data = CapacityTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        HowLongBeenFarming=request.form['HowLongBeenFarming'],
        ParticipatedInTraining=request.form['ParticipatedInTraining'],
        FarmingPractice=request.form['FarmingPractice'],
        KeepsAnimals=request.form['KeepsAnimals'],
        HasCooperative=request.form['HasCooperative'],
        CooperativeName=request.form['CooperativeName'],
        EducationLevel=request.form['EducationLevel']
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddFarmPractice(Resource):	
    def post(self):
        new_data = FarmPractice(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        SizeOfFarm=request.form['SizeOfFarm'],
        FarmIsRentedorLeased=request.form['FarmIsRentedorLeased'],
        NoOfYearsLeased=request.form['NoOfYearsLeased'],
        UsesMachines=request.form['UsesMachines'],
        RotatesCrops=request.form['RotatesCrops'],
        NoOfHectaresProducedYearly=request.form['NoOfHectaresProducedYearly'],
        ApproxFertilizerUse=request.form['ApproxFertilizerUse'],
        NoOfFertlizerApplications=request.form['NoOfFertlizerApplications'],
        DecisionForSpraying=request.form['DecisionForSpraying'],
        WeedControlPractice=request.form['WeedControlPractice'],
        EstimatedIncomePerCrop=request.form['EstimatedIncomePerCrop'],
        CropthatcanSellWell=request.form['CropthatcanSellWell'],
        HasFarmPlanOrProject=request.form['HasFarmPlanOrProject'],
        FarmProjectInfo=request.form['FarmProjectInfo'],
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddMechanization(Resource):	
    def post(self):
        new_data = MechanizationTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        MachinesUsed=request.form['MachinesUsed'],
        MachineHasHelped=request.form['MachineHasHelped'],
        AdviseMachineOrLabour=request.form['AdviseMachineOrLabour'],
        OtherMachinesNeeded=request.form['OtherMachinesNeeded'],
        CanAcquireMoreLands=request.form['CanAcquireMoreLands'],
        PercentCostSaved=request.form['PercentCostSaved'],
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddCultivation(Resource):	
    def post(self):
        new_data = CultivationTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        type_of_labor=request.form['type_of_labor'],
        pay_for_labor=request.form['pay_for_labor'],
        how_many_housechildren_help=request.form['how_many_housechildren_help'],
        season_children_help=request.form['season_children_help'],
        labor_children_do=request.form['labor_children_do'],
        household_vs_hire_cost=request.form['household_vs_hire_cost'],
        labor_women_do=request.form['labor_women_do'],
        percent_female_hired=request.form['percent_female_hired']
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddHarvest(Resource):	
    def post(self):
        new_data = HarvestTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        when_is_harvest_season=request.form['when_is_harvest_season'],
        no_of_hired_workers=request.form['no_of_hired_workers'],
        no_of_family_workers=request.form['no_of_family_workers'],
        no_of_permanent_workers=request.form['no_of_permanent_workers'],
        no_hired_constantly=request.form['no_hired_constantly']
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()

class AddConditions(Resource):	
    def post(self):
        new_data = ConditionsTable(
        id=request.form['Bvn'],
        Bvn=request.form['Bvn'],
        LengthOfHarvestChanged=request.form['LengthOfHarvestChanged']
    )
        db.session.add(new_data)
        db.session.commit()
        return new_data.json()
class FarmerBvn(Resource):
    def get(self, Bvn):
        farmer = FarmerTable.query.filter_by(Bvn=Bvn).first()
        if farmer:
            return farmer.json()
        else:
            return {'Bvn':None},404
    def delete(self, Bvn):
        farmer = FarmerTable.query.filter_by(Bvn=Bvn).first()
        db.session.delete(farmer)
        db.session.commit()
        return {'note':'delete success'}
# All Farmers
class AllFarmers(Resource):
    def get(self):
        all_farmers = FarmerTable.query.all()
        return [farmer.json() for farmer in all_farmers]
class AllBulkFarmer(Resource):
    def post(self):
        farmerslist = request.files.get("file")
        newfarmers = FarmerTable(newfarmers)
        db.session.add_all(newfarmers)
        db.session.commit()


add = api.namespace('add',description='Add New Data')
add.add_resource(AddFarmer,'/farmer')
add.add_resource(AddCrop,'/crop')
add.add_resource(AddScoreCard,'/scorecard')
add.add_resource(AddCapital,'/capital')
add.add_resource(AddCreditAccess,'/creditaccess')
add.add_resource(AddCreditHistory,'/credithistory')
add.add_resource(AddCapacity,'/capacity')
add.add_resource(AddAgronomyServices,'/agronomy')
add.add_resource(AddConditions,'/conditions')
add.add_resource(AddCultivation,'/cultivation')
add.add_resource(AddFarmlandData,'/farmland')
add.add_resource(AddFarmPractice,'/practice')
add.add_resource(AddPsychometrics,'/psychometrics')
add.add_resource(AddMechanization,'/mechanization')
add.add_resource(AddMobileData,'/mobiledata')
add.add_resource(AddHarvest,'/harvest')

farmer = api.namespace('farmer', description='load farmer')
farmer.add_resource(FarmerBvn,'/Bvn=<int:Bvn>')
farmer.add_resource(AllFarmers,'/all')

crops = api.namespace('crop',description='load crops')
crops.add_resource(AllCrops,'/all')
crops.add_resource(Crop,'/<int:id>')

bulk = api.namespace('bulk', description='bulk files')
bulk.add_resource(AllBulkFarmer,'/farmer')

# Running app
if __name__ == '__main__':
    
    app.run(debug=True)
