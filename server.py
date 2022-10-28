# Import flask and datetime module for showing date and time
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api, abort, reqparse

from flasgger import Swagger
import datetime
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Initializing flask app
app = Flask(__name__)

api = Api(app)

# Placeholder
farmers = []

# KYF DATA (MANDATORY ONLY)
class AddFarmer(Resource):
	def post(self,FirstName,Surname,Telephone,Age,Gender,MaritalStatus,BVN,MeansofID,
	YearofIssue,ExpiryYear,NIN,PermanentAddress,Landmark,Stateoforigin,LGA,Group ):
		farmer = {'FirstName':FirstName,'Surname':Surname,'Telephone':Telephone, 'Age':Age, 'Gender':Gender,
'MaritalStatus':MaritalStatus, 'BVN':BVN,'MeansofID':MeansofID,'YearofIssue':YearofIssue,
'ExpiryYear':ExpiryYear,'NIN':NIN,'PermanentAddress':PermanentAddress,'Landmark':Landmark,'Stateoforigin':Stateoforigin,
'LGA':LGA,'Group':Group}
		farmers.append(farmer)
		return farmer
# BVN
class FarmerBVN(Resource):
	def get(self, BVN):
		for farmer in farmers:
			if farmer['BVN'] == BVN:
				return farmer
		return {'BVN':None},404
	"""
	def delete(self, BVN):
		for ind, farmer in enumerate(farmers):
			if farmer['BVN'] == BVN:
				farmers.pop(ind)
				return {'note':'delete success'}
	"""
class AllFarmers(Resource):
	def get(self):
		return {'farmers':farmers}

addfarmer = api.namespace('addfarmer',description='create new farmer')
addfarmer.add_resource(AddFarmer,'/FirstName=<FirstName>&Surname=<Surname>&Telephone=<int:Telephone>&Age=<int:Age>&Gender=<Gender>&MaritalStatus=<MaritalStatus>&BVN=<int:BVN>&MeansofID=<MeansofID>&YearofIssue=<int:YearofIssue>&ExpiryYear=<int:ExpiryYear>&NIN=<int:NIN>&PermanentAddress=<PermanentAddress>&Landmark=<Landmark>&Stateoforigin=<Stateoforigin>&LGA=<LGA>&Group=<Group>')

farmer = api.namespace('farmer', description='load farmer')
farmer.add_resource(FarmerBVN,'/BVN=<int:BVN>')
farmer.add_resource(AllFarmers,'/all')

# Running app
if __name__ == '__main__':
	app.run(debug=True)
