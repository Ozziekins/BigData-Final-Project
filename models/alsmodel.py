from pyspark.ml.recommendation import ALS,ALSModel
import os
from definitions import ROOT_DIR


file = os.path.join(ROOT_DIR, 'modelALS')

def train( train_df,maxIter = 10, rank = 4, regParam = 0.01, overwrite=True):   
    als = ALS(maxIter=maxIter, rank=rank, regParam=regParam, userCol='reviewerid', itemCol='beerid', ratingCol='total')
    model = als.fit(train_df)
    if(overwrite):
        model.save(file)
    return model

def loadModel(filename=file):
    try:
       model = ALSModel.load(filename)
       return model
    except Exception as ex:
        print(ex)
        return None

def predictItems(df, numitems, model):
    if(model is not None):
        return model.recommendForUserSubset(df, numitems).collect()
    else:
        raise Exception("Model not available")

def predictUsers(df, numusers, model):
    if(model is not None):
        return model.recommendForItemSubset(df, numusers).collect()
    else:
        raise Exception("Model not available")