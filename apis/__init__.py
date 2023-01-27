from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)

api = Api(blueprint, title="ZOWASEL FLASK API", version="1.0", description="ZOWASEL FLASK API")
from .loans import *
loans = api.namespace('loan',description='loans')
loans.add_resource(AddLoan,'/add')
loans.add_resource(Loantype,'/type=<type>')
loans.add_resource(Loancompany,'/company=<company>')
loans.add_resource(AllLoans,'/all')
loans.add_resource(ListLoans, '/list/limit=<limit>')
from .farmer import *
farmer = api.namespace('farmer', description='farmer kyf')
farmer.add_resource(AddFarmer,'/add')
farmer.add_resource(Farmerbvn,'/bvn=<bvn>')
farmer.add_resource(Farmertag,'/tag=<tag>')
farmer.add_resource(Farmergroup,'/group=<group>')
farmer.add_resource(AllFarmers,'/all')
farmer.add_resource(ListFarmers, '/list/limit=<limit>')
from .care import *
care = api.namespace('care', description='care')
care.add_resource(AddCareTable,'/add')
care.add_resource(Carebvn,'/bvn=<bvn>')
care.add_resource(AllCare,'/all')
care.add_resource(ListCare, '/list/limit=<limit>')
from .living import *
living = api.namespace('living', description='Living')
living.add_resource(AddLivingTable,'/add')
living.add_resource(Livingbvn,'/bvn=<bvn>')
living.add_resource(AllLiving,'/all')
living.add_resource(ListLiving, '/list/limit=<limit>')
from .planet import *
planet = api.namespace('planet', description='nature of crops and lands')
planet.add_resource(AddPlanet,'/add')
planet.add_resource(Planetbvn,'/bvn=<bvn>')
planet.add_resource(AllPlanet,'/all')
planet.add_resource(ListPlanet, '/list/limit=<limit>')
from .safety import *
safety = api.namespace('safety', description='food safety and quality')
safety.add_resource(AddSafety,'/add')
safety.add_resource(Safetybvn,'/bvn=<bvn>')
safety.add_resource(AllSafety,'/all')
safety.add_resource(ListSafety, '/list/limit=<limit>')
from .capital import *
capital = api.namespace('capital', description='farmer capital')
capital.add_resource(AddCapital,'/add')
capital.add_resource(Capitalbvn,'/bvn=<bvn>')
capital.add_resource(AllCapital,'/all')
capital.add_resource(ListCapital, '/list/limit=<limit>')
from .harvest import *
harvest = api.namespace('harvest', description='farmer harvest')
harvest.add_resource(AddHarvest,'/add')
harvest.add_resource(Harvestbvn,'/bvn=<bvn>')
harvest.add_resource(AllHarvest,'/all')
harvest.add_resource(ListHarvest, '/list/limit=<limit>')
from .agronomy import *
agronomy = api.namespace('agronomy', description='farmer agronomy')
agronomy.add_resource(AddAgronomyServices,'/add')
agronomy.add_resource(Agronomybvn,'/bvn=<bvn>')
agronomy.add_resource(AllAgronomy,'/all')
agronomy.add_resource(ListAgronomy, '/list/limit=<limit>')
from .capacity import *
capacity = api.namespace('capacity', description='farmer capacity')
capacity.add_resource(AddCapacity,'/add')
capacity.add_resource(Capacitybvn,'/bvn=<bvn>')
capacity.add_resource(AllCapacity,'/all')
capacity.add_resource(ListCapacity, '/list/limit=<limit>')
from .farmland import *
farmland = api.namespace('farmland', description='farmland')
farmland.add_resource(AddFarmlandData,'/add')
farmland.add_resource(Farmlandbvn,'/bvn=<bvn>')
farmland.add_resource(AllFarmland,'/all')
farmland.add_resource(ListFarmland, '/list/limit=<limit>')
from .transfer import *
transfer = api.namespace('transfer', description='loan transfers')
transfer.add_resource(AddLoanTransfer,'/add')
transfer.add_resource(Transferbvn,'/bvn=<bvn>')
transfer.add_resource(Transferid,'/id=<id>')
transfer.add_resource(Transfercompany,'/company=<company>')
transfer.add_resource(Transfergroup,'/group=<group>')
transfer.add_resource(Transferstatus,'/status=<status>')
transfer.add_resource(AllTransfer,'/all')
transfer.add_resource(ListTransfer, '/list/limit=<limit>')
transfer.add_resource(AcceptTransferid,'/accept/id=<id>')
transfer.add_resource(UpdateTransferid,'/update/id=<id>')
transfer.add_resource(RejectTransferid,'/reject/id=<id>')
transfer.add_resource(AcceptTransfertag,'/accept/tag=<tag>')
transfer.add_resource(UpdateTransfertag,'/update/tag=<tag>')
transfer.add_resource(RejectTransfertag,'/reject/tag=<tag>')
from .practice import *
practice = api.namespace('practice', description='farm practice')
practice.add_resource(AddFarmPractice,'/add')
practice.add_resource(Practicebvn,'/bvn=<bvn>')
practice.add_resource(AllPractice,'/all')
practice.add_resource(ListPractice, '/list/limit=<limit>')
from .scorecard import *
scorecard = api.namespace('scorecard', description='scorecard')
scorecard.add_resource(AddScoreCard,'/add')
scorecard.add_resource(Scorecardbvn,'/bvn=<bvn>')
scorecard.add_resource(Scorecardid,'/id=<id>')
scorecard.add_resource(AllScorecard,'/all')
scorecard.add_resource(ListScorecard, '/list/limit=<limit>')
from .cropcard import *
cropcard = api.namespace('cropcard', description='cropcard')
cropcard.add_resource(AddCropCard,'/add')
cropcard.add_resource(Cropcardid,'/id=<id>')
cropcard.add_resource(Cropcardbvn,'/bvn=<bvn>')
cropcard.add_resource(Cropcardcrop_name,'/crop_name=<crop_name>')
cropcard.add_resource(AllCropcard,'/all')
cropcard.add_resource(ListCropcard, '/list/limit=<limit>')
from .scoreanalytics import *
scoreanalytics = api.namespace('scoreanalytics', description='scoreanalytics')
scoreanalytics.add_resource(AddScoreAnalytics,'/add')
scoreanalytics.add_resource(ScoreAnalyticsbvn,'/bvn=<bvn>')
scoreanalytics.add_resource(AllScoreAnalytics,'/all')
scoreanalytics.add_resource(ListScoreAnalytics, '/list/limit=<limit>')
from .conditions import *
conditions = api.namespace('conditions', description='conditions')
conditions.add_resource(AddConditions,'/add')
conditions.add_resource(Conditionsbvn,'/bvn=<bvn>')
conditions.add_resource(AllConditions,'/all')
conditions.add_resource(ListConditions, '/list/limit=<limit>')
from .mobiledata import *
mobiledata = api.namespace('mobiledata', description='mobiledata')
mobiledata.add_resource(AddMobileData,'/add')
mobiledata.add_resource(MobileDatabvn,'/bvn=<bvn>')
mobiledata.add_resource(AllMobileData,'/all')
mobiledata.add_resource(ListMobileData, '/list/limit=<limit>')
from .cultivation import *
cultivation = api.namespace('cultivation', description='cultivation')
cultivation.add_resource(AddCultivation,'/add')
cultivation.add_resource(Cultivationbvn,'/bvn=<bvn>')
cultivation.add_resource(AllCultivation,'/all')
cultivation.add_resource(ListCultivation, '/list/limit=<limit>')
from .creditaccess import *
creditaccess = api.namespace('creditaccess', description='credit access')
creditaccess.add_resource(AddCreditAccess,'/add')
creditaccess.add_resource(CreditAccessbvn,'/bvn=<bvn>')
creditaccess.add_resource(AllCreditAccess,'/all')
creditaccess.add_resource(ListCreditAccess, '/list/limit=<limit>')
from .productivity import *
productivity = api.namespace('productivity', description='productivity viability')
productivity.add_resource(AddProductivityViability,'/add')
productivity.add_resource(Productivitybvn,'/bvn=<bvn>')
productivity.add_resource(AllProductivity,'/all')
productivity.add_resource(ListProductivity, '/list/limit=<limit>')
from .credithistory import *
credithistory = api.namespace('credithistory', description='credit history')
credithistory.add_resource(AddCreditHistory,'/add')
credithistory.add_resource(CreditHistorybvn,'/bvn=<bvn>')
credithistory.add_resource(AllCreditHistory,'/all')
credithistory.add_resource(ListCreditHistory, '/list/limit=<limit>')
from .mechanization import *
mechanization = api.namespace('mechanization', description='mechanization')
mechanization.add_resource(AddMechanization,'/add')
mechanization.add_resource(Mechanizationbvn,'/bvn=<bvn>')
mechanization.add_resource(AllMechanization,'/all')
mechanization.add_resource(ListMechanization, '/list/limit=<limit>')
from .psychometrics import *
psychometrics = api.namespace('psychometrics', description='psychometrics')
psychometrics.add_resource(AddPsychometrics,'/add')
psychometrics.add_resource(Psychometricsbvn,'/bvn=<bvn>')
psychometrics.add_resource(AllPsychometrics,'/all')
psychometrics.add_resource(ListPsychometrics, '/list/limit=<limit>')
from .crop_info import *
crop_info = api.namespace('crop_info', description='crop information traceability')
crop_info.add_resource(AddCropInfo,'/add')
crop_info.add_resource(CropInfoTracing,'/tracing_id=<tracing_id>')
crop_info.add_resource(AllCropInfo,'/all')
crop_info.add_resource(ListCropInfo, '/list/limit=<limit>')
from .crop_quality import *
crop_quality = api.namespace('crop_quality', description='crop quality traceability')
crop_quality.add_resource(AddCropQuality,'/add')
crop_quality.add_resource(CropQualityTracing,'/tracing_id=<tracing_id>')
crop_quality.add_resource(AllCropQuality,'/all')
crop_quality.add_resource(ListCropQuality, '/list/limit=<limit>')
from .shipment import *
shipment = api.namespace('shipment', description='shipment traceability')
shipment.add_resource(AddShipment,'/add')
shipment.add_resource(ShipmentTracing,'/tracing_id=<tracing_id>')
shipment.add_resource(AllShipment,'/all')
shipment.add_resource(ListShipment, '/list/limit=<limit>')
from .inputs_info import *
inputs_info = api.namespace('inputs_info', description='inputs_info traceability')
inputs_info.add_resource(AddInputsInfo,'/add')
inputs_info.add_resource(InputsInfoTracing,'/tracing_id=<tracing_id>')
inputs_info.add_resource(AllInputsInfo,'/all')
inputs_info.add_resource(ListInputsInfo, '/list/limit=<limit>')
from .warehouse import *
warehouse = api.namespace('warehouse', description='warehouse traceability')
warehouse.add_resource(AddWarehouse,'/add')
warehouse.add_resource(WarehouseTracing,'/tracing_id=<tracing_id>')
warehouse.add_resource(AllWarehouse,'/all')
warehouse.add_resource(ListWarehouse, '/list/limit=<limit>')
from .recommendation import *
recommendation = api.namespace('recommendation', description='recommendation traceability')
recommendation.add_resource(AddRecommendation,'/add')
recommendation.add_resource(RecommendationTracing,'/tracing_id=<tracing_id>')
recommendation.add_resource(AllRecommendation,'/all')
recommendation.add_resource(ListRecommendation, '/list/limit=<limit>')
from .market import *
buyers_offers = api.namespace('buyers_offers',description='load buyers_offers')
buyers_offers.add_resource(AddBuyersOffers,'/add')
buyers_offers.add_resource(BuyersOffersid,'/id=<id>')
buyers_offers.add_resource(BuyersOfferscrop,'/crop=<crop>')
buyers_offers.add_resource(AllBuyersOffers,'/all')
buyers_offers.add_resource(ListBuyersOffers, '/list/limit=<limit>')
#from .buyers_daily_price import *
buyers_daily_price = api.namespace('daily_price',description='load buyers_daily_price')
buyers_daily_price.add_resource(AddBuyersDailyPrice,'/add')
buyers_daily_price.add_resource(BuyersDailyPriceid,'/id=<id>')
buyers_daily_price.add_resource(BuyersDailyPricecrop,'/crop=<crop>')
buyers_daily_price.add_resource(AllBuyersDailyPrice,'/all')
buyers_daily_price.add_resource(ListBuyersDailyPrice, '/list/limit=<limit>')
#from .farmgate_prices import *
farmgate_prices = api.namespace('farmgate_prices',description='load farmgate_prices')
farmgate_prices.add_resource(AddFarmGatePrices,'/add')
farmgate_prices.add_resource(FarmGatePricesid,'/id=<id>')
farmgate_prices.add_resource(FarmGatePricescrop,'/crop=<crop>')
farmgate_prices.add_resource(AllFarmGatePrices,'/all')
farmgate_prices.add_resource(ListFarmGatePrices, '/list/limit=<limit>')
#from .market_prices import *
market_prices = api.namespace('market_prices',description='load market_prices')
market_prices.add_resource(AddMarketPrices,'/add')
market_prices.add_resource(MarketPricesid,'/id=<id>')
market_prices.add_resource(MarketPricescrop,'/crop=<crop>')
market_prices.add_resource(AllMarketPrices,'/all')
market_prices.add_resource(ListMarketPrices, '/list/limit=<limit>')
from .bulk import *
bulk = api.namespace('bulk', description='bulk files')
bulk.add_resource(AddBulkFarmer,'/farmer')
bulk.add_resource(AddBulkScorecard,'/scorecard')
from .capital5c import *
capital5c = api.namespace('5c_capital', description='farmer 5c_capital')
capital5c.add_resource(AddCapital5c,'/add')
capital5c.add_resource(Capital5cbvn,'/bvn=<bvn>')
capital5c.add_resource(AllCapital5c,'/all')
from .character5c import *
character5c = api.namespace('5c_character', description='farmer 5c_character')
character5c.add_resource(AddCharacter5c,'/add')
character5c.add_resource(Character5cbvn,'/bvn=<bvn>')
character5c.add_resource(AllCharacter5c,'/all')
from .collateral5c import *
collateral5c = api.namespace('5c_collateral', description='farmer 5c_collateral')
collateral5c.add_resource(AddCollateral5c,'/add')
collateral5c.add_resource(Collateral5cbvn,'/bvn=<bvn>')
collateral5c.add_resource(AllCollateral5c,'/all')
from .capacity5c import *
capacity5c = api.namespace('5c_capacity', description='farmer 5c_capacity')
capacity5c.add_resource(AddCapacity5c,'/add')
capacity5c.add_resource(Capacity5cbvn,'/bvn=<bvn>')
capacity5c.add_resource(AllCapacity5c,'/all')
from .conditions5c import *
conditions5c = api.namespace('5c_conditions', description='farmer 5c_conditions')
conditions5c.add_resource(AddConditions5c,'/add')
conditions5c.add_resource(Conditions5cbvn,'/bvn=<bvn>')
conditions5c.add_resource(AllConditions5c,'/all')