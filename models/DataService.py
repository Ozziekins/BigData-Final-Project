from SparkService import SparkService
from pyspark.sql.types import DecimalType
from pyspark.sql.functions import col, month, translate

class DataService(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataService, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        spark = SparkService()
        beer = spark.spark.read.format("avro").table('projectdb.beer_buck')
        beer.createOrReplaceTempView('beer_buck')

        brewer = spark.spark.read.format("avro").table('projectdb.brewer_buck')
        brewer.createOrReplaceTempView('brewer_buck')

        person = spark.spark.read.format("avro").table('projectdb.person_buck')
        person.createOrReplaceTempView('person_buck')

        review = spark.spark.read.format("avro").table('projectdb.review_buck')
        review.createOrReplaceTempView('review_buck')

        beer = beer.withColumn('name', translate("name","'",""))\
        .withColumn('style', translate("style","'",""))\
        .withColumn('abv', col('abv').cast(DecimalType()))

        brewer = brewer.withColumn('brewery_name', translate("brewery_name","'",""))
        
        person = person.withColumn('profilename', translate("profilename","'",""))
        
        review = review.withColumn('appearance', col('appearance').cast(DecimalType()))\
        .withColumn('aroma', col('aroma').cast(DecimalType()))\
        .withColumn('palate', col('palate').cast(DecimalType()))\
        .withColumn('taste', col('taste').cast(DecimalType()))\
        .withColumn('total', col('total').cast(DecimalType()))\
        .withColumn('month', month('time'))

        self.beer = beer
        self.review =  review
        self.person = person
        self.brewer = brewer