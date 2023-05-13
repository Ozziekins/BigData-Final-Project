from pyspark.ml.recommendation import ALS,ALSModel
import os

def train( train_df,maxIter = 10, rank = 4, regParam = 0.01, overwrite=False):   
    als = ALS(maxIter=maxIter, rank=rank, regParam=regParam, userCol='beerid', itemCol='reviewerid', ratingCol='total')
    model = als.fit(train_df)
    if(overwrite):
        model.save("alsmodel")
    return model

def loadModel(filename='alsmodel'):
   if(os.path.exists(filename)):
       return ALSModel.load("alsmodel")
   else:
       return None

def predictItems(df, numitems, model):
    if(model is not None):
        return model.recommendForUserSubset(df, numitems)['beerid']
    else:
        raise Exception("Model not available")

def predictUsers(df, numusers, model):
    if(model is not None):
        return model.recommendForItemSubset(df, numusers)['reviewerid']
    else:
        raise Exception("Model not available")