from alsmodel import loadModel as loadALSModel, predictItems, predictUsers, train as ALSTrain
from BRPLKNN import findNearestNeighbour, load_model as loadBRPModel, train as BRPtrain
from DataService import DataService
from SparkService import SparkService

class ModelService:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ModelService, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.als = loadALSModel()
        self.brpModel, self.brpPipeline = loadBRPModel()
        self.dataService = DataService()

    def retrainALS(self):
        train_df, test_df = self.dataService.review.randomSplit([0.8, 0.2], 42)
        self.als = ALSTrain(train_df)    
    
    def retrainBRP(self):
        beer = self.dataService.beer.na.drop()
        agg_dataset = beer.join(self.dataService.brewer,beer.brewerid ==  self.dataService.brewer.id,"inner")
        train_df, test_df = agg_dataset.randomSplit([0.8, 0.2], 42)
        self.brpPipeline, self.brpModel = BRPtrain(train_df)
    
    def similarItems(self, items, count):
        beer = self.dataService.beer.na.drop()
        agg_dataset = beer.join(self.dataService.brewer,beer.brewerid ==  self.dataService.brewer.id,"inner")
        source_dataset = agg_dataset[~agg_dataset['beer.id'].isin(items)].count()
        items_dataset = agg_dataset[agg_dataset['beer.id'].isin(items)].count()
        return findNearestNeighbour(source_dataset,items_dataset,self.brpModel,self.brpPipeline, count)
    
    def predictItems(self, users, numitems):
        spark = SparkService()
        df = spark.spark.createDataFrame(data=users, schema = ["reviewerid"])
        return predictItems(df, numitems,self.als)

    def predictUsers(self, beers, numusers):
        spark = SparkService()
        df = spark.spark.createDataFrame(data=beers, schema = ["beerid"])
        return predictUsers(df, numusers, self.als)


    