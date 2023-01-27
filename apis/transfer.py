from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

from datetime import datetime
from dateutil.relativedelta import relativedelta

# add transfer
class AddLoanTransfer(Resource):	
    def post(self):
        try:
            type = request.json['type']
            bvn=request.json['bvn']
            loan = Loan.query.filter_by(type=type).first()
            if not loan:
                return {"error":True,"message":loannotfound}
            farmer = ScoreCard.query.filter_by(bvn=bvn).first()
            if not farmer:
                if loan:
                    try:
                        amount=request.json['amount']
                    except KeyError:
                        amount=farmer.applyLoanAmount
                    new_data = LoanTransfer(type=type,company=loan.company,
                amount=amount,group='',
                score='',bin='',
                repayment_amount=float(amount)*(((loan.interest_rate_per_annum*(loan.repayment_months/12))+100)/100),
                status='Offered',bvn=bvn,repayment_months=loan.repayment_months,
                repaid = 0, balance = 0,transfer_date='Pending',due_date='Pending')
                    db.session.add(new_data)
                    db.session.commit()
                    return {"error":False,"message":f'loan transfer{added}',"data":new_data.json()}
            if farmer:
                if loan:
                    try:
                        amount=request.json['amount']
                    except KeyError:
                        amount=farmer.applyLoanAmount
                    new_data = LoanTransfer(type=type,company=loan.company,
                amount=amount,group=farmer.is_in_a_cooperative,
                score=farmer.score,bin=farmer.bin,
                repayment_amount=float(amount)*(((loan.interest_rate_per_annum*(loan.repayment_months/12))+100)/100),
                status='Offered',bvn=bvn,repayment_months=loan.repayment_months,
                repaid = 0, balance = 0,transfer_date='Pending',due_date='Pending')
                    db.session.add(new_data)
                    db.session.commit()
                    return {"error":False,"message":f'loan transfer{added}',"data":new_data.json()}
        except KeyError:
            return {"error":True,"message":missingentry}

# get transfer by bvn
class Transferbvn(Resource):
    def get(self, bvn):
        farmer = LoanTransfer.query.filter_by(bvn=bvn).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":f'loan transfer{retrieved}',"data": transfers})
        else:
            return {"error":True,"message":bvnnotfound}
    def delete(self, bvn):
        farmer = LoanTransfer.query.filter_by(bvn=bvn).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{removed}'}
        else:
            return {"error":True,"message":bvnnotfound}
    
# get transfer by id
class Transferid(Resource):
    def get(self, id):
        farmer = LoanTransfer.query.filter_by(id=id).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":f'loan transfer{retrieved}',"data": transfers})
        else:
            return {"error":True,"message":idnotfound}
    def delete(self, id):
        farmer = LoanTransfer.query.filter_by(id=id).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{removed}'}
        else:
            return {"error":True,"message":idnotfound}
# get transfer by tag
class Transfertag(Resource):
    def get(self, tag):
        farmer = LoanTransfer.query.filter_by(tag=tag).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":f'loan transfer{retrieved}',"data": transfers})
        else:
            return {"error":True,"message":tagnotfound}
    def delete(self, tag):
        farmer = LoanTransfer.query.filter_by(tag=tag).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{removed}'}
        else:
            return {"error":True,"message":tagnotfound}
# get transfer by group      
class Transfergroup(Resource):
    def get(self, group):
        farmer = LoanTransfer.query.filter_by(group=group).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":f'loan transfer{retrieved}',"data": transfers})
        else:
            return {"error":True,"message":groupnotfound}
    def delete(self, group):
        farmer = LoanTransfer.query.filter_by(group=group).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{removed}'}
        else:
            return {"error":True,"message":groupnotfound}
# get transfer by company
class Transfercompany(Resource):
    def get(self, company):
        farmer = LoanTransfer.query.filter_by(company=company).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":f'loan transfer{retrieved}',"data": transfers})
        else:
            return {"error":True,"message":companynotfound}
    def delete(self, company):
        farmer = LoanTransfer.query.filter_by(company=company).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{removed}'}
        else:
            return {"error":True,"message":companynotfound}

# get transfer by status
class Transferstatus(Resource):
    def get(self, status):
        farmer = LoanTransfer.query.filter_by(status=status).all()
        if farmer:
            transfers= [transfer.json() for transfer in farmer]
            return jsonify({"error":False,"message":f'loan transfer{retrieved}',"data": transfers})
        else:
            return {"error":True,"message":statusnotfound}
    def delete(self, status):
        farmer = LoanTransfer.query.filter_by(status=status).first()
        if farmer:
            db.session.delete(farmer)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{removed}'}
        else:
            return {"error":True,"message":statusnotfound}
   
# accept offer
class AcceptTransferid(Resource):	
    def get(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            loan.status = 'Accepted'
            loan.balance = loan.repayment_amount
            loan.transfer_date = datetime.now()
            x=int(loan.repayment_months)
            loan.due_date = datetime.now() + relativedelta(months=+x)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{accepted}'}
        else:
            return {"error":True,"message":idnotfound}
    def post(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            loan.status = 'Accepted'
            loan.balance = loan.repayment_amount
            loan.transfer_date = datetime.now()
            x=int(loan.repayment_months)
            loan.due_date = datetime.now() + relativedelta(months=+x)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{accepted}'}
        else:
            return {"error":True,"message":idnotfound}

# reject offer
class RejectTransferid(Resource):	
    def get(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            loan.status = 'Rejected'
            #loan.transfer_date = datetime.now()
            loan.due_date = 'Rejected'
            db.session.commit()
            return {"error":False,"message":f'loan transfer{rejected}'}
        else:
            return {"error":True,"message":idnotfound}
    def post(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            loan.status = 'Rejected'
            #loan.transfer_date = datetime.now()
            loan.due_date = 'Rejected'
            db.session.commit()
            return {"error":False,"message":f'loan transfer{rejected}'}
        else:
            return {"error":True,"message":idnotfound}
# repay loan
class UpdateTransferid(Resource):	
    def get(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            if loan.status == 'Accepted':
                loan.repaid = float(loan.repaid) + float(request.json['amount'])
                loan.balance = float(loan.balance) - float(request.json['amount'])
                loan.repaid = int(loan.repaid)
                loan.balance = int(loan.balance)
                if float(loan.balance)<=0:
                    loan.status = 'Cleared'
                db.session.commit()
                return {"error":False,"message":f'loan transfer{updated}'}
        else:
            return {"error":True,"message":idnotfound}
    def post(self,id):
        loan = LoanTransfer.query.filter_by(id=id).first()
        if loan:
            if loan.status == 'Accepted':
                loan.repaid = float(loan.repaid) + float(request.json['amount'])
                loan.balance = float(loan.balance) - float(request.json['amount'])
                loan.repaid = int(loan.repaid)
                loan.balance = int(loan.balance)
                if float(loan.balance)<=0:
                    loan.status = 'Cleared'
                db.session.commit()
                return {"error":False,"message":f'loan transfer{updated}'}
        else:
            return {"error":True,"message":idnotfound}
# accept transfer with tag
class AcceptTransfertag(Resource):	
    def get(self,tag):
        loan = LoanTransfer.query.filter_by(tag=tag).first()
        if loan:
            loan.status = 'Accepted'
            loan.balance = loan.repayment_amount
            loan.transfer_date = datetime.now()
            x=int(loan.repayment_months)
            loan.due_date = datetime.now() + relativedelta(months=+x)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{accepted}'}
        else:
            return {"error":True,"message":tagnotfound}
    def get(self,tag):
        loan = LoanTransfer.query.filter_by(tag=tag).first()
        if loan:
            loan.status = 'Accepted'
            loan.balance = loan.repayment_amount
            loan.transfer_date = datetime.now()
            x=int(loan.repayment_months)
            loan.due_date = datetime.now() + relativedelta(months=+x)
            db.session.commit()
            return {"error":False,"message":f'loan transfer{accepted}'}
        else:
            return {"error":True,"message":tagnotfound}
# reject transfer with tag
class RejectTransfertag(Resource):	
    def get(self,tag):
        loan = LoanTransfer.query.filter_by(tag=tag).first()
        if loan:
            loan.status = 'Rejected'
            #loan.transfer_date = datetime.now()
            loan.due_date = 'Rejected'
            db.session.commit()
            return {"error":False,"message":f'loan transfer{rejected}'}
        else:
            return {"error":True,"message":tagnotfound}
    def post(self,tag):
        loan = LoanTransfer.query.filter_by(tag=tag).first()
        if loan:
            loan.status = 'Rejected'
            #loan.transfer_date = datetime.now()
            loan.due_date = 'Rejected'
            db.session.commit()
            return {"error":False,"message":f'loan transfer{rejected}'}
        else:
            return {"error":True,"message":tagnotfound}
# repay loan with tag
class UpdateTransfertag(Resource):	
    def get(self,tag):
        loan = LoanTransfer.query.filter_by(tag=tag).first()
        if loan:
            if loan.status == 'Accepted':
                loan.repaid = float(loan.repaid) + float(request.json['amount'])
                loan.balance = float(loan.balance) - float(request.json['amount'])
                loan.repaid = int(loan.repaid)
                loan.balance = int(loan.balance)
                if float(loan.balance)<=0:
                    loan.status = 'Cleared'
                db.session.commit()
                return {"error":False,"message":f'loan transfer{updated}'}
        else:
            return {"error":True,"message":tagnotfound}

    def post(self,tag):
        loan = LoanTransfer.query.filter_by(tag=tag).first()
        if loan:
            if loan.status == 'Accepted':
                loan.repaid = float(loan.repaid) + float(request.json['amount'])
                loan.balance = float(loan.balance) - float(request.json['amount'])
                loan.repaid = int(loan.repaid)
                loan.balance = int(loan.balance)
                if float(loan.balance)<=0:
                    loan.status = 'Cleared'
                db.session.commit()
                return {"error":False,"message":f'loan transfer{updated}'}
        else:
            return {"error":True,"message":tagnotfound}

# get all transfers
class AllTransfer(Resource):
    def get(self):
        all_farmers = LoanTransfer.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify({'error': False,'message': f'loan transfer{retrieved}','data': all_farmers})

# with pagination
class ListTransfer(Resource):
    def get(self,limit):
        all_farmers = LoanTransfer.query.all()
        all_farmers = [farmer.json() for farmer in all_farmers]
        return jsonify(get_paginated_list(
        all_farmers, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

