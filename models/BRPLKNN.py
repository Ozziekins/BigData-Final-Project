from pyspark.ml.feature import Word2Vec, Tokenizer,StopWordsRemover, StandardScaler
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import VectorAssembler, BucketedRandomProjectionLSH, BucketedRandomProjectionLSHModel
import os
from definitions import ROOT_DIR
from pyspark.sql.functions import col


model_file = os.path.join(ROOT_DIR, 'modelBRP')
pipeline_file = os.path.join(ROOT_DIR, 'pipelineBRP')

def init_pipeline():
    text_features = ['brewery_name','name','style']
    tokenizers = [
        Tokenizer(inputCol = feature, outputCol=feature + 'token')
        for feature in text_features
    ]
    swremovals = [
        StopWordsRemover(inputCol=feature + 'token', outputCol=feature + 'sw')
        for feature in text_features
    ]
    text_encoders = [
        Word2Vec(vectorSize=20, minCount=0, inputCol = feature + 'sw', outputCol=feature + 'enc')
        for feature in text_features
    ]


    final_assembler = VectorAssembler(
        inputCols = [feature + 'enc' for feature in text_features]+['abv'],
        outputCol = 'processed_features'
    )
    scaler = StandardScaler(inputCol = "processed_features", outputCol = "scaled_features")


    pipeline = Pipeline(stages=tokenizers+swremovals+text_encoders+[
        final_assembler,
        scaler])
    
    return pipeline


def train(train_df, overwrite=True, pipelinefilename=pipeline_file, modelfilename=model_file):
    # beer = beer.na.drop()
    # agg_dataset = beer.join(brewer,beer.brewerid ==  brewer.id,"inner")
    # train_df, test_df = agg_dataset.randomSplit([0.8, 0.2])
    pipeline = init_pipeline()
    model = pipeline.fit(train_df)
    if(overwrite):
        model.save(pipelinefilename)
    train_transformed = model.transform(train_df)
    brp = BucketedRandomProjectionLSH(inputCol="scaled_features", outputCol="hashes", bucketLength=2.0,
                                  numHashTables=3)
    brp_model = brp.fit(train_transformed)
    if(overwrite):
        brp_model.save(modelfilename)
    return model, brp_model

def load_model(modelfilename=model_file, pipelinefilename=pipeline_file):
    model, pipeline = None, None
    if os.path.exists(modelfilename):
        model = BucketedRandomProjectionLSHModel.load(modelfilename)
    if os.path.exists(pipelinefilename):
        pipeline = PipelineModel.load(pipelinefilename)
    return model, pipeline

def findNearestNeighbour(source_dataset, predict_dataset,model, pipeline, count = 5):
    if model is not None and pipeline is not None:
        train_transformed = pipeline.transform(source_dataset)
        test_transformed = pipeline.transform(predict_dataset)
        return model.approxNearestNeighbors(train_transformed, test_transformed.first()['scaled_features'], int(count))[[col('spark_catalog.projectdb.beer_buck.id'),'name','abv','style','brewery_name']].collect()
    else:
        raise Exception("Model or Pipeline Not available")
