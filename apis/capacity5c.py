from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add multiple capacity tables at once
class AddCapacity5c(Resource):	
    def post(self):
        try:
            farmercapacity = CapacityTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
        howlongbeenfarming=request.json['howlongbeenfarming'],participatedintraining=request.json['participatedintraining'],
        farmingpractice=request.json['farmingpractice'],keepsanimals=request.json['keepsanimals'],
        hascooperative=request.json['hascooperative'],cooperativename=request.json['cooperativename'],
        educationlevel=request.json['educationlevel'])
            farmerpractice = FarmPractice(bvn=request.json['bvn'],mobile=request.json['mobile'],sizeoffarm=request.json['sizeoffarm'],
        farmisrentedorleased=request.json['farmisrentedorleased'],noofyearsleased=request.json['noofyearsleased'],
        usesmachines=request.json['usesmachines'],rotatescrops=request.json['rotatescrops'],
        noOfhectaresproducedyearly=request.json['noOfhectaresproducedyearly'],approxfertilizeruse=request.json['approxfertilizeruse'],
        nooffertlizerapplications=request.json['nooffertlizerapplications'],decisionforspraying=request.json['decisionforspraying'],
        weedcontrolpractice=request.json['weedcontrolpractice'],estimatedincomepercrop=request.json['estimatedincomepercrop'],
        cropthatcansellwell=request.json['cropthatcansellwell'],hasfarmplanorproject=request.json['hasfarmplanorproject'],
        farmprojectinfo=request.json['farmprojectinfo'])
            farmermechanization = MechanizationTable(bvn=request.json['bvn'],mobile=request.json['mobile'],
        machinesused=request.json['machinesused'],machinehashelped=request.json['machinehashelped'],
        advisemachineorlabour=request.json['advisemachineorlabour'],othermachinesneeded=request.json['othermachinesneeded'],
        canacquiremorelands=request.json['canacquiremorelands'],percentcostsaved=request.json['percentcostsaved'])
            farmercultivation = CultivationTable(bvn=request.json['bvn'],mobile=request.json['mobile'],type_of_labor=request.json['type_of_labor'],
        pay_for_labor=request.json['pay_for_labor'],how_many_housechildren_help=request.json['how_many_housechildren_help'],
        season_children_help=request.json['season_children_help'],labor_children_do=request.json['labor_children_do'],
        household_vs_hire_cost=request.json['household_vs_hire_cost'],labor_women_do=request.json['labor_women_do'],
        percent_female_hired=request.json['percent_female_hired'])
            farmerharvest = HarvestTable(bvn=request.json['bvn'],mobile=request.json['mobile'],when_is_harvest_season=request.json['when_is_harvest_season'],
        no_of_hired_workers=request.json['no_of_hired_workers'],no_of_family_workers=request.json['no_of_family_workers'],
        no_of_permanent_workers=request.json['no_of_permanent_workers'],no_hired_constantly=request.json['no_hired_constantly'])
            farmer = CapacityTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmercapacity)
        
            farmer = FarmPractice.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmerpractice)
        
            farmer = MechanizationTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmermechanization)
        
            farmer = CultivationTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmercultivation)
        
            farmer = HarvestTable.query.filter_by(bvn=request.json['bvn']).first()
            if farmer:
                pass
            else:
                db.session.add(farmerharvest)
            db.session.commit()
            return {"error":False,"message":f'capacity{added}'}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}

class AllCapacity5c(Resource):
    def get(self):
        all_farmer1 = CapacityTable.query.all()
        all_farmer1 = [farmer.json() for farmer in all_farmer1]
        all_farmer2 = FarmPractice.query.all()
        all_farmer2 = [farmer.json() for farmer in all_farmer2]
        all_farmer3 = MechanizationTable.query.all()
        all_farmer3 = [farmer.json() for farmer in all_farmer3]
        all_farmer4 = CultivationTable.query.all()
        all_farmer4 = [farmer.json() for farmer in all_farmer4]
        all_farmer5 = HarvestTable.query.all()
        all_farmer5 = [farmer.json() for farmer in all_farmer5]
        return {"error":False,"message":f'capacity{retrieved}',"data":{'capacity':all_farmer1,'practice':all_farmer2,'mechanization':all_farmer3,'cultivation':all_farmer4,'harvest':all_farmer5}}

class Capacity5cbvn(Resource):
    def get(self, bvn):
        farmer1 = CapacityTable.query.filter_by(bvn=bvn).first()
        farmer2 = FarmPractice.query.filter_by(bvn=bvn).first()
        farmer3 = MechanizationTable.query.filter_by(bvn=bvn).first()
        farmer4 = CultivationTable.query.filter_by(bvn=bvn).first()
        farmer5 = HarvestTable.query.filter_by(bvn=bvn).first()
        
        if not farmer1:
            farmer1={"error":True,"message":bvnnotfound}
        else:
            farmer1=farmer1.json()
        if not farmer2:
            farmer2={"error":True,"message":bvnnotfound}
        else:
            farmer2=farmer2.json()
        if not farmer3:
            farmer3={"error":True,"message":bvnnotfound}
        else:
            farmer3=farmer3.json()
        if not farmer4:
            farmer4={"error":True,"message":bvnnotfound}
        else:
            farmer4=farmer4.json()
        if not farmer5:
            farmer5={"error":True,"message":bvnnotfound}
        else:
            farmer5=farmer5.json()
        return {"error":False,"message":f'capacity{retrieved}',"data":{'capacity':farmer1,'practice':farmer2,'mechanization':farmer3,'cultivation':farmer4,'harvest':farmer5}}
        
    def delete(self, bvn):
        farmer1 = CapacityTable.query.filter_by(bvn=bvn).first()
        farmer2 = FarmPractice.query.filter_by(bvn=bvn).first()
        farmer3 = MechanizationTable.query.filter_by(bvn=bvn).first()
        farmer4 = CultivationTable.query.filter_by(bvn=bvn).first()
        farmer5 = HarvestTable.query.filter_by(bvn=bvn).first()
        if farmer1:
            db.session.delete(farmer1)
            db.session.commit()
        if farmer2:
            db.session.delete(farmer2)
            db.session.commit()
        if farmer3:
            db.session.delete(farmer3)
            db.session.commit()
        if farmer4:
            db.session.delete(farmer4)
            db.session.commit()
        if farmer5:
            db.session.delete(farmer5)
            db.session.commit()
        return {"error":False,"message":f'capacity{removed}'}
