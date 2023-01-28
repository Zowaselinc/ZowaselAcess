from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add living
class AddLivingTable(Resource):	
    def post(self):
        try:
            new_data = LivingTable(bvn=request.json['bvn'],houseowned=request.json['houseowned'],
        stayswithfamily=request.json['stayswithfamily'],relationshipwithowner=request.json['relationshipwithowner'],
        householdeats=request.json['householdeats'],maleunderage=request.json['maleunderage'],
        femaleunderage=request.json['femaleunderage'],childrenunderage=request.json['childrenunderage'],
        maleaboveage=request.json['maleaboveage'],femaleaboveage=request.json['femaleaboveage'],
        childrenaboveage=request.json['childrenaboveage'],liveswith=request.json['liveswith'],ownotherlands=request.json['ownotherlands'],
        standardofliving=request.json['standardofliving'],sourceofwater=request.json['sourceofwater'],
        sourceeverytime=request.json['sourceeverytime'],cookingmethod=request.json['cookingmethod'],
        haveelectricity=request.json['haveelectricity'],powerpayment=request.json['powerpayment'],typeoftoilet=request.json['typeoftoilet'],
        kitchensink=request.json['kitchensink'],hasgroup=request.json['hasgroup'],group=request.json['group'],
        position=request.json['position'],hasaccessedInput=request.json['hasaccessedInput'],input=request.json['input'])
            db.session.add(new_data)
            db.session.commit()
            return {"error":False,"message":f'living{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
# get living by bvn
class Livingbvn(Resource):
    def get(self, bvn):
        farmer = LivingTable.query.filter_by(bvn=bvn).all()
        if farmer:
            return {"error":False,"message":f'living{retrieved}',"data":[farmers.json() for farmers in farmer]}
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = LivingTable.query.filter_by(bvn=bvn).all()
        if farmer:
            for farmers in farmer:
                db.session.delete(farmers)
            db.session.commit()
            return {"error":False,"message":f'living{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}


# get all living
class AllLiving(Resource):
    def get(self):
        all_farmers = LivingTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'living{retrieved}','data': all_farmers})

# with pagination
class ListLiving(Resource):
    def get(self,limit):
        all_farmers = LivingTable.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

