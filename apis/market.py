from constants import *
from flask_restx import Resource
from flask import jsonify, request
from models import *

# buyers daily price
class AddBuyersDailyPrice(Resource):	
    def post(self):
        try:
            new_data = BuyersDailyPrice(
        crop=request.json['crop'],
        location=request.json['location'],
        classification=request.json['classification'],
        min_price=request.json['min_price'],
        max_price=request.json['max_price'],
        ave_price=request.json['ave_price'],
        quality_spec=request.json['quality_spec'],
        date_filled=request.json['date_filled']
        )
            db.session.add(new_data)
            db.session.commit()
            message = {"error":False,"message":f'price{added}'}
            return message
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
# add buyers offers
class AddBuyersOffers(Resource):	
    def post(self):
        try:
            new_data = BuyersOffers(
        crop=request.json['crop'],
        location=request.json['location'],
        classification=request.json['classification'],
        min_price=request.json['min_price'],
        max_price=request.json['max_price'],
        ave_price=request.json['ave_price'],
        quality_spec=request.json['quality_spec'],
        date_filled=request.json['date_filled']
        )
            db.session.add(new_data)
            db.session.commit()
            message = {"error":False,"message":f'price{added}'}
            return message 
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}  
# add farmgate prices
class AddFarmGatePrices(Resource):	
    def post(self):
        try:
            new_data = FarmGatePrices(
        crop=request.json['crop'],
        location=request.json['location'],
        classification=request.json['classification'],
        min_price=request.json['min_price'],
        max_price=request.json['max_price'],
        ave_price=request.json['ave_price'],
        quality_spec=request.json['quality_spec'],
        date_filled=request.json['date_filled']
        )
            db.session.add(new_data)
            db.session.commit()
            message = {"error":False,"message":f'price{added}'}
            return message  
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
# add marketprices
class AddMarketPrices(Resource):	
    def post(self):
        try:
            new_data = MarketPrices(
        crop=request.json['crop'],
        location=request.json['location'],
        classification=request.json['classification'],
        min_price=request.json['min_price'],
        max_price=request.json['max_price'],
        ave_price=request.json['ave_price'],
        quality_spec=request.json['quality_spec'],
        date_filled=request.json['date_filled']
        )
            db.session.add(new_data)
            db.session.commit()
            message = {"error":False,"message":f'price{added}'}
            return message  
        except KeyError:
            return {"error":True,"message":missingentry}
        except AssertionError:
            return {"error":True,"message":invalidinput}
        except Exception as e:
            return {"error":True,"message":e.__doc__}
# get buyers daily price by id  
class BuyersDailyPriceid(Resource):
    def get(self, id):
        price = BuyersDailyPrice.query.filter_by(id=id).first()
        if price:
            return jsonify({"error":False,"message":f'price{retrieved}',"data": price})
        else:
            return {"error":True,"message":idnotfound}
    def delete(self, id):
        price = BuyersDailyPrice.query.filter_by(id=id).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":f'price{removed}'}
# get buyers offers by id
class BuyersOffersid(Resource):
    def get(self, id):
        price = BuyersOffers.query.filter_by(id=id).first()
        if price:
            return jsonify({"error":False,"message":f'price{retrieved}',"data": price})
        else:
            return {"error":True,"message":idnotfound}
    def delete(self, id):
        price = BuyersOffers.query.filter_by(id=id).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":f'price{removed}'}
# get farmgate prices by id
class FarmGatePricesid(Resource):
    def get(self, id):
        price = FarmGatePrices.query.filter_by(id=id).first()
        if price:
            return jsonify({"error":False,"message":f'price{retrieved}',"data": price})
        else:
            return {"error":True,"message":idnotfound}
    def delete(self, id):
        price = FarmGatePrices.query.filter_by(id=id).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":f'price{removed}'}
# get market prices by id
class MarketPricesid(Resource):
    def get(self, id):
        price = MarketPrices.query.filter_by(id=id).first()
        if price:
            return jsonify({"error":False,"message":f'price{retrieved}',"data": price})
        else:
            return {"error":True,"message":idnotfound}
    def delete(self, id):
        price = MarketPrices.query.filter_by(id=id).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":f'price{removed}'}

# get buyers daily price by crop
class BuyersDailyPricecrop(Resource):
    def get(self, crop):
        price = BuyersDailyPrice.query.filter_by(crop=crop).all()
        if price:
            all_prices = [prices.json() for prices in price]
            return jsonify({"error":False,"message":f'price{retrieved}',"data": all_prices})
        else:
            return {"error":True,"message":cropnotfound}
    def delete(self, crop):
        price = BuyersDailyPrice.query.filter_by(crop=crop).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":f'price{removed}'}

# get buyers offers by crop
class BuyersOfferscrop(Resource):
    def get(self, crop):
        price = BuyersOffers.query.filter_by(crop=crop).all()
        if price:
            all_prices = [prices.json() for prices in price]
            return jsonify({"error":False,"message":f'price{retrieved}',"data": all_prices})
        else:
            return {"error":True,"message":cropnotfound}
    def delete(self, crop):
        price = BuyersOffers.query.filter_by(crop=crop).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":f'price{removed}'}

# get farmgate prices by crop
class FarmGatePricescrop(Resource):
    def get(self, crop):
        price = FarmGatePrices.query.filter_by(crop=crop).all()
        if price:
            all_prices = [prices.json() for prices in price]
            return jsonify({"error":False,"message":f'price{added}',"data":all_prices})
        else:
            return {"error":True,"message":cropnotfound}
    def delete(self, crop):
        price = FarmGatePrices.query.filter_by(crop=crop).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":f'price{removed}'}

# get market prices by crop
class MarketPricescrop(Resource):
    def get(self, crop):
        price = MarketPrices.query.filter_by(crop=crop).all()
        if price:
            all_prices = [prices.json() for prices in price]
            return jsonify({"error":False,"message":added,"data": all_prices})
        else:
            return {"error":True,"message":cropnotfound}
    def delete(self, crop):
        price = MarketPrices.query.filter_by(crop=crop).first()
        db.session.delete(price)
        db.session.commit()
        return {"error":False,"message":f'price{removed}'}

# get all buyers daily price
class AllBuyersDailyPrice(Resource):
    def get(self):
        price = BuyersDailyPrice.query.all() 
        price = [prices.json() for prices in price]
        return jsonify({"error":False,"message":f'price{retrieved}',"data": price})

# get all buyers offers
class AllBuyersOffers(Resource):
    def get(self):
        price = BuyersOffers.query.all() 
        price = [prices.json() for prices in price]
        return jsonify({"error":False,"message":f'price{retrieved}',"data": price})

# get all farmgate prices
class AllFarmGatePrices(Resource):
    def get(self):
        price = FarmGatePrices.query.all() 
        price = [prices.json() for prices in price]
        return jsonify({"error":False,"message":f'price{retrieved}',"data": price})

# get all market prices
class AllMarketPrices(Resource):
    def get(self):
        price = MarketPrices.query.all() 
        price = [prices.json() for prices in price]
        return jsonify({"error":False,"message":f'price{retrieved}',"data": price})
        

# with pagination
class ListBuyersDailyPrice(Resource):
    def get(self, limit):
        price = BuyersDailyPrice.query.all() 
        price = [prices.json() for prices in price]
        return jsonify(get_paginated_list(
        price, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

class ListBuyersOffers(Resource):
    def get(self,limit):
        price = BuyersOffers.query.all() 
        price = [prices.json() for prices in price]
        return jsonify(get_paginated_list(
        price, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))

class ListFarmGatePrices(Resource):
    def get(self,limit):
        price = FarmGatePrices.query.all() 
        price = [prices.json() for prices in price]
        return jsonify(get_paginated_list(
        price, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
class ListMarketPrices(Resource):
    def get(self,limit):
        price = MarketPrices.query.all() 
        price = [prices.json() for prices in price]
        return jsonify(get_paginated_list(
        price, 
        '/list', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', limit)
    ))
        