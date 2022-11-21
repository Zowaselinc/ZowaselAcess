"""empty message

Revision ID: 36ed5685f5a5
Revises: 9870780a65b3
Create Date: 2022-11-09 10:32:33.325791

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '36ed5685f5a5'
down_revision = '9870780a65b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crop')
    op.drop_index('id', table_name='credit_access_table')
    op.drop_table('credit_access_table')
    op.drop_index('id', table_name='credit_history__table')
    op.drop_table('credit_history__table')
    op.drop_index('id', table_name='credit_history_table')
    op.drop_table('credit_history_table')
    op.drop_index('id', table_name='agronomy_services_table')
    op.drop_table('agronomy_services_table')
    op.drop_table('locations')
    op.drop_index('id', table_name='productivity_viability_table')
    op.drop_table('productivity_viability_table')
    op.drop_index('id', table_name='farmer_table')
    op.drop_table('farmer_table')
    op.drop_index('Bvn', table_name='score_card')
    op.drop_index('id', table_name='score_card')
    op.drop_table('score_card')
    op.drop_index('id', table_name='capital_table')
    op.drop_table('capital_table')
    op.drop_table('loans')
    op.drop_index('id', table_name='movement_table')
    op.drop_table('movement_table')
    op.drop_table('loantransfers')
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('product_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('loantransfers',
    sa.Column('transfer_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('loan_name', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('amount', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('to_farmer', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('transfer_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('transfer_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('movement_table',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('from_location', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('to_location', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('movement_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'movement_table', ['id'], unique=False)
    op.create_table('loans',
    sa.Column('loan_id', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('loan_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('capital_table',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Bvn', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('MainIncomeSource', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('OtherIncomeSource', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NoOfIncomeEarners', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HasBankAccount', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('FirstFundingOption', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NeedsALoan', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('PayBackMonths', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HarvestQtyChanged', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('PestExpenseChanged', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'capital_table', ['id'], unique=False)
    op.create_table('score_card',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Bvn', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('age', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('number_of_land', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('owner_caretaker', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('crop', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('intercropping', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('machines', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('estimate_monthly_income', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('years_cultivating', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'score_card', ['id'], unique=False)
    op.create_index('Bvn', 'score_card', ['Bvn'], unique=False)
    op.create_table('farmer_table',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('FirstName', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Surname', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Telephone', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Email', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Age', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Gender', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('MaritalStatus', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Bvn', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('MeansofID', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('YearofIssue', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('ExpiryYear', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Nin', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('PermanentAddress', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Landmark', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Stateoforigin', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Lga', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('Group', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'farmer_table', ['id'], unique=False)
    op.create_table('productivity_viability_table',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Bvn', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CropsCultivated', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('GrowsCrops', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('OilPalmFertilizers', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('CocoaFertilizers', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('FertilizerFrequency', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('PestFungHerbicides', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('StageChemicalApplied', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NoOfOilDrums', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NoOfBagsSesame', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NoOfBagsSoyaBeans', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NoOfBagsMaize', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NoOfBagsSorghum', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NoOfBagsCocoaBeans', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CropTrainedOn', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('WhereWhenWhoTrained', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NoOfTraining', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('PruningFrequency', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('CropBasedProblems', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('TooYoungCrops', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('YoungCropsAndStage', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('CultivationStartdate', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('IsIntensiveFarmingPractised', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('EconomicActivities', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'productivity_viability_table', ['id'], unique=False)
    op.create_table('locations',
    sa.Column('location_id', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('location_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('agronomy_services_table',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Bvn', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('KnowsAgriProcessed', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('AgronomistThatTrainedYou', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CanManageEcosystem', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HowToManageEcosystem', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('IsTrainingBeneficial', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FieldRoutines', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HarvestingChanges', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('IsCropCalendarBeneficial', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CropCalendarBenefits', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('RecordKeepingBenefits', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'agronomy_services_table', ['id'], unique=False)
    op.create_table('credit_history_table',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('HasTakenLoanBefore', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('SourceOfLoan', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('PastLoanAmount', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HowLoanWasRepaid', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('IsReadyToPayInterest', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('CanProvideCollateral', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('WhyNoCollateral', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'credit_history_table', ['id'], unique=False)
    op.create_table('credit_history__table',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('HasTakenLoanBefore', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('SourceOfLoan', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('PastLoanAmount', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HowLoanWasRepaid', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('IsReadyToPayInterest', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('CanProvideCollateral', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('WhyNoCollateral', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'credit_history__table', ['id'], unique=False)
    op.create_table('credit_access_table',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Bvn', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HasServedAsTreasurer', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('DurationAsTreasurer', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('SavesMoneyMonthly', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('SavingsAmount', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HadDifficultyRepaying', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('DifficultLoanAmount', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('DifficultyReason', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NoOfDifficultLoans', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NoOfRepaidLoans', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('NoOfLoansOnTime', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('EstMonthlyIncome', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CostOfCultivation', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FarmProduceExchanged', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NoOfTimesExchanged', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Collateral', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('ApplyLoanAmount', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('YearsOfCultivating', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('AnnualTurnover', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'credit_access_table', ['id'], unique=False)
    op.create_table('crop',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=250), nullable=True),
    sa.Column('phone_number', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('location', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('pack_size', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('pack_price', mysql.VARCHAR(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###