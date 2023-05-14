from pyspark.ml.regression import LinearRegression, LinearRegressionModel
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StringIndexer
import os
from definitions import ROOT_DIR


file = os.path.join(ROOT_DIR, 'modelRegression')

def train(train_df, maxIter = 10, regParam = 0.01, overwrite=True): 
    text_features = ['style']

    indexer = [
        StringIndexer(inputCol = feature, outputCol=feature + '_indexed')
        for feature in text_features
    ]

    assembler = VectorAssembler(
        inputCols=['rid', 'abv', 'style_indexed', 'id'],
        outputCol='features')

    pipeline = Pipeline(stages=indexer+[assembler])
        

    model = pipeline.fit(train_df)
    train_transformed = model.transform(train_df)

    lr = LinearRegression(maxIter=maxIter, regParam=regParam, featuresCol='features', labelCol='total')
    model = lr.fit(train_transformed)

    if(overwrite):
        model.save(file)
    return model

def loadModel(filename=file):
    try:
       model = LinearRegression.load(filename)
       return model
    except Exception as ex:
        return None

def predictRatings(df, model):
    if(model is not None):
        return model.predict(df).collect()
    else:
        raise Exception("Model not available")
