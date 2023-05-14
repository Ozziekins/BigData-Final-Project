from alsmodel import loadModel as loadALSModel, predictItems, predictUsers, train as ALSTrain
from BRPLKNN import findNearestNeighbour, load_model as loadBRPModel, train as BRPtrain
from regressionmodel import predictRatings, loadModel as loadRegressorModel, train as Regressortrain
from DataService import DataService
from SparkService import SparkService
from pyspark.sql.types import StructType,StructField, IntegerType
from pyspark.ml.feature import VectorAssembler


class ModelService:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ModelService, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.als = loadALSModel()
        self.brpModel, self.brpPipeline = loadBRPModel()
        self.lrModel = loadRegressorModel()
        
    def retrainALS(self):
        dataService = DataService()
        train_df, test_df = dataService.review.randomSplit([0.8, 0.2], 42)
        self.als = ALSTrain(train_df)    
    
    def retrainBRP(self):
        dataService = DataService()
        beer = dataService.beer.na.drop()
        agg_dataset = beer.join(dataService.brewer,beer.brewerid ==  dataService.brewer.id,"inner")
        train_df, test_df = agg_dataset.randomSplit([0.8, 0.2], 42)
        self.brpPipeline, self.brpModel = BRPtrain(train_df)

    def retrainRegressor(self):
        dataService = DataService()
        review_lr = dataService.review
        beer_lr = dataService.beer.na.drop()

        agg_dataset = review_lr.withColumnRenamed('id', 'rid').join(beer_lr, review_lr.beerid ==  beer_lr.id, "inner")
        train_df, test_df = agg_dataset.randomSplit([0.8, 0.2])

        self.lrModel = Regressortrain(train_df)
    
    def similarItems(self, items, count):
        spark = SparkService()

        dataService = DataService()
        beer_to_search = dataService.beer[dataService.beer['id'].isin(items)]
        beer_to_search_from = dataService.beer[dataService.beer['id'].isin(items) == False].na.drop()
        items_dataset = beer_to_search.join(dataService.brewer,beer_to_search.brewerid ==  dataService.brewer.id,"inner")
        source_dataset = beer_to_search_from.join(dataService.brewer,beer_to_search_from.brewerid ==  dataService.brewer.id,"inner")
        return findNearestNeighbour(source_dataset,items_dataset,self.brpModel,self.brpPipeline, count)
    
    def predictItems(self, users, numitems):
        spark = SparkService()
        df = spark.spark.createDataFrame(data=users, schema =  StructType([StructField("reviewerid", IntegerType(), True)]))
        return predictItems(df, numitems,self.als)

    def predictUsers(self, beers, numusers):
        spark = SparkService()
        df = spark.spark.createDataFrame(data=beers, schema = StructType([StructField("beerid", IntegerType(), True)]))
        return predictUsers(df, numusers, self.als)
    
    def rateBeers(self, beers):
        spark = SparkService()
        df = spark.spark.createDataFrame(data=beers, schema = StructType([StructField("beerid", IntegerType(), True)]))
        return predictRatings(df, self.lrModel)


    