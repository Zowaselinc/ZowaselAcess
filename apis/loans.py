from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# add loan class
class AddLoan(Resource):	
    def post(self):
        type=request.json['type']
        loan = Loan.query.filter_by(type=type).first()
        if loan:
            message = {"error":True,"message":loanexists}
        if not loan:
            new_data = Loan(
        type=request.json['type'],
        company=request.json['company'],
        repayment_months=request.json['repayment_months'],
        interest_rate_per_annum=request.json['interest_rate_per_annum']
        )
            db.session.add(new_data)
            db.session.commit()
            message = {"error":False,"message":f'loan{added}'}
        return message

# get loan by type
class Loantype(Resource):
    def get(self, type):
        loan = Loan.query.filter_by(type=type).first()
        if loan:
            return {"error":False,"message":f'loan{retrieved}',"data":loan.json()}
        else:
            return {"error":True,"message":loannotfound}
    def delete(self, type):
        loan = Loan.query.filter_by(type=type).first()
        if loan:
            db.session.delete(loan)
            db.session.commit()
            return {"error":False,"message":f'loan{removed}'}
        else:
            return {"error":True,"message":loannotfound}

# get loan by company
class Loancompany(Resource):
    def get(self, company):
        all_loans = Loan.query.filter_by(company=company).all()
        if all_loans:
            all_loans = [farmer.json() for farmer in all_loans]
            return jsonify({"error":False,"message":f'loan{retrieved}',"data": all_loans})
            
        else:
            return {"error":True,"message":companynotfound}
    def delete(self, company):
        loan = Loan.query.filter_by(company=company).first()
        db.session.delete(loan)
        db.session.commit()
        return {"error":False,"message":f'loan{removed}'}

# get all loans
class AllLoans(Resource):
    def get(self):
        all_loans = db.session.query(Loan).all()
        all_loans = [loan.json() for loan in all_loans]
        return jsonify({"error":False,"message":f'loan{retrieved}',"data":all_loans})

# with pagination
class ListLoans(Resource):
    def get(self, limit):
        all_loans = db.session.query(Loan).all()
        all_loans = [loan.json() for loan in all_loans]
        return jsonify(get_paginated_list(
        all_loans, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
